use std::io::{self, BufRead};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let lines: Vec<String> = io::stdin().lock().lines().collect::<Result<_, _>>()?;
    let lines: Vec<&str> = lines.iter().map(String::as_str).collect();

    let part1 = solve(&lines, 2)?;
    let part2 = solve(&lines, 12)?;

    println!("{part1}");
    println!("{part2}");

    Ok(())
}

fn solve(banks: &[&str], k: usize) -> Result<u64, &'static str> {
    let mut answer = 0;
    let mut digits = vec![0; k + 1];

    for bank in banks {
        digits.fill(0);

        for ch in bank.chars() {
            let digit = ch.to_digit(10).ok_or("Not a digit")?;
            digits[k] = u64::from(digit);

            if let Some(pos) = digits[..k]
                .iter()
                .enumerate()
                .position(|(i, &d)| d == 0 || d < digits[i + 1])
            {
                digits.copy_within(pos + 1.., pos);
            }
        }

        answer += digits.iter().take(k).fold(0, |acc, digit| acc * 10 + digit);
    }

    Ok(answer)
}

#[cfg(test)]
mod tests {
    use super::solve;

    fn test_banks() -> [&'static str; 4] {
        [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ]
    }

    #[test]
    fn solve_part1() {
        let banks = test_banks();
        assert_eq!(solve(&banks, 2), Ok(357));
    }

    #[test]
    fn solve_part2() {
        let banks = test_banks();
        assert_eq!(solve(&banks, 12), Ok(3121910778619));
    }
}
