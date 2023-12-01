use std::fs;

fn main() {
    let input = "data/day_01_a.txt";
    let contents = fs::read_to_string(input).unwrap();

    let mut sum = 0;
    for line in contents.lines() {
        let mut first_digit = 0;
        let mut second_digit = 0;
        for char in line.chars() {
            if char.is_ascii_digit() {
                first_digit = char.to_digit(10).unwrap();
                break;
            }
        }
        for char in line.chars().rev() {
            if char.is_ascii_digit() {
                second_digit = char.to_digit(10).unwrap();
                break;
            }
        }
        sum += 10 * first_digit + second_digit;
}
    dbg!(sum);

}
