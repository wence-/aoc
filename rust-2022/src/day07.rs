use std::iter::Peekable;

pub fn read(inp: &[u8]) -> (Vec<u32>, u32) {
    let mut v = Vec::with_capacity(512);
    let it = &inp[12..];
    let size = traverse(&mut it.split(|&c| c == b'\n').peekable(), &mut v);
    (v, size)
}

fn traverse<'a>(lines: &mut Peekable<impl Iterator<Item = &'a [u8]>>, out: &mut Vec<u32>) -> u32 {
    let mut size = 0;
    while let Some(&line) = lines.peek() {
        match &line[0] {
            b'$' => break,
            b'd' => (),
            _ => {
                size += line
                    .iter()
                    .take_while(|&&c| c != b' ')
                    .fold(0u32, |acc, &c| acc * 10 + (c - b'0') as u32)
            }
        }
        lines.next();
    }
    while let Some(&line) = lines.peek() {
        if let Some(b'.') = line.get(5) {
            break;
        }
        // Skip $ cd foo
        lines.next();
        // Skip $ ls
        lines.next();
        // Read sub-size
        size += traverse(lines, out);
    }
    lines.next();
    out.push(size);
    size
}

pub fn part1(inp: &(Vec<u32>, u32)) -> u32 {
    inp.0.iter().filter(|&&x| x <= 100_000).sum()
}

pub fn part2(inp: &(Vec<u32>, u32)) -> u32 {
    let (capacity, want) = (70000000, 30000000);
    *inp.0.iter().filter(|&&x| x >= want - (capacity - inp.1)).min().unwrap_or(&0)
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day07.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
