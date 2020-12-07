use std::collections;
use std::fs;
use std::path::PathBuf;

fn read() -> collections::HashSet<i32> {
    let mut d = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    d.push("inputs/day01.input");
    let contents = fs::read_to_string(d).expect("ARGH, didn't read");
    let mut data = collections::HashSet::<i32>::new();
    for line in contents.lines() {
        match line.parse::<i32>() {
            Ok(n) => {
                data.insert(n);
            }
            Err(_) => {
                panic!("Could not parse {}", line);
            }
        }
    }
    return data;
}
fn part1(data: &collections::HashSet<i32>) -> Option<i32> {
    for &n in data {
        if data.contains(&(2020 - n)) {
            return Some(n * (2020 - n));
        }
    }
    return None;
}

fn part2(data: &collections::HashSet<i32>) -> Option<i32> {
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
