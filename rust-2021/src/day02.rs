#[derive(Debug)]
pub enum Move {
    F(i32),
    D(i32),
    Nop,
}

fn parse(word: &[u8]) -> Move {
    match word {
        [b'f', ..] => Move::F((word[8] - b'0') as i32),
        [b'd', ..] => Move::D((word[5] - b'0') as i32),
        [b'u', ..] => Move::D(-((word[3] - b'0') as i32)),
        _ => Move::Nop,
    }
}

pub fn read(inp: &[u8]) -> Vec<Move> {
    inp.split(|&b| b == b'\n').map(parse).collect()
}

pub fn part1(inp: &[Move]) -> i32 {
    let mut h: i32 = 0;
    let mut d: i32 = 0;
    for m in inp {
        match m {
            Move::F(n) => h += n,
            Move::D(n) => d += n,
            Move::Nop => {}
        }
    }
    h * d
}

#[inline(never)]
pub fn part2(inp: &[Move]) -> i32 {
    let mut h: i32 = 0;
    let mut a: i32 = 0;
    let mut d: i32 = 0;
    for m in inp {
        match m {
            Move::F(n) => {
                h += n;
                d += a * n;
            }
            Move::D(n) => a += n,
            Move::Nop => {}
        }
    }
    h * d
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day02.input"));
    let data = read(inp);
    (part1(&data).to_string(), part2(&data).to_string())
}
