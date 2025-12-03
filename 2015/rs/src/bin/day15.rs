use regex::Regex;
use std::io;

fn calculate_score(ingredients: &Vec<Vec<i32>>, teaspoons: [i32; 4]) -> (i32, i32) {
    let mut sums = vec![0; ingredients[0].len()];

    for (properties, teaspoon) in ingredients.iter().zip(teaspoons) {
        for (i, property) in properties.iter().enumerate() {
            sums[i] += teaspoon * property;
        }
    }

    let mut score = 1;
    for sum in sums.iter().take(sums.len() - 1) {
        if *sum < 0 {
            return (0, 0);
        }
        score *= sum;
    }

    (score, *sums.last().expect("No properties found in sums"))
}

fn parse_ingredients() -> Vec<Vec<i32>> {
    let re = Regex::new(r"-?\d+").expect("Failed to compile regex");
    io::stdin()
        .lines()
        .map(|result| {
            let line = result.expect("Failed to read a line from stdin");
            re.find_iter(line.as_str())
                .map(|m| {
                    m.as_str()
                        .parse::<i32>()
                        .expect("Failed to parse a property value as i32")
                })
                .collect()
        })
        .collect()
}

fn main() {
    let mut part1 = 0;
    let mut part2 = 0;

    let ingredients = parse_ingredients();

    for i in 0..=100 {
        for j in 0..=(100 - i) {
            for k in 0..=(100 - i - j) {
                let m = 100 - i - j - k;
                let (score, calories) = calculate_score(&ingredients, [i, j, k, m]);
                part1 = part1.max(score);

                if calories == 500 {
                    part2 = part2.max(score);
                }
            }
        }
    }

    println!("{part1}");
    println!("{part2}");
}
