use std::fs;

fn main() {
    let input = "data/day_04.txt";
    let contents = fs::read_to_string(input).unwrap();

    let mut tot_points = 0;
    for line in contents.lines() {
        let card: Vec<_> = line.split(['|', ':'].as_ref()).collect();
        let my_numbers: Vec<_> = card[1].split_whitespace().collect();
        let win_numbers: Vec<_> = card[2].split_whitespace().collect();
        let mut card_points = 0;
        for my_number in &my_numbers {
            for win_number in &win_numbers {
                if my_number == win_number {
                    if card_points == 0 {
                        card_points = 1
                    } else {
                        card_points *= 2;
                    }
                }
            }
        }
        tot_points += card_points;
    }
    println!("{}", tot_points);
}
