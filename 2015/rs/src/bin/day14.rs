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
            .expect("Failed to match line as Reindeer");

        Ok(Reindeer {
            speed: caps[1].parse().unwrap(),
            fly_time: caps[2].parse().unwrap(),
            rest_time: caps[3].parse().unwrap(),
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
                .expect("Failed to parse Reindeer")
        })
        .collect()
}

fn solve1(reindeers: &Vec<Reindeer>, time_limit: i32) -> i32 {
    reindeers
        .iter()
        .map(|reindeer| reindeer.distance(time_limit))
        .max()
        .unwrap()
}

fn solve2(reindeers: &Vec<Reindeer>, time_limit: i32) -> i32 {
    0
}

fn main() {
    let mut reindeers = parse_reindeers();

    let part1 = solve1(&reindeers, 2503);
    let part2 = solve2(&reindeers, 2503);

    println!("{part1}");
    println!("{part2}");
}
