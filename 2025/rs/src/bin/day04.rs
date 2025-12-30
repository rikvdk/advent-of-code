use std::io::{self, BufRead};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut lines: Vec<Vec<u8>> = io::stdin()
        .lock()
        .lines()
        .map(|l| l.map(std::string::String::into_bytes))
        .collect::<Result<_, _>>()?;

    let part1 = solve(&mut lines, false);
    let part2 = solve(&mut lines, true);

    println!("{part1}");
    println!("{part2}");

    Ok(())
}

fn solve(grid: &mut [Vec<u8>], repeat: bool) -> u64 {
    let mut answer = 0;

    let height = grid.len();
    let width = grid[0].len();

    loop {
        let repeat_count = step(grid, width, height, repeat);
        answer += repeat_count;

        if !repeat || repeat_count == 0 {
            break;
        }
    }

    answer
}

fn step(grid: &mut [Vec<u8>], width: usize, height: usize, remove_rolls: bool) -> u64 {
    let mut removed_count = 0;

    for y in 0..height {
        for x in 0..width {
            if grid[y][x] != b'@' {
                continue;
            }

            let count = neighbors(x, y, width, height)
                .filter(|&(nx, ny)| grid[ny][nx] == b'@')
                .count();

            if count < 4 {
                removed_count += 1;

                if remove_rolls {
                    grid[y][x] = b'.';
                }
            }
        }
    }

    removed_count
}

fn neighbors(
    x: usize,
    y: usize,
    width: usize,
    height: usize,
) -> impl Iterator<Item = (usize, usize)> {
    (-1isize..=1)
        .flat_map(move |dy| (-1isize..=1).map(move |dx| (dx, dy)))
        .filter(|&(dx, dy)| dx != 0 || dy != 0)
        .filter_map(move |(dx, dy)| {
            let nx = x.checked_add_signed(dx)?;
            let ny = y.checked_add_signed(dy)?;

            if nx < width && ny < height {
                Some((nx, ny))
            } else {
                None
            }
        })
}

#[cfg(test)]
mod tests {
    use super::solve;

    fn test_grid() -> [Vec<u8>; 10] {
        [
            b"..@@.@@@@.".to_vec(),
            b"@@@.@.@.@@".to_vec(),
            b"@@@@@.@.@@".to_vec(),
            b"@.@@@@..@.".to_vec(),
            b"@@.@@@@.@@".to_vec(),
            b".@@@@@@@.@".to_vec(),
            b".@.@.@.@@@".to_vec(),
            b"@.@@@.@@@@".to_vec(),
            b".@@@@@@@@.".to_vec(),
            b"@.@.@@@.@.".to_vec(),
        ]
    }

    #[test]
    fn solve_part1() {
        let mut grid = test_grid();
        assert_eq!(solve(&mut grid, false), 13);
    }

    #[test]
    fn solve_part2() {
        let mut grid = test_grid();
        assert_eq!(solve(&mut grid, true), 43);
    }
}
