use itertools::Itertools;
use std::collections::HashMap;
use std::io;

fn read_graph() -> HashMap<String, HashMap<String, u32>> {
    io::stdin()
        .lines()
        .map(|result| result.expect("Failed to read line from stdin"))
        .flat_map(|line| {
            let parts: Vec<_> = line.split_whitespace().collect();
            let distance = parts[4].parse().expect("Failed to parse number");

            [
                (parts[0].to_string(), (parts[2].to_string(), distance)),
                (parts[2].to_string(), (parts[0].to_string(), distance)),
            ]
        })
        .fold(HashMap::new(), |mut acc, (start, (end, distance))| {
            acc.entry(start).or_default().insert(end, distance);
            acc
        })
}

fn main() {
    let graph = read_graph();

    let (part1, part2) = graph
        .keys()
        .permutations(graph.len())
        .map(|perm| perm.windows(2).map(|w| graph[w[0]][w[1]]).sum::<u32>())
        .minmax()
        .into_option()
        .expect("Failed to find shortest and longest routes");

    println!("{part1}");
    println!("{part2}");
}
