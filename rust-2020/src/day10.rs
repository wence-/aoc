use std::iter;

pub fn read(lines: &str) -> Vec<usize> {
    let mut vec = iter::once(0)
        .chain(lines.lines().map(|l| l.parse::<usize>().unwrap()))
        .collect::<Vec<_>>();
    vec.sort_unstable();
    vec.push(vec.last().unwrap() + 3);
    return vec;
}

pub fn part1(data: &Vec<usize>) -> usize {
    let mut ones = 0;
    let mut threes = 0;
    let mut iter = data.iter();
    let mut last = iter.next().unwrap();
    for x in iter {
        match x - last {
            1 => ones += 1,
            3 => threes += 1,
            _ => {}
        }
        last = x;
    }
    return ones * threes;
}

pub fn part2(data: &Vec<usize>) -> usize {
    let mut iter = data.iter().rev();
    let max = *iter.next().unwrap() as usize;
    let mut table = vec![0_usize; max + 1];
    table[max] = 1;
    for &rating in iter {
        table[rating] += (1..=3).map(|i| table[rating + i]).sum::<usize>();
    }
    return table[0];
}

pub static CONTENTS: &str =
    include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day10.input"));
pub fn run() -> (usize, usize) {
    let adapters = read(CONTENTS);
    let p1 = part1(&adapters);
    let p2 = part2(&adapters);
    return (p1, p2);
}
