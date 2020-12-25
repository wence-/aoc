use itertools::Itertools;
use ndarray::Array2;

type State = i8;

const EMPTY: i8 = 0;
const FULL: i8 = 1;
const FLOOR: i8 = 2;

type Grid = Array2<State>;

pub fn read(contents: &str) -> Grid {
    let lines = contents.lines().collect::<Vec<_>>();
    let nx = lines[0].len();
    let ny = lines.len();
    let mut grid = Array2::<State>::default((nx, ny));
    for (i, &line) in lines.iter().enumerate() {
        for (j, c) in line.chars().enumerate() {
            let s = match c {
                '#' => FULL,
                '.' => FLOOR,
                'L' => EMPTY,
                _ => panic!("Unexpected char {}", c),
            };
            grid[[j, i]] = s;
        }
    }
    return grid;
}

trait Search {
    fn search(&self, grid: &Grid, i: usize, j: usize, k: isize, l: isize) -> usize;
}

struct Part1 {}

impl Search for Part1 {
    #[inline]
    fn search(&self, current: &Grid, i: usize, j: usize, k: isize, l: isize) -> usize {
        if k == l && k == 0 {
            return 0;
        }
        let (nx, ny) = current.dim();
        if (0..nx as isize).contains(&(i as isize + k))
            && (0..ny as isize).contains(&(j as isize + l))
        {
            match current[[(i as isize + k) as usize, (j as isize + l) as usize]] {
                FULL => {
                    return 1;
                }
                EMPTY => {
                    return 0;
                }
                _ => {}
            }
        }
        return 0;
    }
}

struct Part2 {}
impl Search for Part2 {
    #[inline]
    fn search(&self, current: &Grid, i: usize, j: usize, k: isize, l: isize) -> usize {
        if k == l && k == 0 {
            return 0;
        }
        let (nx, ny) = current.dim();
        let mut m = 1;
        while (0..nx as isize).contains(&(i as isize + k * m))
            && (0..ny as isize).contains(&(j as isize + l * m))
        {
            match current[[(i as isize + k * m) as usize, (j as isize + l * m) as usize]] {
                FULL => {
                    return 1;
                }
                EMPTY => {
                    return 0;
                }
                _ => {}
            }
            m += 1;
        }
        return 0;
    }
}

fn step<T: Search>(current: &Grid, next: &mut Grid, full: usize, x: T) -> () {
    for (nextij, (i, j)) in next.iter_mut().zip(ndarray::indices_of(current)) {
        *nextij = current[[i, j]];
        if current[[i, j]] == FLOOR {
            continue;
        }
        let noc = (-1..=1)
            .cartesian_product(-1..=1)
            .map(|(k, l)| x.search(current, i, j, k, l))
            .sum::<usize>();
        if current[[i, j]] == EMPTY && noc == 0 {
            *nextij = FULL;
        } else if noc >= full {
            *nextij = EMPTY;
        }
    }
}

pub fn part1(data: &Grid) -> usize {
    let mut current = data.clone();
    let mut next = Array2::<State>::default(data.dim());
    while next != current {
        step(&mut current, &mut next, 4, Part1 {});
        std::mem::swap(&mut current, &mut next);
    }
    return current.iter().filter(|c| **c == FULL).count();
}

pub fn part2(data: &Grid) -> usize {
    let mut current = data.clone();
    let mut next = Array2::<State>::default(data.dim());
    while next != current {
        step(&current, &mut next, 5, Part2 {});
        std::mem::swap(&mut current, &mut next);
    }
    return current.iter().filter(|c| **c == FULL).count();
}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day11.input"));
    let data = read(&contents);
    let p1 = format!("{}", part1(&data));
    let p2 = format!("{}", part2(&data));
    return (p1, p2);
}
