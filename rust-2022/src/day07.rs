use std::collections::HashMap;

pub fn read(inp: &[u8]) -> HashMap<Vec<&[u8]>, u32> {
    let mut tree :HashMap<Vec<&[u8]>, u32> = HashMap::with_capacity(256);
    let mut key = Vec::new();
    for line in inp.split(|&c| c == b'\n') {
        if line[2] == b'c' {
            if line[5] == b'.' {
                key.pop();
            } else {
                key.push(&line[6..]);
            }
        } else if line[0] != b'd' && line[0] != b'$' {
            let n = line
                .split(|&c| c == b' ')
                .next()
                .unwrap()
                .iter()
                .fold(0u32, |acc, &c| acc * 10 + (c - b'0') as u32);
            for i in 0..=key.len() {
                let v = tree.entry((&key[0..i]).to_vec()).or_insert(0);
                *v += n;
            }
        }
    }
    tree
}

pub fn part1(inp: &HashMap<Vec<&[u8]>, u32>) -> u32 {
    inp.values().filter(|&&x| x <= 100_000).sum()
}

pub fn part2(inp: &HashMap<Vec<&[u8]>, u32>) -> u32 {
    let (capacity, want) = (70000000, 30000000);
    let size = inp.values().max().unwrap_or(&0);
    *inp.values().filter(|&&x| x >= want - (capacity - size)).min().unwrap_or(&0)
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day07.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
