use std::collections::HashSet;
use std::iter::FromIterator;

pub fn read(contents: &str) -> HashSet<usize> {
    return HashSet::from_iter(contents.lines().map(|line| {
        line.chars()
            .enumerate()
            .map(|(i, c)| match c {
                'F' | 'L' => 0,
                'B' | 'R' => 1 << (9 - i),
                _ => 0,
            })
            .fold(0, |acc, x| x + acc)
    }));
}

pub fn part1(data: &HashSet<usize>) -> usize {
    return *data.iter().max().unwrap();
}

pub fn part2(data: &HashSet<usize>) -> usize {
    return (0..data.len())
        .filter(|x| !data.contains(x) && data.contains(&(x + 1)) && data.contains(&(x - 1)))
        .next()
        .unwrap();
}

pub fn run() -> (usize, usize) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day05.input"));
    let data = read(&contents);
    return (part1(&data), part2(&data));
}
