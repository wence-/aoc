use std::collections::VecDeque;

const W: usize = 66;
const H: usize = 41;

pub fn read(inp: &[u8]) -> (Vec<u8>, usize, usize) {
    let mut source = 0;
    let mut target = 0;
    let mut i = 0;
    let v: Vec<_> = inp
        .into_iter()
        .filter_map(|&c| {
            if c != b'\n' {
                i += 1;
                match c {
                    b'S' => {
                        source = i - 1;
                        Some(b'a')
                    }
                    b'E' => {
                        target = i - 1;
                        Some(b'z')
                    }
                    _ => Some(c),
                }
            } else {
                None
            }
        })
        .collect();
    (v, source, target)
}

fn solve(grid: &[u8], source: usize, target: usize, done: fn(usize, usize, u8) -> bool) -> u32 {
    let mut seen = [false; W * H];
    let mut q = VecDeque::from([(source, 0)]);
    while let Some((node, distance)) = q.pop_front() {
        if done(node, target, grid[node]) {
            return distance;
        }
        let (x, y) = (node % W, node / W);
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
            if !((x == 0 && dx == -1) || (y == 0 && dy == -1)) {
                let (nx, ny) = ((x as i32 + dx) as usize, (y as i32 + dy) as usize);
                if ny == H || nx == W {
                    continue;
                }
                let neighbour = ny * W + nx;
                if !seen[neighbour] && grid[node] - 1 <= grid[neighbour] {
                    seen[neighbour] = true;
                    q.push_back((neighbour, distance + 1));
                }
            }
        }
    }
    unreachable!();
}

pub fn part1(inp: &(Vec<u8>, usize, usize)) -> u32 {
    solve(&inp.0, inp.2, inp.1, |node, target, _| node == target)
}

pub fn part2(inp: &(Vec<u8>, usize, usize)) -> u32 {
    solve(&inp.0, inp.2, inp.1, |_, _, val| val == b'a')
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day12.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
