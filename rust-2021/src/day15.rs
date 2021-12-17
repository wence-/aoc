use std::{cmp::Reverse, collections::BinaryHeap};

const N: usize = 100;

pub fn read(input: &str) -> Vec<u8> {
    input
        .split('\n')
        .flat_map(|l| l.bytes().map(|c| c - b'0'))
        .collect()
}

fn dijkstra<const N: usize>(grid: &[u8]) -> u32 {
    let mut seen = vec![false; N * N];
    let mut pq = BinaryHeap::from([(Reverse(0), 0)]);
    while let Some((Reverse(risk), ix)) = pq.pop() {
        if ix == N * N - 1 {
            return risk;
        }
        let i = ix / N;
        let j = ix % N;
        [
            [i.wrapping_sub(1), j],
            [i + 1, j],
            [i, j.wrapping_sub(1)],
            [i, j + 1],
        ]
        .into_iter()
        .filter_map(|[i, j]| {
            if i < N && j < N {
                Some(i * N + j)
            } else {
                None
            }
        })
        .for_each(|ix| {
            if !seen[ix] {
                pq.push((Reverse(risk + grid[ix] as u32), ix));
                seen[ix] = true;
            }
        })
    }
    0
}

pub fn part1(input: &[u8]) -> u32 {
    dijkstra::<N>(input)
}

pub fn part2(input: &[u8]) -> u32 {
    const NS: usize = N * SCALE;
    const SCALE: usize = 5;
    let mut large = [0; SCALE * N * SCALE * N];
    (0..N * SCALE)
        .flat_map(|i| (0..N * SCALE).map(move |j| (i, j, i / N + j / N)))
        .for_each(|(i, j, k)| {
            large[i * N * SCALE + j] = ((input[(i % N) * N + j % N] as usize + k - 1) % 9) as u8 + 1
        });
    dijkstra::<NS>(&large)
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day15.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
