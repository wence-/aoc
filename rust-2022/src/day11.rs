use std::{cmp::Reverse, str::from_utf8};

#[derive(Debug, Copy, Clone)]
enum Op {
    A,
    M,
    P,
}

#[derive(Debug, Clone)]
pub struct Monkey {
    items: Vec<usize>,
    op: (Op, usize),
    divisor: usize,
    target_false: usize,
    target_true: usize,
    count: usize,
}

pub fn read(inp: &[u8]) -> Vec<Monkey> {
    let mut v = Vec::new();
    let mut c = 0;
    let mut items = vec![];
    let mut op = (Op::A, 0);
    let mut divisor = 0;
    let mut target_false = 0;
    let mut target_true = 0;
    for line in inp.split(|&c| c == b'\n') {
        if line.is_empty() {
            continue;
        }
        match c {
            0 => (),
            1 => {
                items = from_utf8(&line[18..])
                    .unwrap()
                    .split(", ")
                    .map(|n| n.parse::<usize>().unwrap())
                    .collect::<Vec<_>>()
            }
            2 if line[25] == b'o' => op = (Op::P, 2),
            2 if line[23] == b'+' => {
                op = (
                    Op::A,
                    from_utf8(&line[25..]).unwrap().parse::<usize>().unwrap(),
                )
            }
            2 if line[23] == b'*' => {
                op = (
                    Op::M,
                    from_utf8(&line[25..]).unwrap().parse::<usize>().unwrap(),
                )
            }
            3 => divisor = from_utf8(&line[21..]).unwrap().parse::<usize>().unwrap(),
            4 => target_true = (line[line.len() - 1] - b'0') as usize,
            5 => {
                target_false = (line[line.len() - 1] - b'0') as usize;
            }
            _ => unreachable!(),
        }
        c += 1;
        if c == 6 {
            c = 0;
            v.push(Monkey {
                items: items.to_owned(),
                op,
                divisor,
                target_false,
                target_true,
                count: 0,
            });
        }
    }
    v
}

#[inline]
fn compute(item: usize, op: (Op, usize)) -> usize {
    match op.0 {
        Op::A => item + op.1,
        Op::M => item * op.1,
        Op::P => item * item,
    }
}

pub fn part1(inp: &[Monkey]) -> usize {
    let mut inp = inp.to_vec();
    for _ in 0..20 {
        for i in 0..inp.len() {
            for j in 0..inp[i].items.len() {
                let item = inp[i].items[j];
                let item = compute(item, inp[i].op) / 3;
                let dest = if item % inp[i].divisor == 0 {
                    inp[i].target_true
                } else {
                    inp[i].target_false
                };
                inp[dest].items.push(item);
                inp[i].count += 1;
            }
            inp[i].items.clear();
        }
    }
    inp.select_nth_unstable_by_key(2, |s| Reverse(s.count));
    inp[0].count * inp[1].count
}

pub fn part2(inp: &[Monkey]) -> usize {
    let mut inp = inp.to_vec();
    let lcm = inp.iter().fold(1, |acc, m| acc * m.divisor);
    for _ in 0..10_000 {
        for i in 0..inp.len() {
            for j in 0..inp[i].items.len() {
                let item = inp[i].items[j];
                let item = compute(item, inp[i].op) % lcm;
                let dest = if item % inp[i].divisor == 0 {
                    inp[i].target_true
                } else {
                    inp[i].target_false
                };
                inp[dest].items.push(item);
                inp[i].count += 1;
            }
            inp[i].items.clear();
        }
    }
    inp.sort_unstable_by_key(|s| Reverse(s.count));
    inp[0].count * inp[1].count
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day11.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
