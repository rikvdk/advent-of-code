use itertools::Itertools;
use regex::Regex;
use std::collections::HashMap;
use std::io;

fn parse_happiness_mapping() -> HashMap<String, HashMap<String, i32>> {
    let mut happiness_map = HashMap::<String, HashMap<String, i32>>::new();

    let re = Regex::new(
        r"([[:alpha:]]+) would (lose|gain) (\d+) happiness units by sitting next to ([[:alpha:]]+).",
    )
    .expect("Failed to compile regex");

    let lines = io::stdin()
        .lines()
        .map(|result| result.expect("Failed to read line from stdin"));

    for line in lines {
        let caps = re.captures(&line).expect("Failed to match line with regex");
        let (a, sign, n, b) = (&caps[1], &caps[2], &caps[3], &caps[4]);

        let value = match sign {
            "lose" => -n.parse::<i32>().expect("Failed to parse number"),
            "gain" => n.parse::<i32>().expect("Failed to parse number"),
            _ => unreachable!(),
        };
        happiness_map
            .entry(a.to_string())
            .or_default()
            .insert(b.to_string(), value);
    }

    happiness_map
}

fn solve(happiness_map: &HashMap<String, HashMap<String, i32>>) -> i32 {
    let keys: Vec<String> = happiness_map.keys().cloned().collect();
    let fixed = &keys[0];

    keys.iter()
        .skip(1)
        .permutations(happiness_map.len() - 1)
        .map(|perm| {
            let first = *perm
                .first()
                .expect("Permutation should have at least one element");
            let last = *perm
                .last()
                .expect("Permutation should have at least one element");

            perm.windows(2)
                .map(|w| happiness_map[w[0]][w[1]] + happiness_map[w[1]][w[0]])
                .sum::<i32>()
                + happiness_map[fixed][first]
                + happiness_map[first][fixed]
                + happiness_map[fixed][last]
                + happiness_map[last][fixed]
        })
        .max()
        .expect("No valid seating arrangements found")
}

fn add_me(happiness_map: &mut HashMap<String, HashMap<String, i32>>) {
    let people: Vec<String> = happiness_map.keys().cloned().collect();
    let me = "me".to_string();

    for person in &people {
        happiness_map
            .entry(person.clone())
            .or_default()
            .insert(me.clone(), 0);

        happiness_map
            .entry(me.clone())
            .or_default()
            .insert(person.clone(), 0);
    }
}

fn main() {
    let mut happiness_map = parse_happiness_mapping();

    let part1 = solve(&happiness_map);
    add_me(&mut happiness_map);
    let part2 = solve(&happiness_map);

    println!("{part1}");
    println!("{part2}");
}
