use md5::{Digest, Md5};
use std::io;

fn solve(key: &str, third_byte_max: u8) -> usize {
    for i in 1.. {
        let mut hasher = Md5::new();

        hasher.update(key.as_bytes());
        hasher.update(i.to_string());

        let digest = hasher.finalize();
        if digest[0] == 0 && digest[1] == 0 && digest[2] <= third_byte_max {
            return i;
        }
    }

    unreachable!("No valid hash found");
}

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read input");

    let input = input.trim();

    println!("{}", solve(input, 0x0F));
    println!("{}", solve(input, 0x00));
}
