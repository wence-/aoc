use regex::Regex;
use std::collections::HashMap;
use std::collections::HashSet;
use std::fs;
use std::path::PathBuf;

type Graph<'a> = HashMap<&'a str, Vec<(&'a str, usize)>>;
type IGraph<'a> = HashMap<&'a str, HashSet<&'a str>>;

fn read(lines: &str) -> (Graph, IGraph) {
    let mut graph = Graph::new();
    let mut invgraph = IGraph::new();

    let pat = Regex::new(r"(\d+) (.+?) bags?[,.]").unwrap();
    for line in lines.trim().split("\n") {
        match line.split(" bags contain ").collect::<Vec<_>>().as_slice() {
            &[source, targets] => {
                for cap in pat.captures_iter(targets) {
                    let target = cap.get(2).unwrap().as_str();
                    let n = cap.get(1).unwrap().as_str().parse().unwrap();
                    graph
                        .entry(source)
                        .or_insert_with(Vec::new)
                        .push((target, n));
                    invgraph
                        .entry(target)
                        .or_insert_with(HashSet::new)
                        .insert(source);
                }
            }
            _ => panic!("Didn't parse line"),
        }
    }
    return (graph, invgraph);
}

fn part1(data: &IGraph) -> usize {
    let mut lifo = vec!["shiny gold"];
    let mut seen = HashSet::<&str>::new();
    while let Some(top) = lifo.pop() {
        match data.get(top) {
            Some(t) => {
                for &c in t {
                    seen.insert(c);
                    lifo.push(c);
                }
            }
            None => (),
        }
    }
    return seen.len();
}

fn part2(data: &Graph) -> usize {
    let mut n: usize = 0;
    let mut lifo = vec![("shiny gold", 1)];
    while let Some((top, b)) = lifo.pop() {
        n += b;
        match data.get(top) {
            Some(t) => {
                for &(k, w) in t {
                    lifo.push((k, w * b));
                }
            }
            None => (),
        }
    }
    return n - 1;
}

pub fn run() -> (usize, usize) {
    let mut d = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    d.push("inputs/day07.input");
    let contents = fs::read_to_string(d).expect("ARGH, didn't read");
    let (graph, invgraph) = read(contents.as_str());
    let p1 = part1(&invgraph);
    let p2 = part2(&graph);
    return (p1, p2);
}
