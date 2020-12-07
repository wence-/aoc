use std::fs;
use std::path::PathBuf;

struct Field<'a> {
    lo: usize,
    hi: usize,
    chr: char,
    passwd: &'a str,
}

fn read(contents: &str) -> Vec<Field> {
    let mut data = Vec::<Field>::new();
    for line in contents.lines() {
        match line
            .split([' ', '-'].as_ref())
            .collect::<Vec<_>>()
            .as_slice()
        {
            &[lo, hi, chr, passwd] => {
                data.push(Field {
                    lo: lo.parse().unwrap(),
                    hi: hi.parse().unwrap(),
                    chr: chr.chars().nth(0).unwrap(),
                    passwd: passwd,
                });
            }
            _ => panic!(),
        }
    }
    return data;
}

fn part1(data: &Vec<Field>) -> usize {
    return data.iter().fold(0, |acc, field| {
        let c = field.passwd.chars().filter(|&c| c == field.chr).count();
        if field.lo <= c && c <= field.hi {
            acc + 1
        } else {
            acc
        }
    });
}

fn part2(data: &Vec<Field>) -> usize {
    return data.iter().fold(0, |acc, field| {
        let loc: char = field.passwd.chars().nth(field.lo - 1).unwrap();
        let hic: char = field.passwd.chars().nth(field.hi - 1).unwrap();
        acc + ((loc == field.chr) ^ (hic == field.chr)) as usize
    });
}

pub fn run() -> (usize, usize) {
    let mut d = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    d.push("inputs/day02.input");
    let contents = fs::read_to_string(d).expect("ARGH, didn't read");
    let data = read(&contents);
    return (part1(&data), part2(&data));
}
