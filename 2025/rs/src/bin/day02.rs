use std::io;

fn main() {
    let mut line = String::new();
    io::stdin()
        .read_line(&mut line)
        .expect("Failed to read line");

    let (part1, part2) = solve(&line);

    println!("{part1}");
    println!("{part2}");
}

fn solve(ranges: &str) -> (usize, usize) {
    let mut part1 = 0;
    let mut part2 = 0;

    for range in ranges.trim().split(',') {
        let (start, end) = range.split_once('-').expect("bad range");
        let start: usize = start.parse().expect("bad number");
        let end: usize = end.parse().expect("bad number");

        for value in start..=end {
            let len = (value.ilog10() + 1) as usize;

            if len % 2 == 0 && has_repeated_parts(value, len, len / 2) {
                part1 += value;
                part2 += value;
                continue;
            }

            for j in 1..len {
                if has_repeated_parts(value, len, j) {
                    part2 += value;
                    break;
                }
            }
        }
    }

    (part1, part2)
}

fn has_repeated_parts(mut value: usize, len: usize, part_len: usize) -> bool {
    if len % part_len != 0 {
        return false;
    }

    let chunk_count = len / part_len;
    let base = 10usize.pow(u32::try_from(part_len).expect("part_len does not fit in u32"));
    let part = value % base;

    for _ in 1..chunk_count {
        value /= base;

        if value % base != part {
            return false;
        }
    }

    true
}

#[cfg(test)]
mod tests {
    #[test]
    fn solve() {
        let ranges = "11-22,95-115,998-1012,1188511880-1188511890,\
            222220-222224,1698522-1698528,446443-446449,38593856-38593862,\
            565653-565659,824824821-824824827,2121212118-2121212124";

        assert_eq!(super::solve(ranges), (1227775554, 4174379265));
    }
}
