use std::io::{self, BufRead};
use std::ops::RangeInclusive;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut lines = io::stdin().lock().lines();
    let mut ranges = read_ranges(&mut lines)?;
    let numbers = read_numbers(&mut lines)?;

    let part1 = solve1(&ranges, &numbers);
    let part2 = solve2(&mut ranges);

    println!("{part1}");
    println!("{part2}");

    Ok(())
}

fn solve1(ranges: &[RangeInclusive<usize>], numbers: &[usize]) -> usize {
    numbers
        .iter()
        .filter(|n| ranges.iter().any(|r| r.contains(n)))
        .count()
}

fn solve2(ranges: &mut Vec<RangeInclusive<usize>>) -> usize {
    merge_overlapping_ranges(ranges);
    ranges.iter().map(|r| r.end() - r.start() + 1).sum()
}

fn merge_overlapping_ranges(ranges: &mut Vec<RangeInclusive<usize>>) {
    ranges.sort_by_key(|r| *r.start());

    let mut merged: Vec<RangeInclusive<usize>> = Vec::with_capacity(ranges.len());

    for range in ranges.drain(..) {
        match merged.last_mut() {
            Some(last) if range.start() <= last.end() => {
                let start = *last.start();
                let end = (*range.end()).max(*last.end());
                *last = start..=end;
            }
            _ => merged.push(range),
        }
    }

    *ranges = merged;
}

fn read_ranges(
    lines: &mut std::io::Lines<io::StdinLock<'_>>,
) -> Result<Vec<RangeInclusive<usize>>, Box<dyn std::error::Error>> {
    let mut ranges = vec![];

    for line in lines {
        let line = line?;
        if line.is_empty() {
            break;
        }

        let (start, end) = line.split_once('-').ok_or("bad range")?;
        let start: usize = start.parse()?;
        let end: usize = end.parse()?;

        ranges.push(start..=end);
    }

    Ok(ranges)
}

fn read_numbers(
    lines: &mut std::io::Lines<io::StdinLock<'_>>,
) -> Result<Vec<usize>, Box<dyn std::error::Error>> {
    let mut numbers = vec![];

    for line in lines {
        let line = line?;
        let number = line.parse::<usize>()?;

        numbers.push(number);
    }

    Ok(numbers)
}

#[cfg(test)]
mod tests {
    use super::{solve1, solve2};
    use std::ops::RangeInclusive;

    fn test_ranges() -> [RangeInclusive<usize>; 4] {
        [3..=5, 10..=14, 16..=20, 12..=18]
    }

    fn test_numbers() -> [usize; 6] {
        [1, 5, 8, 11, 17, 32]
    }

    #[test]
    fn solve_part1() {
        let ranges = test_ranges();
        let numbers = test_numbers();
        assert_eq!(solve1(&ranges, &numbers), 3);
    }

    #[test]
    fn solve_part2() {
        let ranges = test_ranges();
        assert_eq!(solve2(&mut ranges.to_vec()), 14);
    }
}
