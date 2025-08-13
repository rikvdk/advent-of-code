use regex::Regex;
use std::io;

const GRID_SIZE: usize = 1000;
const COMMAND_CHAR_INDEX: usize = 6;
const TURN_ON_INDICATOR: char = 'n';
const TURN_OFF_INDICATOR: char = 'f';
const TOGGLE_INDICATOR: char = ' ';

fn main() {
    let mut grid1 = vec![[false; GRID_SIZE]; GRID_SIZE];
    let mut grid2 = vec![[0u32; GRID_SIZE]; GRID_SIZE];

    let re = Regex::new(r"\d+").expect("Failed to compile regex");

    let lines = io::stdin()
        .lines()
        .map(|result| result.expect("Failed to read line from stdin"));

    for line in lines {
        let command = line
            .chars()
            .nth(COMMAND_CHAR_INDEX)
            .expect("Failed to extract command charachter");

        let mut it = re
            .find_iter(&line)
            .map(|m| m.as_str().parse::<usize>().expect("Failed to parse number"));

        let x1 = it.next().expect("Failed to extract first number");
        let y1 = it.next().expect("Failed to extract second number");
        let x2 = it.next().expect("Failed to extract third number");
        let y2 = it.next().expect("Failed to extract fourth number");

        for y in y1..=y2 {
            for x in x1..=x2 {
                match command {
                    TURN_ON_INDICATOR => {
                        grid1[y][x] = true;
                        grid2[y][x] += 1;
                    }
                    TURN_OFF_INDICATOR => {
                        grid1[y][x] = false;
                        grid2[y][x] = grid2[y][x].saturating_sub(1);
                    }
                    TOGGLE_INDICATOR => {
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
