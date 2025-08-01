use std::io;

fn contains_three_or_more_vowels(bytes: &[u8]) -> bool {
    bytes
        .iter()
        .filter(|c| matches!(c, b'a' | b'e' | b'i' | b'o' | b'u'))
        .count()
        >= 3
}

fn contains_consecutive_duplicates(bytes: &[u8]) -> bool {
    bytes.windows(2).any(|t| t[0] == t[1])
}

fn contains_forbidden_substrings(bytes: &[u8]) -> bool {
    bytes
        .windows(2)
        .any(|t| matches!(t, b"ab" | b"cd" | b"pq" | b"xy"))
}

fn contains_non_overlapping_duplicate_pairs(bytes: &[u8]) -> bool {
    bytes
        .windows(2)
        .enumerate()
        .any(|(i, t)| bytes[i + 2..].windows(2).any(|u| t == u))
}

fn contains_letter_sandwich(bytes: &[u8]) -> bool {
    bytes.windows(3).any(|t| t[0] == t[2])
}

fn is_nice_string_part1(bytes: &[u8]) -> bool {
    contains_three_or_more_vowels(bytes)
        && contains_consecutive_duplicates(bytes)
        && !contains_forbidden_substrings(bytes)
}

fn is_nice_string_part2(bytes: &[u8]) -> bool {
    contains_non_overlapping_duplicate_pairs(bytes) && contains_letter_sandwich(bytes)
}

fn main() {
    let mut part1 = 0;
    let mut part2 = 0;

    let lines = io::stdin()
        .lines()
        .map(|result| result.expect("Failed to read line from stdin"));

    for line in lines {
        let bytes = line.as_bytes();

        if is_nice_string_part1(bytes) {
            part1 += 1;
        }

        if is_nice_string_part2(bytes) {
            part2 += 1;
        }
    }

    println!("{part1}");
    println!("{part2}");
}
