use std::io;

use itertools::Itertools;

fn parse_dimensions(s: &str) -> [i32; 3] {
    s.split('x')
        .map(|t| t.parse().expect("Failed to parse numbers"))
        .sorted()
        .collect::<Vec<_>>()
        .try_into()
        .unwrap()
}

fn main() {
    let mut part1 = 0;
    let mut part2 = 0;

    let lines = io::stdin().lines().map(Result::unwrap);

    for line in lines {
        let [l, w, h] = parse_dimensions(&line);

        part1 += 3 * l * w + 2 * w * h + 2 * l * h;
        part2 += 2 * l + 2 * w + l * w * h;
    }

    println!("{part1}");
    println!("{part2}");
}
