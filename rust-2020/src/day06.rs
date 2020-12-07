use std::fs;
use std::path::PathBuf;

fn read() -> (Vec<u32>, Vec<u32>) {
    let mut d = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    d.push("inputs/day06.input");
    let contents = fs::read_to_string(d).expect("ARGH, didn't read");
    let mut veca = Vec::<u32>::new();
    let mut vecb = Vec::<u32>::new();
    for group in contents.trim().split("\n\n") {
        let p1 = group
            .bytes()
            .filter(|&c| c != b'\n')
            .fold(0_u32, |acc, choice| acc | 1 << (choice - b'a'))
            .count_ones();
        let p2 = group
            .split('\n')
            .map(|person| {
                person
                    .bytes()
                    .fold(0_u32, |acc, choice| acc | 1 << (choice - b'a'))
            })
            .fold(std::u32::MAX, |acc, one| acc & one)
            .count_ones();
        veca.push(p1);
        vecb.push(p2);
    }
    return (veca, vecb);
}

fn part1(data: &Vec<u32>) -> u32 {
    return data.iter().sum::<u32>();
}

fn part2(data: &Vec<u32>) -> u32 {
    return data.iter().sum::<u32>();
}

pub fn run() -> (u32, u32) {
    let (d1, d2) = read();
    let p1 = part1(&d1);
    let p2 = part2(&d2);
    return (p1, p2);
}
