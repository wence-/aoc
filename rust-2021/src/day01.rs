fn parse(word: &[u8]) -> usize {
    word.iter().fold(0, |a, b| 10 * a + (b - b'0') as usize)
}

pub fn read(inp: &[u8]) -> Vec<usize> {
    inp.split(|&b| b == b'\n').map(parse).collect()
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
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day01.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
