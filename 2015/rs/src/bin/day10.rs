use itertools::Itertools;
use std::io;

fn repeat_look_and_say(mut value: String, count: usize) -> String {
    for _ in 0..count {
        value = value
            .chars()
            .chunk_by(|e| *e)
            .into_iter()
            .flat_map(|(key, group)| [group.count().to_string(), key.to_string()])
            .collect::<String>();
    }

    value
}

fn main() {
    let mut line = String::new();

    io::stdin()
        .read_line(&mut line)
        .expect("Failed to read line");

    line = line.trim_end().to_string();

    let part1_string = repeat_look_and_say(line, 40);
    let part1 = part1_string.len();

    let part2_string = repeat_look_and_say(part1_string, 10);
    let part2 = part2_string.len();

    println!("{part1}");
    println!("{part2}");
}
