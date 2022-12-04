pub fn read(lines: &str) -> &str {
    lines
}

pub fn part1(_data: &str) -> usize {
    0
}

pub fn part2(_data: &str) -> usize {
    0
}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day01.input")); // FIXME
    let data = read(contents);
    let p1 = part1(data).to_string();
    let p2 = part2(data).to_string();
    (p1, p2)
}
