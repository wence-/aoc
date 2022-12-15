use itertools::Itertools;

const P: usize = 99;
pub fn read(inp: &[u8]) -> Vec<u8> {
    let mut v = vec![0_u8; P * P];
    let mut i = 0;
    for &c in inp {
        if c != b'\n' {
            v[i] = c;
            i += 1;
        }
    }
    v
}

pub fn part1(inp: &[u8]) -> u16 {
    let mut visible = vec![0_u8; inp.len()];
    for row in 0..P {
        let mut max = 0;
        for col in 0..P {
            let c = inp[row * P + col];
            if c > max {
                max = c;
                visible[row * P + col] = 1;
            }
        }
        max = 0;
        for col in (0..P).rev() {
            let c = inp[row * P + col];
            if c > max {
                max = c;
                visible[row * P + col] = 1;
            }
        }
    }
    for col in 0..P {
        let mut max = 0;
        for row in 0..P {
            let c = inp[row * P + col];
            if c > max {
                max = c;
                visible[row * P + col] = 1;
            }
        }
        max = 0;
        for row in (0..P).rev() {
            let c = inp[row * P + col];
            if c > max {
                max = c;
                visible[row * P + col] = 1;
            }
        }
    }
    visible.iter().map(|&x| x as u16).sum::<u16>()
}

pub fn part2(inp: &[u8]) -> u32 {
    let ray = |mut i, mut j, (istride, jstride)| -> u32 {
        let val = inp[i * P + j];
        for c in 0.. {
            i = (i as i64 + istride) as usize;
            j = (j as i64 + jstride) as usize;
            if i >= P || j >= P {
                return c;
            }
            if inp[i * P + j] >= val {
                return c + 1;
            }
        }
        100
    };
    (0..P).cartesian_product(0..P).fold(0u32, |acc, (i, j)| {
        acc.max(
            [(-1, 0), (1, 0), (0, -1), (0, 1)]
                .iter()
                .fold(1u32, |acc, &x| acc * ray(i, j, x)),
        )
    })
}

pub fn run() -> (String, String) {
    let inp = include_bytes!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day08.input"));

    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
