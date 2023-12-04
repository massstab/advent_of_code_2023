use std::fs;

fn main() {
    let input = "data/day_04.txt";
    let contents = fs::read_to_string(input).unwrap();

    let mut cards: Vec<Card> = Vec::new();

    // Generating a struct Card with all the informations we need and put
    // them in a vector
    for line in contents.lines() {
        let raw_card: Vec<_> = line.split(['|', ':'].as_ref()).collect();
        let id = raw_card[0][5..].trim().to_string().parse::<u32>().unwrap();
        let my_numbers: Vec<_> = raw_card[1].split_whitespace().collect();
        let win_numbers: Vec<_> = raw_card[2].split_whitespace().collect();

        let mut points = 0;
        for my_number in &my_numbers {
            for win_number in &win_numbers {
                if my_number == win_number {
                    points += 1;
                }
            }
        }
        let card: Card = Card {
            id: id.try_into().unwrap(),
            points,
            copies: 1,
        };
        cards.push(card);
    }

    // Now that we have all the first copies. Try to follow the rules to get
    // the other copies
    for i in 0..cards.len() {
        for _ in 0..cards[i].copies {
            let low = cards[i].id + 1;
            let high = cards[i].id + cards[i].points;
            for j in low..high + 1 {
                cards[j - 1].copies += 1;
            }
        }
    }

    // Finally count all cards
    let mut sum = 0;
    for card in cards {
        sum += card.copies;
    }
    print!("Total scratchcards: {:?}", sum)
}

struct Card {
    id: usize,
    points: usize,
    copies: usize,
}
