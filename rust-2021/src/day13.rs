use itertools::Itertools;

type I = usize;
type Input<'a> = (Vec<(u16, u16)>, Vec<(bool, u16)>);

pub fn read(inp: &str) -> Input {
    let (coords, folds) = inp.split_once("\n\n").unwrap();
    let c = coords
        .split('\n')
        .map(|line| {
            let (a, b) = line.split_once(',').unwrap();
            (a.parse::<u16>().unwrap(), b.parse::<u16>().unwrap())
        })
        .collect();
    let f = folds
        .split('\n')
        .map(|line| {
            let y = line.chars().nth(11) == Some('y');
            let n = line[13..].parse::<_>().unwrap();
            (y, n)
        })
        .collect();
    (c, f)
}

pub fn part1(inp: &Input) -> I {
    let (coords, folds) = inp;
    let mut coords = coords.to_owned();
    let &(comp, n) = folds.iter().next().unwrap();

    for mut p in coords.iter_mut() {
        if comp {
            if p.1 > n {
                p.1 = 2 * n - p.1;
            }
        } else if p.0 > n {
            p.0 = 2 * n - p.0;
        }
    }
    coords.sort_unstable();
    coords
        .iter()
        .fold(((u16::MAX, u16::MAX), 0), |(prev, sum), &x| {
            (x, sum + (x != prev) as usize)
        })
        .1
}

#[inline]
fn decode(c: &u32) -> char {
    // Bit location is lexicographic top left to bottom
    // right.
    // 0123
    // 5678
    // 9012
    // 3456
    // 7890
    // 1234
    match c {
        0b1001_1001_1111_1001_1001_0110 => 'A',
        0b0111_1001_1001_0111_1001_0111 => 'B',
        0b0110_1001_0001_0001_1001_0110 => 'C',
        0b1111_0001_0001_0111_0001_1111 => 'E',
        0b0001_0001_0001_0111_0001_1111 => 'F',
        0b1110_1001_1101_0001_1001_0110 => 'G',
        0b1001_1001_1001_1111_1001_1001 => 'H',
        0b1110_0100_0100_0100_0100_1110 => 'I',
        0b0110_1001_1000_1000_1000_1100 => 'J',
        0b1001_0101_0101_0011_0101_1001 => 'K',
        0b1111_0001_0001_0001_0001_0001 => 'L',
        0b0110_1001_1001_1001_1001_0110 => 'O',
        0b0001_0001_0111_1001_1001_0111 => 'P',
        0b1001_0101_0111_1001_1001_0111 => 'R',
        0b0111_1000_0110_0001_0001_1110 => 'S',
        0b0110_1001_1001_1001_1001_1001 => 'U',
        0b0100_0100_0100_1010_0001_0001 => 'Y',
        0b1111_0001_0010_0100_1000_1111 => 'Z',
        _ => {
            println!("Couldn't decode 0b{:032b}", c);
            '_'
        }
    }
}

pub fn part2(inp: &Input) -> String {
    let (coords, folds) = inp;
    let mut chars = [0u32; 8];
    for &p in coords.iter() {
        let mut x = p.0;
        let mut y = p.1;
        for &(comp, n) in folds.iter() {
            if comp {
                if y > n {
                    y = 2 * n - y;
                }
            } else if x > n {
                x = 2 * n - x;
            }
        }
        let i = x / 5;
        chars[i as usize] |= 1 << (y * 4 + x - 5 * i);
    }

    chars.iter().map(decode).join("")
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day13.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data);
    (a, b)
}
