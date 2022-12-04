pub fn read(inp: &str) -> Vec<i16> {
    inp.trim()
        .split('\n')
        .flat_map(|line| {
            line.split(" -> ")
                .flat_map(|word| word.split(',').map(|w| w.parse::<i16>().unwrap()))
        })
        .collect()
}

struct Range {
    b: i16,
    e: i16,
    s: i16,
    c: i16,
}

impl Range {
    fn new(b: i16, e: i16, s: i16) -> Range {
        Range {
            b,
            e: e + s,
            s,
            c: b,
        }
    }
}

impl Iterator for Range {
    type Item = i16;

    fn next(&mut self) -> Option<Self::Item> {
        if self.s == 0 {
            Some(self.b)
        } else if self.c == self.e {
            None
        } else {
            self.c += self.s;
            Some(self.c - self.s)
        }
    }
}

fn solve(inp: &[i16], diag: bool) -> usize {
    let mut xmax: usize = 0;
    let mut ymax: usize = 0;
    for c in inp.chunks_exact(4) {
        xmax = xmax.max(c[0] as usize).max(c[2] as usize);
        ymax = ymax.max(c[1] as usize).max(c[3] as usize);
    }
    xmax += 1;
    ymax += 1;
    let mut m = vec![0i8; xmax * ymax];
    let mut ret = 0;
    for c in inp.chunks_exact(4) {
        let x1 = c[0];
        let y1 = c[1];
        let x2 = c[2];
        let y2 = c[3];
        let dx = (x2 - x1).signum();
        let dy = (y2 - y1).signum();
        for (x, y) in Range::new(x1, x2, dx).zip(Range::new(y1, y2, dy)) {
            if !diag && dx != 0 && dy != 0 {
                continue;
            }
            let mi = &mut m[(x as usize) * ymax + y as usize];
            *mi += 1;
            if *mi == 2 {
                ret += 1;
            }
        }
    }
    ret
}

pub fn part1(inp: &[i16]) -> usize {
    solve(inp, false)
}
pub fn part2(inp: &[i16]) -> usize {
    solve(inp, true)
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day05.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
