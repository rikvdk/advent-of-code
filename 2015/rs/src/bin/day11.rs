use itertools::Itertools;
use std::io;

fn is_valid_password(password: &[u8]) -> bool {
    let contains_increasing_letters = password
        .windows(3)
        .any(|w| w[1] == w[0] + 1 && w[2] == w[1] + 1);

    let contains_illegal_letter = password.iter().any(|&c| [b'i', b'l', b'o'].contains(&c));

    let contains_two_pairs = password
        .windows(2)
        .filter(|w| w[0] == w[1])
        .combinations(2)
        .any(|w| w[0][0] != w[1][0]);

    contains_increasing_letters && !contains_illegal_letter && contains_two_pairs
}

fn increment_password(password: &mut [u8]) {
    for c in password.iter_mut().rev() {
        if *c != b'z' {
            *c += 1;
            break;
        }

        *c = b'a';
    }
}

fn next_password(password: &str) -> String {
    let mut candidate_password = password.as_bytes().to_owned();

    loop {
        increment_password(&mut candidate_password);
        if is_valid_password(&candidate_password) {
            break;
        }
    }

    str::from_utf8(&candidate_password)
        .expect("Failed to convert [u8] into String")
        .to_string()
}

fn main() {
    let mut line = String::new();

    io::stdin()
        .read_line(&mut line)
        .expect("Failed to read line");

    let part1 = next_password(line.trim_end());
    let part2 = next_password(&part1);

    println!("{part1}");
    println!("{part2}");
}
