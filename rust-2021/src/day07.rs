use itertools::Itertools;

type T = i16;
type I = i32;

pub fn read(inp: &str) -> Vec<T> {
    inp.trim()
        .split(',')
        .map(|word| word.parse::<T>().unwrap())
        .sorted()
        .collect()
}

pub fn part1(inp: &[T]) -> I {
    let median = inp[inp.len() / 2];
    inp.iter()
        .fold(I::default(), |acc, i| acc + ((i - median).abs() as I))
}

pub fn part2(inp: &[T]) -> I {
    let mean: I = inp.iter().fold(I::default(), |acc, &i| acc + i as I) / (inp.len() as I);
    let mut ret = I::default();
    for &i in inp {
        let diff = (i as I - mean).abs();
        let gauss = diff * (diff + 1);
        ret += gauss;
    }
    ret >> 1
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day07.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
