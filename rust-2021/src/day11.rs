type I = u32;
type Input = ();

pub fn read(inp: &str) {
    ()
}

pub fn part1(inp: &Input) -> I {
    0
}

pub fn part2(inp: &Input) -> I {
    0
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day11.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
