use itertools::Itertools;
use std::collections;
use std::fs;
use std::path::PathBuf;

fn parse(s: &str) -> Option<collections::HashMap<&str, &str>> {
    let p = s
        .split_whitespace()
        .flat_map(|p| p.split(':'))
        .tuples()
        .collect::<collections::HashMap<_, _>>();
    let invalid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        .iter()
        .any(|k| !p.contains_key(k));
    if invalid {
        return None;
    }
    return Some(p);
}

fn byr(val: &str) -> bool {
    return (1920..=2002).contains(&val.parse::<i32>().unwrap_or(0));
}

fn iyr(val: &str) -> bool {
    return (2010..=2020).contains(&val.parse::<i32>().unwrap_or(0));
}

fn eyr(val: &str) -> bool {
    return (2020..=2030).contains(&val.parse::<i32>().unwrap_or(0));
}

fn hgt(val: &str) -> bool {
    let height = val[0..(val.len() - 2)].parse::<i32>().unwrap_or(0);
    match &val[(val.len() - 2)..] {
        "cm" => {
            return 150 <= height && height <= 193;
        }
        "in" => {
            return 59 <= height && height <= 76;
        }
        _ => {
            return false;
        }
    };
}

fn hcl(val: &str) -> bool {
    return val.starts_with('#')
        && val.len() == 7
        && val.chars().skip(1).all(|c| c.is_ascii_hexdigit());
}

fn ecl(val: &str) -> bool {
    lazy_static! {
        static ref THINGS: collections::HashSet<&'static str> =
            ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                .iter()
                .cloned()
                .collect();
    }
    return THINGS.contains(val);
}

fn pid(val: &str) -> bool {
    return val.len() == 9 && val.chars().all(|c| c.is_ascii_digit());
}

fn valid(p: &collections::HashMap<&str, &str>) -> bool {
    return p.iter().all(|(&k, v)| match k {
        "cid" => true,
        "byr" => byr(v),
        "iyr" => iyr(v),
        "eyr" => eyr(v),
        "hcl" => hcl(v),
        "ecl" => ecl(v),
        "pid" => pid(v),
        "hgt" => hgt(v),
        _ => unreachable!(),
    });
}

fn part1(data: &Vec<collections::HashMap<&str, &str>>) -> usize {
    return data.len();
}

fn part2(data: &Vec<collections::HashMap<&str, &str>>) -> usize {
    return data.iter().filter(|p| valid(p)).count();
}

pub fn run() -> (usize, usize) {
    let mut d = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    d.push("inputs/day04.input");
    let contents = fs::read_to_string(d).expect("ARGH, didn't read");
    let data = contents
        .trim()
        .split("\n\n")
        .filter_map(|s| parse(&s))
        .collect::<Vec<_>>();
    let p1 = part1(&data);
    let p2 = part2(&data);
    return (p1, p2);
}