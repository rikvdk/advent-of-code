use std::io;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut line = String::new();
    io::stdin()
        .read_line(&mut line)
        .expect("Failed to read line");

    let (part1, part2) = solve(&line)?;

    println!("{part1}");
    println!("{part2}");

    Ok(())
}

fn solve(ranges: &str) -> Result<(usize, usize), &'static str> {
    let mut part1 = 0;
    let mut part2 = 0;

    ranges
        .split(',')
        .map(|range| range.split_once('-').expect("Failed to split range"))
        .map(|(start, end)| start.parse::<usize>().unwrap()..=end.parse::<usize>().unwrap())
        .for_each(|range| {
            for i in range {
                let len = i.ilog10() + 1;
                println!("--- {i} ---");

                for j in 1..len {
                    if len % j != 0 {
                        continue;
                    }
                    println!("  {j}");

                    let times = len / j;
                    let mmm = 10u32.pow(j);
                    let mut v = i as u32;

                    for k in 0..times {
                        print!("{} ", v % mmm);
                        v /= mmm;
                    }
                    println!("");
                }
            }
        });

    Ok((part1, part2))
}

#[cfg(test)]
mod tests {
    #[test]
    fn solve() {
        let ranges = "11-22,95-115,998-1012,1188511880-1188511890,\
            222220-222224,1698522-1698528,446443-446449,38593856-38593862,\
            565653-565659,824824821-824824827,2121212118-2121212124";

        assert_eq!(super::solve(ranges), Ok((1227775554, 4174379265)));
    }
}
