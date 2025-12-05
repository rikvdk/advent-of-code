use std::io::{self, BufRead};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let lines: Vec<String> = io::stdin().lock().lines().collect::<Result<_, _>>()?;
    let lines: Vec<&str> = lines.iter().map(String::as_str).collect();

    let (part1, part2) = solve(&lines)?;

    println!("{part1}");
    println!("{part2}");

    Ok(())
}

fn solve(instructions: &[&str]) -> Result<(isize, isize), std::num::ParseIntError> {
    let mut answer1 = 0;
    let mut answer2 = 0;
    let mut dial: i32 = 50;

    for instruction in instructions {
        let mut value = instruction[1..].parse::<isize>()?;
        if instruction.starts_with('L') {
            value = -value;
        }

        let direction = if value < 0 { -1 } else { 1 };

        for _ in 0..value.abs() {
            dial = (dial + direction).rem_euclid(100);
            if dial == 0 {
                answer2 += 1;
            }
        }

        if dial == 0 {
            answer1 += 1;
        }
    }

    Ok((answer1, answer2))
}

#[cfg(test)]
mod tests {
    fn test_instructions() -> [&'static str; 10] {
        [
            "L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82",
        ]
    }

    #[test]
    fn solve() {
        let instructions = test_instructions();
        assert_eq!(super::solve(&instructions), Ok((3, 6)));
    }
}
