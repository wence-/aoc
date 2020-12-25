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
        .filter(|(&want, have)| !(*have).iter().any(|h| have.contains(&(want - h))))
        .next()
        .unwrap()
        .0
}

pub fn part2(data: &[i64]) -> i64 {
    let want = part1(&data);
    let mut left = 0;
    let mut subseq_sum = 0;
    for (right, n) in data.iter().enumerate() {
        while subseq_sum > want && left < right {
            subseq_sum -= data[left];
            left += 1;
        }
        if subseq_sum == want {
            match &data[left..right].iter().minmax() {
                MinMax(&min, &max) => {
                    return min + max;
                }
                _ => {}
            }
        }
        subseq_sum += n;
    }
    unreachable!()
}
pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day09.input"));
    let data = read(&contents);
    let p1 = format!("{}", part1(&data));
    let p2 = format!("{}", part2(&data));
    return (p1, p2);
}
