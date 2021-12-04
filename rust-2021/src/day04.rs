use itertools::Itertools;

const N: usize = 5;
type Board = Vec<u8>;

pub fn read(inp: &str) -> (Vec<u8>, Vec<Board>) {
    let mut s = inp.trim().split("\n\n");

    let moves = s
        .next()
        .unwrap()
        .trim()
        .split(',')
        .map(|word| word.parse::<u8>().unwrap())
        .collect();

    let boards = s
        .map(|board| {
            board
                .trim()
                .split_ascii_whitespace()
                .map(|word| word.parse::<u8>().unwrap())
                .collect()
        })
        .collect();
    (moves, boards)
}

fn time_to_win(board: &[u8], times: &[u8]) -> u8 {
    let mut col = [0; N];
    let mut row = [0; N];
    for ((r, c), &n) in (0..N).cartesian_product(0..N).zip(board.iter()) {
        let t = times[n as usize];
        col[c] = col[c].max(t);
        row[r] = row[r].max(t);
    }
    col.into_iter()
        .min()
        .unwrap_or(0)
        .min(row.into_iter().min().unwrap_or(0))
}

fn solve(inp: &(Vec<u8>, Vec<Board>), cmp: impl Fn(u8, u8) -> bool, init: u8) -> usize {
    let (moves, boards) = inp;
    let mut times = [0u8; 100];
    for (i, &n) in moves.iter().enumerate() {
        times[n as usize] = i as u8;
    }
    let mut idx = 0;
    let mut win = init;
    for (i, board) in boards.iter().enumerate() {
        let t = time_to_win(board, &times);
        if cmp(t, win) {
            win = t;
            idx = i;
        }
    }
    let board = &boards[idx];
    let score = board.iter().fold(0usize, |a, &n| {
        if times[n as usize] > win {
            a + n as usize
        } else {
            a
        }
    });
    score * (moves[win as usize] as usize)
}

pub fn part1(inp: &(Vec<u8>, Vec<Board>)) -> usize {
    solve(inp, |t, win| t < win, u8::MAX)
}

pub fn part2(inp: &(Vec<u8>, Vec<Board>)) -> usize {
    solve(inp, |t, win| t > win, 0)
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day04.input"));
    let data = read(inp);
    (part1(&data).to_string(), part2(&data).to_string())
}
