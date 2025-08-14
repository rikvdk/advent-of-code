use std::{collections::HashMap, io};

#[derive(Clone, Debug)]
enum Instruction {
    Value(u16),
    Not(String),
    And(String, String),
    Or(String, String),
    Lshift(String, String),
    Rshift(String, String),
}

fn read_instructions() -> HashMap<String, Instruction> {
    let mut instructions = HashMap::new();

    let lines = io::stdin()
        .lines()
        .map(|result| result.expect("Failed to read line from stdin"));

    for line in lines {
        let parts: Vec<_> = line.split_whitespace().collect();

        println!("{line}");
        println!("{parts:#?}");

        let instruction = match parts.len() {
            3 => Instruction::Value(parts[0].parse().unwrap()),
            4 => Instruction::Not(parts[1].to_string()),
            5 => match parts[1] {
                "AND" => Instruction::And(parts[0].to_string(), parts[2].to_string()),
                "OR" => Instruction::Or(parts[0].to_string(), parts[2].to_string()),
                "LSHIFT" => Instruction::Lshift(parts[0].to_string(), parts[2].to_string()),
                "RSHIFT" => Instruction::Rshift(parts[0].to_string(), parts[2].to_string()),
                _ => unreachable!(),
            },
            _ => unreachable!(),
        };

        instructions.insert(parts.last().unwrap().to_string(), instruction);

        // println!("{instructions:?} - {parts:?}");
    }

    // println!("{instructions:#?}");
    instructions
}

fn run(instructions: &HashMap<String, Instruction>, wire: &str) -> u16 {
    if let Ok(num) = wire.parse::<u16>() {
        return num;
    }

    // println!("{wire}");

    let instruction = &instructions[wire];
    match instruction {
        Instruction::Value(v) => v.clone(),
        Instruction::Not(o) => !run(&instructions, o),
        Instruction::And(l, r) => run(instructions, l) & run(instructions, r),
        Instruction::Or(l, r) => run(instructions, l) | run(instructions, r),
        Instruction::Lshift(l, r) => run(instructions, l) << run(instructions, r),
        Instruction::Rshift(l, r) => run(instructions, l) >> run(instructions, r),
        _ => unreachable!(),
    }
}

fn main() {
    let instructions = read_instructions();

    let part1 = run(&instructions, "h");
    // let part1 = run(&instructions, "a");
    // instructions["b"] = Instruction::VALUE(part1);
    // let part2 = run(instructions, "a");

    println!("{part1}");
    // println!("{part2}");
}
