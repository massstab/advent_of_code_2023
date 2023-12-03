use std::fs;

const RED: u8 = 12;
const GREEN: u8 = 13;
const BLUE: u8 = 14;

fn main() {
    let input = "data/day_01_a.txt";
    let contents = fs::read_to_string(input).unwrap();
    let mut sum_id = 0;

    'outer: for line in contents.lines() {
        let parts = line.split(":");
        let parts: Vec<&str> = parts.collect();
        let game_id: i32 = parts[0][5..].parse().unwrap();
        let sets_of_cubes: Vec<&str> = parts[1].split(";").collect();

        println!("Game ID: {:?}", game_id);
        println!("Sets of Cubes: {:?}", sets_of_cubes);
        println!("");

        for set in sets_of_cubes {
            let subsets = set.split(",");
            let subsets: Vec<&str> = subsets.collect();
            println!("{:?}", subsets);
            for subset in subsets {
                if subset.chars().last().unwrap() == 'd' {
                    let number = subset[..3].trim().to_string();
                    println!("Red Balls: {}", number);
                    let number = number.parse::<u8>().unwrap();
                    if number > RED {
                        println!("!!GAME {} NOT POSSIBLE!! Too many red  balls!", game_id);
                        continue 'outer;
                    }
                } else if subset.chars().last().unwrap() == 'n' {
                    let number = subset[..3].trim().to_string();
                    println!("Green Balls: {}", number);
                    let number = number.parse::<u8>().unwrap();
                    if number > GREEN {
                        println!("!!GAME {} NOT POSSIBLE!! Too many green balls!", game_id);
                        continue 'outer;
                    }
                } else if subset.chars().last().unwrap() == 'e' {
                    let number = subset[..3].trim().to_string();
                    println!("Blue Balls: {}", number);
                    let number = number.parse::<u8>().unwrap();
                    if number > BLUE {
                        println!("!!GAME {} NOT POSSIBLE!! Too many blue balls!", game_id);
                        continue 'outer;
                    }
                }
            }
            println!("");
        }
        sum_id += game_id;
    }
    println!("Sum of possible games: {}", sum_id);
}
