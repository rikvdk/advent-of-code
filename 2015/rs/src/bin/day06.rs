use std::io;
use std::str::FromStr;

const GRID_SIZE: usize = 1000;

#[derive(Clone, Copy)]
enum Action {
    TurnOn,
    TurnOff,
    Toggle,
}

struct Point {
    x: usize,
    y: usize,
}

impl FromStr for Point {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (x, y) = s
            .split_once(',')
            .ok_or_else(|| format!("Point must be in the form 'x,y', got '{s}'"))?;

        Ok(Self {
            x: x.parse()
                .map_err(|e| format!("Failed to parse x coordinate '{x}': {e}"))?,
            y: y.parse()
                .map_err(|e| format!("Failed to parse y coordinate '{y}': {e}"))?,
        })
    }
}

pub struct Instruction {
    action: Action,
    from: Point,
    to: Point,
}

impl FromStr for Instruction {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (action, rest) = if let Some(r) = s.strip_prefix("turn on ") {
            (Action::TurnOn, r)
        } else if let Some(r) = s.strip_prefix("turn off ") {
            (Action::TurnOff, r)
        } else if let Some(r) = s.strip_prefix("toggle ") {
            (Action::Toggle, r)
        } else {
            return Err(format!("Invalid instruction: {s}"));
        };

        let (from, to) = rest
            .split_once(" through ")
            .ok_or("Instruction must contain ' through ' to separate points")?;
        let from = from.parse()?;
        let to = to.parse()?;

        Ok(Self { action, from, to })
    }
}

fn main() {
    let mut grid1 = vec![false; GRID_SIZE * GRID_SIZE].into_boxed_slice();
    let mut grid2 = vec![0u32; GRID_SIZE * GRID_SIZE].into_boxed_slice();

    let lines = io::stdin()
        .lines()
        .map(|result| result.expect("Failed to read line from stdin"));

    for line in lines {
        let instruction = line
            .parse::<Instruction>()
            .expect("Failed to parse Instruction");

        for y in instruction.from.y..=instruction.to.y {
            for x in instruction.from.x..=instruction.to.x {
                let index = y * GRID_SIZE + x;

                match instruction.action {
                    Action::TurnOn => {
                        grid1[index] = true;
                        grid2[index] += 1;
                    }
                    Action::TurnOff => {
                        grid1[index] = false;
                        grid2[index] = grid2[index].saturating_sub(1);
                    }
                    Action::Toggle => {
                        grid1[index] = !grid1[index];
                        grid2[index] += 2;
                    }
                }
            }
        }
    }

    let part1 = grid1.iter().filter(|&&v| v).count();
    let part2: u32 = grid2.iter().sum();

    println!("{part1}");
    println!("{part2}");
}
