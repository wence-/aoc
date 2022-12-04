use itertools::Itertools;
use std::collections;

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
    Some(p)
}

fn byr(val: &str) -> bool {
    (1920..=2002).contains(&val.parse::<i32>().unwrap_or(0))
}

fn iyr(val: &str) -> bool {
    (2010..=2020).contains(&val.parse::<i32>().unwrap_or(0))
}

fn eyr(val: &str) -> bool {
    (2020..=2030).contains(&val.parse::<i32>().unwrap_or(0))
}

fn hgt(val: &str) -> bool {
    let height = val[0..(val.len() - 2)].parse::<i32>().unwrap_or(0);
    match &val[(val.len() - 2)..] {
        "cm" => (150..=193).contains(&height),
        "in" => (59..=76).contains(&height),
        _ => false,
    }
}

fn hcl(val: &str) -> bool {
    val.starts_with('#') && val.len() == 7 && val.chars().skip(1).all(|c| c.is_ascii_hexdigit())
}

fn ecl(val: &str) -> bool {
    lazy_static! {
        static ref THINGS: collections::HashSet<&'static str> =
            ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                .iter()
                .cloned()
                .collect();
    }
    THINGS.contains(val)
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

pub fn part1(data: &[collections::HashMap<&str, &str>]) -> usize {
    data.len()
}

pub fn part2(data: &[collections::HashMap<&str, &str>]) -> usize {
    data.iter().filter(|p| valid(p)).count()
}

pub fn read(contents: &str) -> Vec<collections::HashMap<&str, &str>> {
    contents
        .trim()
        .split("\n\n")
        .filter_map(parse)
        .collect::<Vec<_>>()
}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day04.input"));
    let data = read(contents);
    let p1 = part1(&data).to_string();
    let p2 = part2(&data).to_string();
    (p1, p2)
}
