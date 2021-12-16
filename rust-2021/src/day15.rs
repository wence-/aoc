use std::{cmp::Reverse, collections::BinaryHeap};

const N: usize = 100;

fn read<const N: usize>(input: &str) -> Result<[[u8; N]; N], ()> {
    input
        .lines()
        .map(|l| {
            l.bytes()
                .map(|c| c - b'0')
                .collect::<Vec<_>>()
                .try_into()
                .map_err(|_| ())
        })
        .collect::<Result<Vec<_>, ()>>()?
        .try_into()
        .map_err(|_| ())
}

fn dijkstra<const N: usize>(grid: &Result<[[u8; N]; N], ()>) -> u32 {
    let mut m = grid.unwrap().to_owned();
    let mut pq = BinaryHeap::from([(Reverse(0), (0, 0))]);
    while let Some((Reverse(risk), (i, j))) = pq.pop() {
        if (i, j) == (N - 1, N - 1) {
            return risk;
        }
        [(i.wrapping_sub(1), j), (i + 1, j), (i, j.wrapping_sub(1)), (i, j + 1)]
            .into_iter()
            .filter(|&(i, j)| i < N && j < N)
            .for_each(|(i, j)| {
                if m[i][j] > 0 {
                    pq.push((Reverse(risk + m[i][j] as u32), (i, j)));
                    m[i][j] = 0;
                }
            })
    }
    0
}

fn part1(input: &Result<[[u8; N]; N], ()>) -> u32 {
    dijkstra::<N>(input)
}

fn part2(input: &Result<[[u8; N]; N], ()>) -> u32 {
    const SCALE: usize = 5;
    const NS: usize = 500;
    let grid = input.unwrap();
    let mut large = [[0; SCALE * N]; SCALE * N];
    (0..N * SCALE)
        .flat_map(|i| (0..N * SCALE).map(move |j| (i, j, i / N + j / N)))
        .for_each(|(i, j, k)| large[i][j] = ((grid[i % N][j % N] as usize + k - 1) % 9) as u8 + 1);
    dijkstra::<NS>(&Ok(large))
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day15.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
