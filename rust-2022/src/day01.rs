type I = u32;

pub fn read(inp: &[u8]) -> Vec<I> {
    let mut v = Vec::with_capacity(256);
    let mut val = 0;
    for line in inp.split(|&c| c == b'\n') {
        if line.len() == 0 {
            v.push(val);
            val = 0;
        } else {
            val = val
                + line
                    .iter()
                    .fold(0u32, |acc, &c| acc * 10 + ((c - b'0') as u32));
        }
    }
    v
}

pub fn part1(inp: &[I]) -> I {
    inp.iter().fold(I::MIN, |acc, &i| acc.max(i))
}

#[inline]
fn sort(r: &mut [I]) {
    if r[0] > r[1] {
        r.swap(0, 1)
    }
    if r[0] > r[2] {
        r.swap(0, 2)
    }
    if r[1] > r[2] {
        r.swap(1, 2)
    }
}

pub fn part2(inp: &[I]) -> I {
    const N: usize = 3;
    let mut r = [0; N];
    for &e in inp.iter() {
        if r[0] < e {
            r[0] = e;
            sort(&mut r);
        }
    }
    r.into_iter().sum()
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day01.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
