use std::collections::HashMap;

type GraphNode = (u8, Vec<u8>);
const N: usize = 51;
const P: usize = 15;
type Paths = [[(u8, u8); P]; N];

fn allpaths(graph: &[GraphNode]) -> Paths {
    let mut vv = [[99u8; N]; N];
    for (i, (_, conn)) in graph.iter().enumerate() {
        for &c in conn.iter() {
            vv[i][c as usize] = 1;
        }
    }
    for k in 0..N {
        for i in 0..N {
            for j in 0..N {
                vv[i][j] = vv[i][j].min(vv[i][k] + vv[k][j]);
            }
        }
    }
    let mut ret = [[(0u8, 0u8); P]; N];
    for (i, v) in vv.iter().enumerate() {
        for (j, r) in v
            .iter()
            .enumerate()
            .filter_map(|(node, time)| {
                (graph[node].0 > 0).then_some((node as u8, *time + 1))
            })
            .enumerate()
        {
            ret[i][j] = r;
        }
    }
    ret
}

#[inline]
fn best_remaining(enabled: u64, rates: &[u16]) -> u16 {
    (0..N)
        .filter_map(|i| (enabled & (1 << i) == 0).then_some(rates[i]))
        .max()
        .unwrap_or(0)
}

pub fn read(inp: &[u8]) -> (Vec<GraphNode>, Paths) {
    let mapping: HashMap<&[u8], u8> = inp
        .split(|&c| c == b'\n')
        .enumerate()
        .map(|(i, line)| (&line[6..8], i as u8))
        .collect();
    let mut graph = Vec::with_capacity(64);
    for line in inp.split(|&c| c == b'\n') {
        let rate = if line[24] == b';' {
            line[23] - b'0'
        } else {
            10 * (line[23] - b'0') + (line[24] - b'0')
        };
        let offset = if line[47] == b' ' { 48 } else { 49 };
        let edges = line[offset..]
            .split(|&c| c == b',')
            .map(|entry| *mapping.get(&entry[(entry[0] == b' ') as usize..]).unwrap())
            .collect::<Vec<_>>();
        graph.push((rate, edges))
    }
    let paths = allpaths(&graph);
    (graph, paths)
}

fn search(
    node: u8,
    best: u16,
    current: u16,
    time_left: u8,
    enabled: u64,
    paths: &Paths,
    rates: &[u16],
) -> (u16, u16) {
    let mut score = current;
    let mut best = best;
    for &(dst, cur_time) in paths[node as usize].iter() {
        if cur_time > time_left || ((1 << dst) & enabled) != 0 {
            continue;
        }
        let new_time = (time_left - cur_time) as u16;
        let new_score = current + new_time * rates[dst as usize];
        let optimistic = best_remaining(enabled | (1 << dst), rates);
        if new_score + (new_time * new_time * optimistic) / 15 < best {
            continue;
        }
        let x = search(
            dst,
            best,
            new_score,
            new_time as u8,
            enabled | (1 << dst),
            paths,
            rates,
        );
        best = x.1;
        score = score.max(x.0);
    }
    (score, best.max(score))
}

fn search2(
    me: u8,
    you: u8,
    best: u16,
    current: u16,
    time_left: u16,
    enabled: u64,
    budget: u16,
    paths: &Paths,
    rates: &[u16],
) -> (u16, u16) {
    let mut score = current;
    let mut best = best;
    for &(dst, cur_time) in paths[me as usize].iter() {
        let cur_time = cur_time as u16;
        if cur_time > time_left || ((1 << dst) & enabled) != 0 {
            continue;
        }
        let (new_me, new_you, new_time_left, new_budget);
        if budget < cur_time {
            (new_me, new_you) = (you, dst);
            (new_time_left, new_budget) = (time_left - budget, cur_time - budget);
        } else {
            (new_me, new_you) = (dst, you);
            (new_time_left, new_budget) = (time_left - cur_time, budget - cur_time);
        }
        let new = current + (time_left - cur_time) * rates[dst as usize];
        if new + (89 * time_left).saturating_sub(110 * cur_time + 65 * budget) < best {
            continue;
        }

        let x = search2(
            new_me,
            new_you,
            best,
            new,
            new_time_left,
            enabled | (1 << dst),
            new_budget,
            paths,
            rates,
        );
        best = x.1;
        score = score.max(x.0);
    }
    (score, best.max(score))
}

pub fn part1(inp: &(Vec<GraphNode>, Paths)) -> u16 {
    let rates: Vec<_> = inp.0.iter().map(|x| x.0 as u16).collect();
    search(16, 0, 0, 30, 0, &inp.1, &rates).0
}

pub fn part2(inp: &(Vec<GraphNode>, Paths)) -> u16 {
    let rates: Vec<_> = inp.0.iter().map(|x| x.0 as u16).collect();
    search2(16, 16, 0, 0, 26, 0, 0, &inp.1, &rates).0
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day16.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
