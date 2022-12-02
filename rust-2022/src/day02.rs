type I = u8;

pub fn read(inp: &[u8]) -> Vec<[I; 2]> {
    let mut v = Vec::with_capacity(4096);
    for line in inp.split(|&c| c == b'\n') {
        v.push([line[0] - b'A', line[2] - b'X']);
    }
    v
}

pub fn part1(inp: &[[I; 2]]) -> u16 {
    inp.iter().fold(0u16, |acc, &[you, me]| {
        acc + ((me + 1 + 3 * (((me + 4) - you) % 3)) as u16)
    })
}

pub fn part2(inp: &[[I; 2]]) -> u16 {
    inp.iter().fold(0u16, |acc, &[you, result]| {
        acc + (((you + result + 2) % 3 + 1 + 3 * result) as u16)
    })
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day02.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
