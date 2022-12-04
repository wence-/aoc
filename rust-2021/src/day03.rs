const N: usize = 12;

pub fn read(inp: &str) -> Vec<u32> {
    inp.trim()
        .split('\n')
        .map(|word| u32::from_str_radix(word, 2).unwrap())
        .collect()
}

pub fn part1(inp: &[u32]) -> u32 {
    let n = ((inp.len() + 1) / 2) as u32;
    let mut gamma = 0;
    for i in 0..N {
        let mut t = 0;
        for &b in inp {
            t += ((b & (1 << i)) != 0) as u32;
        }
        let b = (t >= n) as u32;
        gamma |= (1 << i) * b;
    }
    gamma * ((1 << N) - 1 - gamma)
}

#[inline]
fn prune(inp: &[u32], mut bit: u32, flip: bool) -> u32 {
    let mut pruned = inp.to_owned();
    while pruned.len() != 1 {
        let t = pruned.iter().filter(|&b| b & bit != 0).count();
        let keep = ((flip as u32) * bit) ^ (if 2 * t >= pruned.len() { bit } else { 0 });
        pruned.retain(|&bits| bits & bit == keep);
        bit >>= 1;
    }
    pruned[0]
}

pub fn part2(inp: &[u32]) -> u32 {
    prune(inp, 1 << (N - 1), false) * prune(inp, 1 << (N - 1), true)
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day03.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
