pub fn read(inp: &[u8]) -> Vec<[u8; 4]> {
    inp.split(|&c| c == b'\n')
        .map(|line| {
            let mut v = [0u8; 4];
            let mut pos = 0;
            for v_ in &mut v {
                let c0 = line[pos].saturating_sub(b'0' - 1);
                let c1 = line.get(pos + 1).unwrap_or(&0).saturating_sub(b'0' - 1);
                match c1 {
                    0 => {
                        *v_ = c0;
                        pos += 2
                    }
                    _ => {
                        *v_ = (c0 << 4) + c1;
                        pos += 3
                    }
                }
            }
            v
        })
        .collect()
}

#[inline]
fn contains(s1: u8, e1: u8, s2: u8, e2: u8) -> bool {
    s1 <= s2 && e1 >= e2
}

#[inline]
fn overlaps(s1: u8, e1: u8, s2: u8, e2: u8) -> bool {
    s1 <= e2 && s2 <= e1
}

pub fn part1(inp: &[[u8; 4]]) -> u16 {
    inp.iter().fold(0u16, |acc, &v| {
        acc + (contains(v[0], v[1], v[2], v[3]) || contains(v[2], v[3], v[0], v[1])) as u16
    })
}

pub fn part2(inp: &[[u8; 4]]) -> u16 {
    inp.iter().fold(0u16, |acc, &v| {
        acc + overlaps(v[0], v[1], v[2], v[3]) as u16
    })
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day04.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
