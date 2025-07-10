use itertools::Itertools;
use std::io;

fn main() {
    let mut part1 = 0;
    let mut part2 = 0;

    io::stdin()
        .lines()
        .filter_map(Result::ok)
        .map(|line| {
            line.split('x')
                .map(|s| s.parse().expect("Failed to parse numbers"))
                .sorted()
                .collect::<Vec<_>>()
                .try_into()
        })
        .filter_map(Result::<[i32; 3], Vec<i32>>::ok)
        .for_each(|[l, w, h]| {
            part1 += 3 * l * w + 2 * w * h + 2 * l * h;
            part2 += 2 * l + 2 * w + l * w * h;
        });

    println!("{}", part1);
    println!("{}", part2);
}
