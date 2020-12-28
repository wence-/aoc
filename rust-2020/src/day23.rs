use itertools::iterate;
use std::char;
use std::iter;
use std::ops::{Index, IndexMut};

pub fn read(lines: &str) -> Vec<usize> {
    lines
        .trim()
        .chars()
        .map(|c| c.to_digit(10).unwrap() as usize)
        .collect()
}

#[derive(Debug)]
struct Link {
    link: Vec<usize>,
    max: usize,
    head: usize,
}

impl Index<usize> for Link {
    type Output = usize;
    fn index(&self, i: usize) -> &Self::Output {
        &self.link[i]
    }
}

impl IndexMut<usize> for Link {
    fn index_mut(&mut self, i: usize) -> &mut Self::Output {
        &mut self.link[i]
    }
}

impl Link {
    fn new(cards: &[usize]) -> Link {
        let mut link = vec![0; cards.len() + 1];
        for (&a, b) in cards
            .iter()
            .zip(cards[1..].iter().copied().chain(iter::once(cards[0])))
        {
            link[a] = b;
        }
        let head = link[*cards.last().unwrap()];
        Link {
            link,
            max: *cards.iter().max().unwrap(),
            head,
        }
    }

    fn run(&mut self, n: usize) {
        let mut i = 0;
        while i < n {
            let cur = self.head;
            let a = self[cur];
            let b = self[a];
            let c = self[b];
            self[cur] = self[c];
            let mut dest = cur - 1;
            loop {
                if dest == 0 {
                    dest = self.max;
                }
                if dest != a && dest != b && dest != c {
                    break;
                }
                dest -= 1;
            }
            self[c] = self[dest];
            self[dest] = a;
            self.head = self[cur];
            i += 1;
        }
    }

    fn iter<'a>(&'a self) -> impl Iterator<Item = usize> + 'a {
        iterate(self[1], move |&i| self[i])
    }
}

pub fn part1(data: &[usize]) -> String {
    let mut cards = Link::new(&data);
    cards.run(100);
    cards
        .iter()
        .take_while(|&x| x != 1)
        .map(|x| char::from_digit(x as u32, 10).unwrap())
        .collect::<String>()
}

pub fn part2(data: &[usize]) -> usize {
    let mut cards = Link::new(
        &data
            .iter()
            .copied()
            .chain(10..=1_000_000)
            .collect::<Vec<_>>(),
    );
    cards.run(10_000_000);
    cards.iter().take(2).product::<usize>()
}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day23.input"));
    let data = read(&contents);
    let p1 = format!("{}", part1(&data));
    let p2 = format!("{}", part2(&data));
    return (p1, p2);
}
