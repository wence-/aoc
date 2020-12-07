use std::collections;
use std::fs;
use std::path::PathBuf;

fn read() -> Vec<(usize, collections::HashMap<char, usize>)> {
    let mut d = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    d.push("inputs/day06.input");
    let contents = fs::read_to_string(d).expect("ARGH, didn't read");
    let mut vec = Vec::<(usize, collections::HashMap<char, usize>)>::new();
    for group in contents.trim().split("\n\n") {
        let mut data = collections::HashMap::<char, usize>::new();
        let mut n: usize = 0;
        for line in group.trim().split("\n") {
            for c in line.chars() {
                *data.entry(c).or_insert(0) += 1;
            }
            n += 1;
        }
        vec.push((n, data));
    }
    return vec;
}

fn part1(data: &Vec<(usize, collections::HashMap<char, usize>)>) -> usize {
    return data.iter().map(|(_, g)| g.len()).sum();
}

fn part2(data: &Vec<(usize, collections::HashMap<char, usize>)>) -> usize {
    return data
        .iter()
        .map(|(n, g)| g.values().filter(|v| *v == n).count())
        .sum();
}

pub fn run() -> (usize, usize) {
    let data = read();
    let p1 = part1(&data);
    let p2 = part2(&data);
    return (p1, p2);
}
