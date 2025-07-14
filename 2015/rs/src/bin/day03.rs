use std::collections::HashSet;
use std::io;

fn main() {
    let mut part1 = HashSet::new();
    let mut part2 = HashSet::new();

    let mut current = (0, 0);
    let mut santa = (0, 0);
    let mut robot = (0, 0);

    part1.insert(current);
    part2.insert(current);

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read input");

    for (i, c) in input.trim().chars().enumerate() {
        let (dx, dy) = match c {
            '^' => (0, 1),
            '>' => (1, 0),
            'v' => (0, -1),
            '<' => (-1, 0),
            _ => panic!("Unexpected input"),
        };
        current = (current.0 + dx, current.1 + dy);
        part1.insert(current);

        if i % 2 == 0 {
            santa = (santa.0 + dx, santa.1 + dy);
            part2.insert(santa);
        } else {
            robot = (robot.0 + dx, robot.1 + dy);
            part2.insert(robot);
        }
    }

    println!("{}", part1.len());
    println!("{}", part2.len());
}
