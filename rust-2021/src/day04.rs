use itertools::Itertools;

const N: usize = 5;
type Board = [u8; N * N];

fn parse(word: &[u8]) -> u8 {
    word.iter().fold(0, |a, b| 10 * a + (b - b'0') as u8)
}

pub fn read(inp: &[u8]) -> (Vec<u8>, Vec<Board>) {
    let mut moves = Vec::with_capacity(100);
    let mut boards = Vec::with_capacity(100);
    let mut r = 0;
    let mut board = [0u8; N * N];
    let mut s = inp.split(|&b| b == b'\n').filter(|l| !l.is_empty());

    for n in s.next().unwrap().split(|&b| b == b',') {
        moves.push(parse(n));
    }

    for line in s {
        let mut c = 0;
        for word in line.split(|&b| b == b' ') {
            if word.is_empty() {
                continue;
            }
            let n = parse(word);
            board[r * 5 + c] = n;
            c += 1;
        }
        r = (r + 1) % 5;
        if r == 0 {
            boards.push(board);
            board = [0u8; N * N];
        }
    }
    (moves, boards)
}

fn time_to_win(board: &Board, times: &[u8]) -> u8 {
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
    let board = boards[idx];
    let score = board.into_iter().fold(0usize, |a, n| {
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
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day04.input"));
    let data = read(inp);
    (part1(&data).to_string(), part2(&data).to_string())
}
