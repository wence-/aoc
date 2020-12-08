use std::collections::HashSet;
use std::iter::FromIterator;

fn read() -> HashSet<i32> {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day01.input"));
    return HashSet::from_iter(contents.lines().map(|line| line.parse::<i32>().unwrap()));
}

fn part1(data: &HashSet<i32>) -> Option<i32> {
    for &n in data {
        if data.contains(&(2020 - n)) {
            return Some(n * (2020 - n));
        }
    }
    return None;
}

fn part2(data: &HashSet<i32>) -> Option<i32> {
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
    let data = read();
    return (part1(&data).unwrap(), part2(&data).unwrap());
}
