use std::collections::HashSet;

pub fn read(contents: &str) -> HashSet<usize> {
    contents
        .lines()
        .map(|line| {
            line.chars()
                .enumerate()
                .map(|(i, c)| match c {
                    'F' | 'L' => 0,
                    'B' | 'R' => 1 << (9 - i),
                    _ => 0,
                })
                .fold(0, |acc, x| x + acc)
        })
        .collect()
}

pub fn part1(data: &HashSet<usize>) -> usize {
    *data.iter().max().unwrap()
}

pub fn part2(data: &HashSet<usize>) -> usize {
    (0..data.len())
        .find(|x| !data.contains(x) && data.contains(&(x + 1)) && data.contains(&(x - 1)))
        .unwrap()
}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day05.input"));
    let data = read(&contents);
    let p1 = format!("{}", part1(&data));
    let p2 = format!("{}", part2(&data));
    (p1, p2)
}
