use std::fs;
use std::path::PathBuf;

fn read() -> Vec<String> {
    let mut d = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    d.push("inputs/day03.input");
    let contents = fs::read_to_string(d).expect("ARGH, didn't read");
    let mut data = Vec::<String>::new();
    for line in contents.lines() {
        data.push(line.to_string());
    }
    return data;
}

fn trees(grid: &Vec<String>, row: usize, col: usize) -> i32 {
    let mut c: i32 = 0;
    for (i, line) in grid.iter().step_by(col).enumerate() {
        if line.chars().nth(i * row % line.len()).unwrap() == '#' {
            c += 1;
        }
    }
    return c;
}

fn part1(data: &Vec<String>) -> i32 {
    return trees(data, 3, 1);
}

fn part2(data: &Vec<String>) -> i32 {
    let skips: [(usize, usize); 5] = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];
    return skips
        .iter()
        .map(|(row, col)| trees(data, *row, *col))
        .fold(1, |acc, x| acc * x);
}

pub fn run() -> (i32, i32) {
    let data = read();
    return (part1(&data), part2(&data));
}
