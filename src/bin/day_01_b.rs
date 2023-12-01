use std::fs;

fn main() {
    let input = "data/day_01_b.txt";
    let contents = fs::read_to_string(input).unwrap();

    let mut sum = 0;
    for line in contents.lines() {
        // println!("First from left!");
        // Starting normally finding the first digit as number or as word (from right to left)
        let mut first_digit = 0;
        let mut index_left = line.len();
        for (idx, number) in [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        ]
        .iter()
        .enumerate()
        {
            let first_word_digit = line.find(number);
            match first_word_digit {
                None => (),
                Some(i) => {
                    if i < index_left {
                        index_left = i;
                        first_digit = idx;
                    }
                }
            };

            // println!(
            //     "{:?} word {}({}). Smallest index is {:?}",
            //     first_word_digit, number, idx, index_left
            // );
        }
        for (idx, char) in line.char_indices() {
            if char.is_ascii_digit() {
                if idx < index_left {
                    index_left = idx;
                    first_digit = char.to_digit(10).unwrap() as usize;
                    // println!("Number {} is earlier at index {}", first_digit, idx);
                }
                break;
            }
        }

        // println!("Now from right!");
        // Now the same in reverse (from right to left)
        let mut second_digit = 0;
        let mut index_right = 0;
        for (idx, number) in [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        ]
        .iter()
        .enumerate()
        {
            let second_word_digit = line.rfind(number);
            match second_word_digit {
                None => (),
                Some(i) => {
                    if i > index_right {
                        index_right = i;
                        second_digit = idx;
                    }
                }
            };

            // println!(
            //     "{:?} word {}({}). Largest index is {:?}",
            //     second_word_digit, number, idx, index_right
            // );
        }
         for (idx, char) in line.char_indices().rev() {
            if char.is_ascii_digit() {
                if idx >= index_right {
                    index_right = idx;
                    second_digit = char.to_digit(10).unwrap() as usize;
                    // println!("Number {} is earlier at index {}", second_digit, idx);
                }
                break;
            }
        }
        let summand = 10 * first_digit + second_digit;
        // println!("Adding {} to the total sum", summand);
        // println!("Next...");
        // println!("");
        // println!("");
        println!("{}", summand);
        sum += summand
    }
    dbg!(sum);
}
