use regex::Regex;
use serde_json::Value;
use std::io;

fn sum_numbers(s: &str) -> i64 {
    let re = Regex::new(r"-?\d+").expect("Failed to compile regex");

    re.find_iter(s)
        .map(|m| m.as_str().parse::<i64>().expect("Failed to parse number"))
        .sum()
}

fn sum_numbers_in_value_ignore_red(value: &Value) -> i64 {
    match value {
        Value::Number(n) => n.as_i64().expect("Failed to cast Number to i64"),
        Value::Array(a) => a.iter().map(sum_numbers_in_value_ignore_red).sum(),
        Value::Object(o) => {
            if o.values()
                .any(|v| matches!(v, Value::String(s) if s == "red"))
            {
                0
            } else {
                o.values().map(sum_numbers_in_value_ignore_red).sum()
            }
        }
        _ => 0,
    }
}

fn sum_numbers_ignore_red(s: &[u8]) -> i64 {
    let value: Value = serde_json::from_slice(s).expect("Failed to parse json");
    sum_numbers_in_value_ignore_red(&value)
}

fn main() {
    let mut line = String::new();

    io::stdin()
        .read_line(&mut line)
        .expect("Failed to read line");

    let part1 = sum_numbers(&line);
    let part2 = sum_numbers_ignore_red(line.as_bytes());

    println!("{part1}");
    println!("{part2}");
}
