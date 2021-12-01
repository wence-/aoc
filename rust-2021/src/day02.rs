pub fn read(inp: &str) -> Vec<usize> {
    inp.lines()
        .map(|l| l.parse::<usize>().unwrap())
        .collect::<Vec<_>>()
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
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day02.input"));
    let data = read(&inp);
    return (part1(&data).to_string(), part2(&data).to_string());
}
