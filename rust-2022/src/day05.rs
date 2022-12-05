type Moves = Vec<(usize, usize, usize)>;
type Stacks = [Vec<u8>; 9];

pub fn read(inp: &[u8]) -> (Moves, Stacks) {
    const X: Vec<u8> = Vec::new();
    let mut stacks = [X; 9];
    let mut moves = Vec::with_capacity(512);
    for line in inp.split(|&c| c == b'\n') {
        if line.is_empty() {
            continue;
        } else if line[0] == b'[' {
            for (i, &c) in line.iter().skip(1).step_by(4).enumerate() {
                if c != b' ' {
                    stacks[i].push(c);
                }
            }
        } else if line[0] == b'm' {
            let c0 = line[5];
            let c1 = line[6];
            if c1 == b' ' {
                moves.push((
                    (c0 - b'0') as usize,
                    (line[12] - b'1') as usize,
                    (line[17] - b'1') as usize,
                ))
            } else {
                moves.push((
                    ((c0 - b'0') * 10 + (c1 - b'0')) as usize,
                    (line[13] - b'1') as usize,
                    (line[18] - b'1') as usize,
                ))
            }
        }
    }
    for s in &mut stacks {
        s.reverse();
    }
    (moves, stacks)
}

pub fn part1(inp: &(Moves, Stacks)) -> String {
    let (moves, stacks) = inp;
    let mut stacks = stacks.to_owned();
    for &(n, src, dst) in moves.iter() {
        for _ in 0..n {
            let t = stacks[src].pop().unwrap();
            stacks[dst].push(t);
        }
    }
    String::from_utf8(stacks.iter().map(|s| *(s.last().unwrap())).collect()).unwrap()
}

pub fn part2(inp: &(Moves, Stacks)) -> String {
    let (moves, stacks) = inp;
    let mut stacks = stacks.to_owned();
    let mut tmp = [0u8; 64];
    for &(n, src, dst) in moves.iter() {
        for t in tmp.iter_mut().take(n) {
            *t = stacks[src].pop().unwrap();
        }
        for i in (0..n).rev() {
            stacks[dst].push(tmp[i]);
        }
    }
    String::from_utf8(stacks.iter().map(|s| *(s.last().unwrap())).collect()).unwrap()
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day05.input"));
    let data = read(inp);
    let a = part1(&data);
    let b = part2(&data);
    (a, b)
}
