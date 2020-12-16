use std::collections::HashSet;
use std::iter::FromIterator;

pub fn read(contents: &str) -> HashSet<i32> {
    return HashSet::from_iter(contents.lines().map(|line| line.parse::<i32>().unwrap()));
}

pub fn part1(data: &HashSet<i32>) -> Option<i32> {
    for &n in data {
        if data.contains(&(2020 - n)) {
            return Some(n * (2020 - n));
        }
    }
    return None;
}

pub fn part2(data: &HashSet<i32>) -> Option<i32> {
    for &n in data {
        for &p in data {
            if data.contains(&(2020 - n - p)) {
                return Some(n * p * (2020 - n - p));
            }
        }
    }
    return None;
}

pub fn run() -> (i32, i32) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day01.input"));
    let data = read(&contents);
    return (part1(&data).unwrap(), part2(&data).unwrap());
}
