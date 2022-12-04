pub fn read(contents: &str) -> Vec<&str> {
    contents.lines().collect()
}

fn trees(grid: &[&str], row: usize, col: usize) -> usize {
    let ncol = grid[0].len();
    grid.iter()
        .step_by(col)
        .enumerate()
        .filter(|(i, line)| line.chars().nth(i * row % ncol).unwrap() == '#')
        .count()
}

pub fn part1(data: &[&str]) -> usize {
    trees(data, 3, 1)
}

pub fn part2(data: &[&str]) -> usize {
    let skips = vec![(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];
    skips
        .iter()
        .map(|(row, col)| trees(data, *row, *col))
        .product()
}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day03.input"));
    let data = read(contents);
    let p1 = part1(&data).to_string();
    let p2 = part2(&data).to_string();
    (p1, p2)
}
