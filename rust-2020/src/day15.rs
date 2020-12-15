fn read() -> Vec<u8> {
    vec![7, 12, 1, 0, 16, 2]
}

fn solve(data: &Vec<u8>, max_turn: u32) -> u32 {
    let mut spoken = vec![0u32; max_turn as usize];
    let mut last: u32 = 0;
    for (i, &n) in data.iter().enumerate() {
        spoken[n as usize] = i as u32 + 1;
        last = n.into();
    }
    for i in (data.len() as u32)..max_turn {
        let cur = spoken[last as usize];
        spoken[last as usize] = i;
        last = if cur == 0 { 0 } else { i - cur };
    }
    return last;
}

pub fn run() -> (u32, u32) {
    let data = read();
    return (solve(&data, 2020), solve(&data, 30_000_000));
}
