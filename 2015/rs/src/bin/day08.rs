use std::io;

const EXTRA_QUOTES: usize = 2;

fn memory_savings(s: &str) -> usize {
    s.chars()
        .fold((0, false), |(savings, prev_slash), c| {
            match (prev_slash, c) {
                (true, '\\' | '"') => (savings + 1, false),
                (true, 'x') => (savings + 3, false),
                (false, '\\') => (savings, true),
                _ => (savings, false),
            }
        })
        .0
        + EXTRA_QUOTES
}

fn encoded_overhead(s: &str) -> usize {
    s.chars().filter(|&c| c == '\\' || c == '"').count() + EXTRA_QUOTES
}

fn main() {
    let mut part1 = 0;
    let mut part2 = 0;

    let lines = io::stdin()
        .lines()
        .map(|result| result.expect("Failed to read line from stdin"));

    for line in lines {
        part1 += memory_savings(&line);
        part2 += encoded_overhead(&line);
    }

    println!("{part1}");
    println!("{part2}");
}
