use itertools::Itertools;
use std::collections::HashMap;
use std::ops::Index;
use std::str::from_utf8;

type T = u16;
type I = u32;

#[derive(Debug)]
pub struct Graph {
    nupper: T,
    start: T,
    end: T,
    nedges: [usize; 16],
    edges: [T; 64],
}

impl Index<T> for Graph {
    type Output = [T];
    fn index<'a>(&'_ self, i: T) -> &'_ Self::Output {
        &self.edges[self.nedges[i as usize]..self.nedges[i as usize + 1]]
    }
}

pub fn read(inp: &str) -> Graph {
    let mut nodes = HashMap::new();
    for line in inp.trim().split('\n') {
        let (a, b) = line.split('-').next_tuple().unwrap();
        if b != "start" {
            nodes.entry(a).or_insert_with(Vec::new).push(b);
        }
        if a != "start" {
            nodes.entry(b).or_insert_with(Vec::new).push(a);
        }
    }
    let mut start = 0;
    let mut end = 0;
    let mut nupper = 0;
    let mut namemap: HashMap<&str, T> = HashMap::new();
    let mut nedges = [0usize; 16];
    for (i, (&k, v)) in nodes.iter().sorted_by_key(|x| x.0).enumerate() {
        if k == "end" {
            end = i;
        } else if k == "start" {
            start = i;
        }
        namemap.insert(k, i as T);
        if k.bytes().all(|c| c < b'a') {
            nupper = i;
        }
        nedges[i + 1] = nedges[i] + v.len();
    }
    let mut edges = [T::default(); 64];

    for (k, v) in nodes.iter() {
        let i = namemap[k];
        for (j, e) in v.iter().sorted().enumerate() {
            edges[nedges[i as usize] + j] = namemap[e];
        }
    }
    Graph {
        nupper: nupper as T,
        start: start as T,
        end: end as T,
        nedges,
        edges,
    }
}

type Cache = HashMap<u32, I>;

#[inline]
fn index(head: T, seen: u32, twice: bool) -> u32 {
    let t = if twice { 1 << 31 } else { 0 };
    seen << 12 | (head as u32) | t
}

fn recurse(head: T, nodes: &Graph, seen: u32, twice: bool, cache: &mut Cache) -> I {
    if head == nodes.end {
        return 1;
    }
    let key = index(head, seen, twice);
    if let Some(&v) = cache.get(&key) {
        return v;
    }
    let mut s = 0;
    for &c in nodes[head].iter() {
        let seenp = (seen & (2 << c)) != 0;
        if twice && seenp {
            continue;
        }
        if c <= nodes.nupper {
            s += recurse(c, nodes, seen, twice, cache);
        } else {
            s += recurse(c, nodes, seen | (2 << c), twice || seenp, cache);
        }
    }
    cache.insert(key, s);
    s
}

pub fn part1(inp: &Graph) -> I {
    recurse(inp.start, inp, 0u32, true, &mut Cache::new())
}

pub fn part2(inp: &Graph) -> I {
    recurse(inp.start, inp, 0u32, false, &mut Cache::new())
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day12.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
