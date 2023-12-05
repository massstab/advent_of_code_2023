use std::fs;

fn main() {
    let input = "data/day_03.txt";
    let contents = fs::read_to_string(input).unwrap();
    let mut number_of_lines = 0;
    let line_len: usize = contents.lines().nth(0).unwrap().len();

    //Stragegy: find all digits, place them in a .
    let mut numbers_vector: Vec<Numbers> = Vec::new();
    for (i, line) in contents.lines().enumerate() {
        number_of_lines += 1;
        // println!("{}: {}", i, line);
        let mut digits_str = String::new();
        for (j, char) in line.chars().enumerate() {
            if char.is_ascii_digit() {
                digits_str += &char.to_string();
            } else if digits_str.is_empty() {
                continue;
            } else {
                // println!("{}", digits_str);
                let number = Numbers {
                    number: digits_str.parse().unwrap(),
                    line: i,
                    end_index: j,
                    len_digits: digits_str.len(),
                };
                numbers_vector.push(number);
                digits_str = String::new();
            }
            if j == 9 && char.is_ascii_digit() {
                let number = Numbers {
                    number: digits_str.parse().unwrap(),
                    line: i,
                    end_index: j,
                    len_digits: digits_str.len(),
                };
                numbers_vector.push(number);
                digits_str = String::new();
            }
        }
    }

    // println!("{:?}", numbers_vector);
    for number in numbers_vector {
        // println!("{}, {}", number.end_index, line_len);
        if number.line == 0 {
            // println!("First line {:?}", number);
            continue;
        } else if (number.line as i32) == (number_of_lines as i32 - 1) {
            // println!("Last line {:?}", number);
            continue;
        }
        if (number.end_index as i32) - (number.len_digits as i32) < 0 {
            // println!("Line starts with number {:?}", number);
            continue;
        } else if number.end_index == line_len {
            // println!("Line end with number {:?}", number);
            continue;
        }
        print!("{:?}", number)
    }
    


}

#[derive(Debug)]
struct Numbers {
    number: u32,
    line: usize,
    end_index: usize,
    len_digits: usize,
}
