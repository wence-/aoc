pub enum Op {
    Acc(i32),
    Jmp(i32),
    Nop(i32),
}

pub fn read(lines: &str) -> Vec<Op> {
    lines
        .trim()
        .split("\n")
        .map(|line| {
            let n = line[4..].parse::<i32>().unwrap();
            match &line[0..3] {
                "acc" => Op::Acc(n),
                "jmp" => Op::Jmp(n),
                "nop" => Op::Nop(n),
                _ => panic!("Didn't parse line {}", line),
            }
        })
        .collect()
}

pub fn part1(data: &Vec<Op>) -> i32 {
    let mut seen = vec![];
    let (mut acc, mut ip) = (0, 0);
    while !seen.contains(&ip) {
        seen.push(ip);
        match data[ip as usize] {
            Op::Acc(n) => acc += n,
            Op::Jmp(n) => ip += n - 1,
            _ => {}
        }
        ip += 1;
    }
    return acc;
}

pub fn part2(data: &Vec<Op>) -> i32 {
    let ninsn = data.len();
    for i in 0..ninsn {
        let mut seen = Vec::new();
        seen.resize(ninsn, false);
        let (mut acc, mut ip) = (0, 0);
        while !seen[ip as usize] {
            seen[ip as usize] = true;
            match (&data[ip as usize], (ip as usize) == i) {
                (Op::Acc(n), _) => acc += n,
                (Op::Jmp(n), false) | (Op::Nop(n), true) => ip += n - 1,
                (Op::Nop(_), false) | (Op::Jmp(_), true) => {}
            }
            ip += 1;
            if ip as usize == ninsn {
                return acc;
            }
        }
    }
    panic!()
}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day08.input"));
    let data = read(&contents);
    let p1 = format!("{}", part1(&data));
    let p2 = format!("{}", part2(&data));
    return (p1, p2);
}
