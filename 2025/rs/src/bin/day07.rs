use std::io::{self, BufRead};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut lines: Vec<Vec<u8>> = io::stdin()
        .lock()
        .lines()
        .map(|l| l.map(std::string::String::into_bytes))
        .collect::<Result<_, _>>()?;

    let (part1, part2) = solve(&mut lines);

    println!("{part1}");
    println!("{part2}");

    Ok(())
}

fn solve(lines: &mut [Vec<u8>]) -> (usize, usize) {
    let mut part1 = 0;
    let height = lines.len();
    let width = lines[0].len();

    let start_index = lines[0]
        .iter()
        .position(|&c| c == b'S')
        .expect("No starting position found");

    let mut values = vec![vec![0usize; width]; 2];
    values[0][start_index] = 1;

    for i in 1..height {
        for j in 0..width {
            let prev = lines[i - 1][j];
            let curr = lines[i][j];

            if prev == b'|' || prev == b'S' {
                if curr == b'^' {
                    part1 += 1;
                    values[1][j - 1] += values[0][j];
                    values[1][j + 1] += values[0][j];
                    lines[i][j - 1] = b'|';
                    lines[i][j + 1] = b'|';
                } else {
                    values[1][j] += values[0][j];
                    lines[i][j] = b'|';
                }
            }
        }

        values.swap(0, 1);
        values[1].fill(0);
    }

    (part1, values[0].iter().sum())
}

#[cfg(test)]
mod tests {
    use super::solve;

    fn test_lines() -> [Vec<u8>; 16] {
        [
            b".......S.......".to_vec(),
            b"...............".to_vec(),
            b".......^.......".to_vec(),
            b"...............".to_vec(),
            b"......^.^......".to_vec(),
            b"...............".to_vec(),
            b".....^.^.^.....".to_vec(),
            b"...............".to_vec(),
            b"....^.^...^....".to_vec(),
            b"...............".to_vec(),
            b"...^.^...^.^...".to_vec(),
            b"...............".to_vec(),
            b"..^...^.....^..".to_vec(),
            b"...............".to_vec(),
            b".^.^.^.^.^...^.".to_vec(),
            b"...............".to_vec(),
        ]
    }

    #[test]
    fn test_solve() {
        let mut lines = test_lines();
        assert_eq!(solve(&mut lines), (21, 40));
    }
}
