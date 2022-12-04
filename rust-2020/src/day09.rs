use itertools::Itertools;
use itertools::MinMaxResult::MinMax;

pub fn read(contents: &str) -> Vec<i64> {
    contents
        .lines()
        .map(|line| line.parse::<i64>().unwrap())
        .collect::<Vec<_>>()
}

pub fn part1(data: &[i64]) -> i64 {
    let window_size = 25;
    *data[window_size..]
        .iter()
        .zip(data.windows(window_size))
        .find(|(&want, have)| !(*have).iter().any(|h| have.contains(&(want - h))))
        .unwrap()
        .0
}

pub fn part2(data: &[i64]) -> i64 {
    let want = part1(data);
    let mut left = 0;
    let mut subseq_sum = 0;
    for (right, n) in data.iter().enumerate() {
        while subseq_sum > want && left < right {
            subseq_sum -= data[left];
            left += 1;
        }
        if subseq_sum == want {
            if let MinMax(&min, &max) = &data[left..right].iter().minmax() {
                return min + max;
            }
        }
        subseq_sum += n;
    }
    unreachable!()
}
pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day09.input"));
    let data = read(contents);
    let p1 = part1(&data).to_string();
    let p2 = part2(&data).to_string();
    (p1, p2)
}
