type Integer = usize;

pub fn read(inp: &str) -> [Integer; 7] {
    let mut v = [Integer::default(); 7];
    for word in inp.as_bytes().split(|&b| b == b',') {
        v[(word[0] - b'0') as usize] += 1;
    }
    v
}

#[inline]
fn solve<const N: usize>(inp: &[Integer]) -> Integer {
    let mut v = inp.to_owned();
    let mut e = [Integer::default(); 3];
    for i in 0..N {
        v[(i + 6) % 7] += e[(i % 3)];
        e[(i % 3)] = v[i % 7];
    }
    v.into_iter().sum()
}

pub fn part1(inp: &[Integer]) -> Integer {
    solve::<80>(inp)
}

pub fn part2(inp: &[Integer]) -> Integer {
    solve::<256>(inp)
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day06.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
