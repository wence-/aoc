type I = u32;

pub fn read(inp: &str) -> &str {
    inp
}

pub fn part1(_inp: &str) -> I {
    0
}

pub fn part2(_inp: &str) -> I {
    0
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day11.input"));
    let data = read(inp);
    let a = part1(data).to_string();
    let b = part2(data).to_string();
    (a, b)
}
