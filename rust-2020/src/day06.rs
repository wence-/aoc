pub fn read(contents: &str) -> (u32, u32) {
    let mut a = 0_u32;
    let mut b = 0_u32;
    for group in contents.trim().split("\n\n") {
        a += group
            .bytes()
            .filter(|&c| c != b'\n')
            .fold(0_u32, |acc, choice| acc | 1 << (choice - b'a'))
            .count_ones();
        b += group
            .split('\n')
            .map(|person| {
                person
                    .bytes()
                    .fold(0_u32, |acc, choice| acc | 1 << (choice - b'a'))
            })
            .fold(std::u32::MAX, |acc, one| acc & one)
            .count_ones();
    }
    return (a, b);
}

pub fn part1(data: &(u32, u32)) -> u32 {
    data.0
}
pub fn part2(data: &(u32, u32)) -> u32 {
    data.1
}
pub fn run() -> (u32, u32) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day06.input"));
    return read(contents);
}
