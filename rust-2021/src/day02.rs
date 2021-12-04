#[derive(Debug)]
pub enum Move {
    F(i32),
    D(i32),
}

fn parse(word: &str) -> Move {
    match word.chars().next() {
        Some('f') => Move::F(word[8..].parse::<i32>().unwrap()),
        Some('d') => Move::D(word[5..].parse::<i32>().unwrap()),
        Some('u') => Move::D(-word[3..].parse::<i32>().unwrap()),
        _ => unreachable!(),
    }
}

pub fn read(inp: &str) -> Vec<Move> {
    inp.trim().split('\n').map(parse).collect()
}

pub fn part1(inp: &[Move]) -> i32 {
    let mut h: i32 = 0;
    let mut d: i32 = 0;
    for m in inp {
        match m {
            Move::F(n) => h += n,
            Move::D(n) => d += n,
        }
    }
    h * d
}

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
        }
    }
    h * d
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day02.input"));
    let data = read(inp);
    (part1(&data).to_string(), part2(&data).to_string())
}
