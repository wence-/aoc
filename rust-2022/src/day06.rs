pub fn read(inp: &[u8]) -> &[u8] {
    inp
}

#[inline]
fn unique<const N: usize>(s: &[u8]) -> bool {
    s.iter()
        .fold(0u64, |acc, &c| acc | (1u64 << (c - 64)))
        .count_ones()
        == N as u32
}

fn solve<const N: usize>(inp: &[u8]) -> usize {
    if let Some((i, _)) = inp
        .windows(N)
        .enumerate()
        .find(|(_, win)| unique::<N>(win))
    {
        i + N
    } else {
        unreachable!()
    }
}

pub fn part1(inp: &[u8]) -> usize {
    solve::<4>(inp)
}

pub fn part2(inp: &[u8]) -> usize {
    solve::<14>(inp)
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day06.input"));
    let data = read(inp);
    let a = part1(data).to_string();
    let b = part2(data).to_string();
    (a, b)
}
