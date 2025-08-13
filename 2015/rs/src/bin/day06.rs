use regex::Regex;
use std::io;

const GRID_SIZE: usize = 1000;

fn main() {
    let mut grid1 = [[false; GRID_SIZE]; GRID_SIZE];
    let mut grid2 = [[0u32; GRID_SIZE]; GRID_SIZE];

    let re = Regex::new(r"\d+")
        .expect("Failed to compile regex");

    let lines = io::stdin()
        .lines()
        .map(|result| result.expect("Failed to read line from stdin"));

    for line in lines {
        let mut it = re.find_iter(&line)
            .map(|m| m.as_str().parse::<usize>().expect("Failed to parse usize"));

        let command = line.chars().nth(6).expect("Failed to get 6th charachter");
        let x1 = it.next().expect("Failed to extract first number");
        let y1 = it.next().expect("Failed to extract second number");
        let x2 = it.next().expect("Failed to extract third number");
        let y2 = it.next().expect("Failed to extract fourth number");

        for y in y1..=y2 {
            for x in x1..=x2 {
                match command {
                    'n' => {
                        grid1[y][x] = true;
                        grid2[y][x] += 1;
                    }
                    'f' => {
                        grid1[y][x] = false;
                        grid2[y][x] = grid2[y][x].saturating_sub(1);
                    }
                    ' ' => {
                        grid1[y][x] = !grid1[y][x];
                        grid2[y][x] += 2;
                    }
                    _ => unreachable!(),
                }
            }
        }
    }

    let part1 = grid1.iter().flatten().filter(|&&v| v).count();
    let part2: u32 = grid2.iter().flatten().sum();

    println!("{part1}");
    println!("{part2}");
}
