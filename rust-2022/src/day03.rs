pub fn read(inp: &[u8]) -> Vec<&[u8]> {
    inp.split(|&c| c == b'\n').collect()
}

#[inline]
fn score(c: u32) -> u32 {
    // b'a' - 64; not adding 64 to trailing zeros to get back into
    // ascii, hence weird numbers
    if c < 33 {
        c + 26 // upper case: c - (b'A' - 64) + 27
    } else {
        c - 32 // lower case: c - (b'a' - 64) + 1
    }
}

#[inline]
fn encode(badge: &[u8]) -> u64 {
    badge.iter().fold(0u64, |acc, &c| acc | (1u64 << (c - 64)))
}

pub fn part1(inp: &[&[u8]]) -> u32 {
    inp.iter().fold(0u32, |acc, &line| {
        let n = line.len() >> 1;
        let (left, right) = line.split_at(n);
        let (mut left_badge, mut right_badge) = (0u64, 0u64);
        for i in 0..n {
            left_badge |= 1u64 << (left[i] - 64);
            right_badge |= 1u64 << (right[i] - 64);
        }
        acc + score((left_badge & right_badge).trailing_zeros())
    })
}

pub fn part2(inp: &[&[u8]]) -> u32 {
    inp.chunks_exact(3).fold(0u32, |acc, chunk| {
        let common = chunk
            .iter()
            .fold(u64::MAX, |acc, &badge| acc & encode(badge));
        acc + score(common.trailing_zeros())
    })
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day03.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
