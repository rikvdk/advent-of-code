use std::collections::HashMap;
use std::io;

fn read_graph() -> HashMap<(String, String), u32> {
    let mut graph = HashMap::new();

    let lines = io::stdin()
        .lines()
        .map(|result| result.expect("Failed to read line from stdin"));

    for _line in lines {
        graph.insert(("foo".to_string(), "bar".to_string()), 10);
    }

    graph
}

fn main() {
    let mut part1 = 0;
    let mut part2 = 0;

    let graph = read_graph();

    println!("{part1}");
    println!("{part2}");
}
