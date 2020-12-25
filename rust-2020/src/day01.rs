use std::collections::HashSet;
use std::iter::FromIterator;

pub fn read(contents: &str) -> HashSet<i32> {
    return HashSet::from_iter(contents.lines().map(|line| line.parse::<i32>().unwrap()));
}

pub fn part1(data: &HashSet<i32>) -> i32 {
    for &n in data {
        if data.contains(&(2020 - n)) {
            return n * (2020 - n);
        }
    }
    unreachable!();
}

pub fn part2(data: &HashSet<i32>) -> i32 {
    for &n in data {
        for &p in data {
            if data.contains(&(2020 - n - p)) {
                return n * p * (2020 - n - p);
            }
        }
    }
    unreachable!();
}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day01.input"));
    let data = read(&contents);
    let p1 = format!("{}", part1(&data));
    let p2 = format!("{}", part2(&data));
    return (p1, p2);
}
