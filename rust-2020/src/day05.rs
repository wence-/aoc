use std::collections;
use std::fs;
use std::path::PathBuf;

fn read() -> collections::HashSet<i32> {
    let mut d = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    d.push("inputs/day05.input");
    let contents = fs::read_to_string(d).expect("ARGH, didn't read");
    let mut data = collections::HashSet::<i32>::new();
    for line in contents.lines() {
        let x: i32 = line
            .chars()
            .enumerate()
            .map(|(i, c)| match c {
                'F' => 0,
                'B' => 1 << (9 - i),
                'R' => 1 << (9 - i),
                'L' => 0,
                _ => 0,
            })
            .fold(0, |acc, x| x + acc);
        data.insert(x);
    }
    return data;
}

fn part1(data: &collections::HashSet<i32>) -> i32 {
    return *data.iter().max().unwrap();
}

fn part2(data: &collections::HashSet<i32>) -> i32 {
    let maxid = *data.iter().max().unwrap() + 1;
    let seat: i32 = (0..maxid)
        .filter(|x| !data.contains(x) && data.contains(&(x + 1)) && data.contains(&(x - 1)))
        .next()
        .unwrap();
    return seat;
}

pub fn run() -> (i32, i32) {
    let data = read();
    return (part1(&data), part2(&data));
}
