use std::str::FromStr;
use std::{collections::HashMap, io};

#[derive(Clone, Debug)]
enum Signal {
    Const(u16),
    WireRef(String),
}

impl From<&str> for Signal {
    fn from(s: &str) -> Self {
        s.parse()
            .map_or_else(|_| Self::WireRef(s.to_string()), Self::Const)
    }
}

#[derive(Clone, Debug)]
enum Instruction {
    Assign(Signal),
    BitNot(Signal),
    BitAnd(Signal, Signal),
    BitOr(Signal, Signal),
    Shl(Signal, Signal),
    Shr(Signal, Signal),
}

impl FromStr for Instruction {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let parts: Vec<_> = s.split_whitespace().collect();

        match parts.as_slice() {
            [x] => Ok(Self::Assign(Signal::from(*x))),
            ["NOT", x] => Ok(Self::BitNot(Signal::from(*x))),
            [lhs, "AND", rhs] => Ok(Self::BitAnd(Signal::from(*lhs), Signal::from(*rhs))),
            [lhs, "OR", rhs] => Ok(Self::BitOr(Signal::from(*lhs), Signal::from(*rhs))),
            [lhs, "LSHIFT", rhs] => Ok(Self::Shl(Signal::from(*lhs), Signal::from(*rhs))),
            [lhs, "RSHIFT", rhs] => Ok(Self::Shr(Signal::from(*lhs), Signal::from(*rhs))),
            _ => Err(format!("Invalid instruction: {s}")),
        }
    }
}

fn parse_circuit() -> HashMap<String, Instruction> {
    io::stdin()
        .lines()
        .map(|result| {
            let line = result.expect("Failed to read line from stdin");
            let (expr, wire) = line.split_once(" -> ").expect("Invalid line format");
            (
                wire.to_string(),
                expr.parse().expect("Failed to parse instruction"),
            )
        })
        .collect()
}

fn evaluate(circuit: &mut HashMap<String, Instruction>, signal: &Signal) -> u16 {
    let wire = match signal {
        Signal::Const(v) => return *v,
        Signal::WireRef(w) => w,
    };

    let instruction = circuit.get(wire).cloned().expect("Unknown wire");
    let value = match instruction {
        Instruction::Assign(s) => evaluate(circuit, &s),
        Instruction::BitNot(o) => !evaluate(circuit, &o),
        Instruction::BitAnd(lhs, rhs) => evaluate(circuit, &lhs) & evaluate(circuit, &rhs),
        Instruction::BitOr(lhs, rhs) => evaluate(circuit, &lhs) | evaluate(circuit, &rhs),
        Instruction::Shl(lhs, rhs) => evaluate(circuit, &lhs) << evaluate(circuit, &rhs),
        Instruction::Shr(lhs, rhs) => evaluate(circuit, &lhs) >> evaluate(circuit, &rhs),
    };

    circuit.insert(wire.to_string(), Instruction::Assign(Signal::Const(value)));

    value
}

fn main() {
    let mut circuit = parse_circuit();
    let a = Signal::from("a");

    let part1 = evaluate(&mut circuit.clone(), &a);
    circuit.insert("b".to_string(), Instruction::Assign(Signal::Const(part1)));
    let part2 = evaluate(&mut circuit, &a);

    println!("{part1}");
    println!("{part2}");
}
