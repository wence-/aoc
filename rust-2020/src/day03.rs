fn read(contents: &str) -> Vec<&str> {
    return contents.lines().collect();
}

fn trees(grid: &Vec<&str>, row: usize, col: usize) -> usize {
    let ncol = grid[0].len();
    return grid
        .iter()
        .step_by(col)
        .enumerate()
        .filter(|(i, line)| line.chars().nth(i * row % ncol).unwrap() == '#')
        .count();
}

fn part1(data: &Vec<&str>) -> usize {
    return trees(data, 3, 1);
}

fn part2(data: &Vec<&str>) -> usize {
    let skips = vec![(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];
    return skips
        .iter()
        .map(|(row, col)| trees(data, *row, *col))
        .product();
}

pub fn run() -> (usize, usize) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day03.input"));
    let data = read(contents);
    return (part1(&data), part2(&data));
}
