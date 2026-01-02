use std::io::{self, BufRead};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let lines: Vec<String> = io::stdin().lock().lines().collect::<Result<_, _>>()?;
    let lines: Vec<&str> = lines.iter().map(String::as_str).collect();

    let part1 = solve1(&lines)?;
    let part2 = solve2(&lines)?;

    println!("{part1}");
    println!("{part2}");

    Ok(())
}

fn solve1(lines: &[&str]) -> Result<u64, Box<dyn std::error::Error>> {
    let (last_line, numbers_lines) = lines.split_last().ok_or("empty input")?;
    let numbers = parse_numbers(numbers_lines)?;
    let operators: Vec<&str> = last_line.split_whitespace().collect();

    Ok(operators
        .iter()
        .enumerate()
        .map(|(i, &op)| {
            let column = numbers.iter().map(|row| row[i]);
            match op {
                "+" => column.sum::<u64>(),
                "*" => column.product::<u64>(),
                _ => unreachable!(),
            }
        })
        .sum())
}

fn solve2(lines: &[&str]) -> Result<u64, Box<dyn std::error::Error>> {
    let mut result = 0;
    let mut numbers = vec![];
    let mut operator = '+';

    let grid: Vec<Vec<char>> = lines.iter().map(|line| line.chars().collect()).collect();
    let ncols = grid[0].len();

    for col in 0..ncols {
        let mut s: String = grid.iter().map(|row| row[col]).collect();
        let last = s.pop().unwrap_or(' ');
        if last != ' ' {
            operator = last;
        }

        if s.trim().is_empty() {
            result += apply(&numbers, operator);
            numbers.clear();
        } else {
            let number = s.trim().parse::<u64>()?;
            numbers.push(number);
        }
    }

    result += apply(&numbers, operator);
    Ok(result)
}

fn apply(numbers: &[u64], operator: char) -> u64 {
    match operator {
        '+' => numbers.iter().sum::<u64>(),
        '*' => numbers.iter().product::<u64>(),
        _ => unreachable!(),
    }
}

fn parse_numbers(lines: &[&str]) -> Result<Vec<Vec<u64>>, std::num::ParseIntError> {
    lines
        .iter()
        .map(|line| {
            line.split_whitespace()
                .map(str::parse)
                .collect::<Result<Vec<_>, _>>()
        })
        .collect()
}

#[cfg(test)]
mod tests {
    use super::{solve1, solve2};

    fn test_lines() -> Vec<&'static str> {
        vec![
            "123 328  51 64 ",
            " 45 64  387 23 ",
            "  6 98  215 314",
            "*   +   *   +  ",
        ]
    }

    #[test]
    fn test_solve1() {
        let lines = test_lines();
        let result = solve1(&lines).unwrap();
        assert_eq!(result, 4277556);
    }

    #[test]
    fn test_solve2() {
        let lines = test_lines();
        let result = solve2(&lines).unwrap();
        assert_eq!(result, 3263827);
    }
}
