use std::io;

fn main() {
    let mut part1 = 0;
    let mut part2 = 0;

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read input");

    for (i, c) in input.chars().enumerate() {
        match c {
            '(' => part1 += 1,
            ')' => part1 -= 1,
            _ => (),
        }

        if part2 == 0 && part1 == -1 {
            part2 = i + 1;
        }
    }

    println!("{}", part1);
    println!("{}", part2);
}
