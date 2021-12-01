pub fn read(_lines: &str) -> () {}

pub fn part1(data: ()) -> usize {
    return 0;
}

pub fn part2(data: ()) -> usize {
    return 0;
}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day01.input")); // FIXME
    let data = read(&contents);
    let p1 = format!("{}", part1(*&data));
    let p2 = format!("{}", part2(*&data));
    return (p1, p2);
}
