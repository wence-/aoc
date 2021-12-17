type I = u32;

const N: usize = 100;

pub fn read(inp: &str) -> Vec<u8> {
    let mut v = vec![b'9'; (N + 2) * (N + 2)];
    for (i, chunk) in inp.as_bytes().chunks(N + 1).enumerate() {
        v[(i + 1) * (N + 2) + 1..(i + 1) * (N + 2) + N + 1].copy_from_slice(&chunk[..N]);
    }
    v
}

pub fn part1(inp: &[u8]) -> I {
    let mut s = 0;
    for i in 1..=N {
        let row = i * (N + 2);
        for j in 1..=N {
            let idx = row + j;
            let v = inp[idx];
            s += ((v - b'0') as I + 1)
                * ((v < inp[idx - (N + 2)]
                    && v < inp[idx + (N + 2)]
                    && v < inp[idx - 1]
                    && v < inp[idx + 1]) as I);
        }
    }
    s
}

pub fn part2(inp: &[u8]) -> I {
    let mut grid = inp.to_owned();
    let mut sizes = Vec::with_capacity(100);
    fn dfs(grid: &mut [u8], idx: usize, cols: usize) -> I {
        if grid[idx] == b'9' {
            0
        } else {
            grid[idx] = b'9';
            let mut size = 1;
            size += dfs(grid, idx - cols, cols);
            size += dfs(grid, idx + cols, cols);
            size += dfs(grid, idx - 1, cols);
            size += dfs(grid, idx + 1, cols);
            size
        }
    }
    for i in 1..=N {
        let row = i * (N + 2);
        for j in 1..=N {
            let size = dfs(&mut grid, row + j, N + 2);
            if size != 0 {
                sizes.push(size);
            }
        }
    }
    sizes.sort_unstable();
    sizes[sizes.len() - 3..].iter().product::<I>()
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day09.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
