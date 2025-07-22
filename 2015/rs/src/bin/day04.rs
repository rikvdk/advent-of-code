use std::io;
use md5::{Md5, Digest};

fn solve(key: &str) -> usize {
    for i in 1.. {
        let mut hasher = Md5::new();

        hasher.update(key.as_bytes());
        hasher.update(i.to_string());

        let x = hasher.finalize();
        let c = &x[0..3];
        if c.iter().all(|y| *y == 0) {
            return i;
        }
        
        // if hasher.finalize().starts_with(b"00") {
        //     return i;
        // }
    }

    return 0;
}

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read input");

    let input = input.trim();

    println!("{}", solve(&input));
    println!("{}", solve(&input));
}
