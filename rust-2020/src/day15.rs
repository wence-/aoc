pub fn read(contents: &str) -> Vec<u8> {
    contents
        .trim()
        .split(",")
        .map(|n| n.parse::<u8>().unwrap())
        .collect::<Vec<_>>()
}

fn solve(data: &Vec<u8>, max_turn: u32) -> u32 {
    let mut spoken = vec![0u32; max_turn as usize];
    let mut last: u32 = 0;
    for (i, &n) in data.iter().enumerate() {
        spoken[n as usize] = i as u32 + 1;
        last = n as u32;
    }
    for i in (data.len() as u32)..max_turn {
        let cur = spoken[last as usize];
        spoken[last as usize] = i;
        last = if cur == 0 { 0 } else { i - cur };
    }
    return last;
}

pub fn part1(data: &Vec<u8>) -> u32 {
    solve(&data, 2020)
}

pub fn part2(data: &Vec<u8>) -> u32 {
    solve(&data, 30_000_000)
}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day01.input"));
    let data = read(&contents);
    let p1 = format!("{}", part1(&data));
    let p2 = format!("{}", part2(&data));
    return (p1, p2);
}
