use regex::Regex;
use std::io;
use std::str::FromStr;
use std::sync::LazyLock;

struct Reindeer {
    speed: i32,
    fly_time: i32,
    rest_time: i32,
}

static REINDEER_RE: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(
        r"[[:alpha:]]+ can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",
    )
    .expect("Failed to compile reindeer regex")
});

impl FromStr for Reindeer {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let caps = REINDEER_RE
            .captures(s)
            .ok_or_else(|| format!("Invalid reindeer description: {s}"))?;

        let parse = |i: usize| caps[i].parse::<i32>().map_err(|e| e.to_string());

        Ok(Self {
            speed: parse(1)?,
            fly_time: parse(2)?,
            rest_time: parse(3)?,
        })
    }
}

impl Reindeer {
    fn distance(&self, time_limit: i32) -> i32 {
        let q = time_limit / (self.fly_time + self.rest_time);
        let r = time_limit % (self.fly_time + self.rest_time);

        self.speed * (self.fly_time * q + self.fly_time.min(r))
    }
}

fn parse_reindeers() -> Vec<Reindeer> {
    io::stdin()
        .lines()
        .map(|result| {
            result
                .expect("Failed to read line from stdin")
                .parse()
                .expect("Failed to parse input line into Reindeer")
        })
        .collect()
}

fn max_distance(reindeers: &[Reindeer], time_limit: i32) -> i32 {
    reindeers
        .iter()
        .map(|reindeer| reindeer.distance(time_limit))
        .max()
        .expect("No reindeers found when computing max distance")
}

fn max_points(reindeers: &[Reindeer], time_limit: i32) -> i32 {
    let mut points = vec![0; reindeers.len()];

    for current_time in 1..=time_limit {
        let distances: Vec<_> = reindeers.iter().map(|r| r.distance(current_time)).collect();

        if let Some(&max_distance) = distances.iter().max() {
            distances
                .iter()
                .enumerate()
                .filter(|&(_, &d)| d == max_distance)
                .for_each(|(i, _)| points[i] += 1);
        }
    }

    *points
        .iter()
        .max()
        .expect("No points to compute maximum score")
}

fn main() {
    let reindeers = parse_reindeers();

    let part1 = max_distance(&reindeers, 2503);
    let part2 = max_points(&reindeers, 2503);

    println!("{part1}");
    println!("{part2}");
}
