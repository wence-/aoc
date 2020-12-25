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

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day10.input"));
    let data = read(&contents);
    let p1 = format!("{}", part1(&data));
    let p2 = format!("{}", part2(&data));
    return (p1, p2);
}
