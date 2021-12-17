type T = u8;
type I = u32;

/*
 *    0
 *  1   2
 *    3
 *  4   5
 *    6
 */
pub fn read(inp: &str) -> Vec<[T; 14]> {
    let mut v = Vec::with_capacity(100);
    for line in inp.trim().split('\n') {
        let mut decoded = [0u8; 14];
        let mut i = 0;
        for word in line.split(' ') {
            if word == "|" {
                continue;
            }
            let mut x = 0u8;
            for c in word.chars() {
                match c {
                    'a' => x |= 0b0000_0001,
                    'b' => x |= 0b0000_0010,
                    'c' => x |= 0b0000_0100,
                    'd' => x |= 0b0000_1000,
                    'e' => x |= 0b0001_0000,
                    'f' => x |= 0b0010_0000,
                    'g' => x |= 0b0100_0000,
                    _ => unreachable!(),
                }
            }
            decoded[i] = x;
            i += 1;
        }
        v.push(decoded);
    }
    v
}

pub fn part1(inp: &[[T; 14]]) -> I {
    let mut ret = 0;
    for line in inp.iter() {
        for i in 10..14 {
            match line[i].count_ones() {
                2 | 3 | 4 | 7 => ret += 1,
                _ => (),
            }
        }
    }
    ret
}

fn decode(line: [T; 14]) -> I {
    let (mut one, mut four, mut seven) = (0, 0, 0);
    let eight = 0b0111_1111;
    let mut zero_six_nine = [0; 3];
    for i in 0..10 {
        let digit = line[i];
        match digit.count_ones() {
            2 => one = digit,
            3 => seven = digit,
            4 => four = digit,
            6 => {
                zero_six_nine[0] = digit;
                zero_six_nine.rotate_right(1);
            }
            _ => (),
        }
    }
    let mut segments = [0; 7];

    segments[0] = seven & !one;
    for x in &zero_six_nine[..3] {
        let c = eight & !x;
        if c & one != 0 {
            segments[2] = c;
            segments[5] = one & !c;
        } else if c & four != 0 {
            segments[3] = c;
            segments[1] = four & !one & !c;
        } else {
            segments[4] = c;
            segments[6] = x & !four & !seven;
        }
    }
    let mut digits = [0; 10];

    digits[0] = eight & !segments[3];
    digits[1] = one;
    digits[2] = eight & !segments[1] & !segments[5];
    digits[3] = eight & !segments[1] & !segments[4];
    digits[4] = four;
    digits[5] = eight & !segments[2] & !segments[4];
    digits[6] = eight & !segments[2];
    digits[7] = seven;
    digits[8] = eight;
    digits[9] = eight & !segments[4];

    let mut decoder = [I::default(); 256];
    for i in 0..10 {
        decoder[digits[i] as usize] = i as I;
    }
    let mut ret = 0;
    for i in 10..14 {
        ret *= 10;
        ret += decoder[line[i] as usize]
    }
    ret
}
pub fn part2(inp: &[[T; 14]]) -> I {
    inp.iter()
        .fold(I::default(), |acc, &line| acc + decode(line))
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day08.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
