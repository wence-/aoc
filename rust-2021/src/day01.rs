type Integer = i16;

pub fn read(inp: &str) -> Vec<Integer> {
    inp.trim()
        .split('\n')
        .map(|word| word.parse::<Integer>().unwrap())
        .collect()
}

#[inline(always)]
fn solve<const N: usize>(inp: &[Integer]) -> Integer {
    inp.iter()
        .zip(inp[N..].iter())
        .fold(0, |acc, (a, b)| acc + Integer::from(b > a))
}

pub fn part1(inp: &[Integer]) -> Integer {
    solve::<1>(inp)
}

pub fn part2(inp: &[Integer]) -> Integer {
    solve::<3>(inp)
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day01.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
