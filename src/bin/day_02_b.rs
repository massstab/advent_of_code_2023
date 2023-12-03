use std::fs;

fn main() {
    let input = "data/day_02.txt";
    let contents = fs::read_to_string(input).unwrap();
    let mut sum_powers: u32 = 0;

    for line in contents.lines() {
        let parts = line.split(":");
        let parts: Vec<&str> = parts.collect();
        let game_id: i32 = parts[0][5..].parse().unwrap();
        let sets_of_cubes: Vec<&str> = parts[1].split(";").collect();
        let mut min_red: u32 = 0;
        let mut min_green: u32 = 0;
        let mut min_blue: u32 = 0;

        println!("Game ID: {:?}", game_id);
        // println!("Sets of Cubes: {:?}", sets_of_cubes);
        println!("----------");

        for set in sets_of_cubes {
            let subsets = set.split(",");
            let subsets: Vec<&str> = subsets.collect();
            // println!("{:?}", subsets);
            for subset in subsets {
                if subset.chars().last().unwrap() == 'd' {
                    let number = subset[..3].trim().to_string();
                    println!("Red Balls: {}", number);
                    let number = number.parse::<u32>().unwrap();
                    if number > min_red {
                        min_red = number;
                    }
                } else if subset.chars().last().unwrap() == 'n' {
                    let number = subset[..3].trim().to_string();
                    println!("Green Balls: {}", number);
                    let number = number.parse::<u32>().unwrap();
                    if number > min_green {
                        min_green = number; 
                    }
                } else if subset.chars().last().unwrap() == 'e' {
                    let number = subset[..3].trim().to_string();
                    println!("Blue Balls: {}", number);
                    let number = number.parse::<u32>().unwrap();
                    if number > min_blue {
                        min_blue = number;
                    }
                }
            }
            println!("");
        }
        sum_powers += (min_red * min_green * min_blue);
    }
    println!("Sum of minimum set of cubes games: {}", sum_powers);
}
