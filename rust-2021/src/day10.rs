type I = usize;
type Input = (I, I);

pub fn read(inp: &str) -> Input {
    let mut v1 = 0;
    let mut v2 = Vec::with_capacity(100);
    for line in inp.trim().split('\n') {
        let (c1, c2) = check(line);
        if c1 != 0 {
            v1 += c1;
        } else {
            v2.push(c2)
        }
    }
    let n = v2.len() >> 1;
    (v1, *v2.select_nth_unstable(n).1)
}

#[inline]
fn check(line: &str) -> (I, I) {
    let mut lifo = Vec::with_capacity(20);
    for c in line.chars() {
        match c {
            '(' | '{' | '[' | '<' => lifo.push(c),
            ')' => {
                if lifo.pop() != Some('(') {
                    return (3, 0);
                }
            }
            ']' => {
                if lifo.pop() != Some('[') {
                    return (57, 0);
                }
            }
            '}' => {
                if lifo.pop() != Some('{') {
                    return (1197, 0);
                }
            }
            '>' => {
                if lifo.pop() != Some('<') {
                    return (25137, 0);
                }
            }
            _ => {
                unreachable!()
            }
        }
    }
    let mut s = 0;
    for &c in lifo.iter().rev() {
        s = s * 5
            + match c {
                '(' => 1,
                '[' => 2,
                '{' => 3,
                '<' => 4,
                _ => unreachable!(),
            }
    }
    (0, s)
}

pub fn part1(inp: &Input) -> I {
    inp.0
}

pub fn part2(inp: &Input) -> I {
    inp.1
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day10.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
