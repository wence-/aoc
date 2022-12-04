type Integer = usize;

pub fn read(inp: &str) -> [Integer; 7] {
    let mut v = [Integer::default(); 7];
    for word in inp.as_bytes().split(|&b| b == b',') {
        v[(word[0] - b'0') as usize] += 1;
    }
    v
}

fn solve(inp: &[Integer], n: usize) -> Integer {
    let mut counts = [0usize; 9];
    for (i, &c) in inp.iter().enumerate() {
        counts[i] = c;
    }
    for _ in 0..n {
        let new = counts[0];
        counts.rotate_left(1);
        counts[6] += new;
    }
    counts.into_iter().sum()
}

pub fn part1(inp: &[Integer]) -> Integer {
    solve(inp, 80)
}

pub fn part2(inp: &[Integer]) -> Integer {
    solve(inp, 256)
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day06.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
