const MODULUS: usize = 20201227usize;

pub fn read(lines: &str) -> Vec<usize> {
    lines
        .lines()
        .map(|line| line.parse::<usize>().unwrap())
        .collect()
}

pub fn part1(data: &[usize]) -> usize {
    let mut e = 0;
    let mut n = 1;
    if let [cardpub, doorpub] = *data {
        while n != doorpub {
            e += 1;
            n = 7 * n % MODULUS;
        }
        return mod_exp::mod_exp(cardpub, e, MODULUS);
    }
    unreachable!()
}

pub fn part2(_data: &[usize]) {}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day25.input"));
    let data = read(&contents);
    let p1 = format!("{}", part1(&data));
    let p2 = "No part 2".to_string();
    (p1, p2)
}
