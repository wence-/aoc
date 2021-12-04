pub fn read(inp: &str) -> Vec<usize> {
    inp.trim()
        .split('\n')
        .map(|word| word.parse::<usize>().unwrap())
        .collect()
}

pub fn part1(inp: &[usize]) -> usize {
    inp.iter()
        .zip(inp[1..].iter())
        .filter(|(a, b)| b > a)
        .count()
}

pub fn part2(inp: &[usize]) -> usize {
    inp.iter()
        .zip(inp[3..].iter())
        .filter(|(a, b)| b > a)
        .count()
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day01.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
