use std::collections::HashSet;

use itertools::Itertools;

pub fn read(inp: &str) -> Vec<(bool, [i32; 6])> {
    let mut v = Vec::with_capacity(420);
    for line in inp.split('\n') {
        if let Some((on, cube)) = line.split(' ').next_tuple() {
            let on = on.chars().nth(1).unwrap() == 'n';
            let mut bounds = [0i32; 6];
            let mut i = 0;
            for bound in cube.split(',') {
                if let Some((lo, hi)) = bound[2..].split("..").next_tuple() {
                    bounds[i] = lo.parse::<_>().unwrap();
                    bounds[i + 1] = hi.parse::<_>().unwrap();
                    i += 2;
                }
            }
            v.push((on, bounds));
        }
    }
    v
}

#[inline]
fn vol(cube: [i32; 6]) -> u64 {
    let [x1, x2, y1, y2, z1, z2] = cube;
    (x2 - x1 + 1) as u64 * (y2 - y1 + 1) as u64 * (z2 - z1 + 1) as u64
}

#[inline]
fn clip(a: &[i32; 6], b: &[i32; 6]) -> Option<[i32; 6]> {
    let &[x1, x2, y1, y2, z1, z2] = a;
    let &[a1, b2, c1, d2, e1, f2] = b;

    let x_1 = x1.max(a1);
    let x_2 = x2.min(b2);
    if x_1 >= x_2 {
        return None;
    }

    let y_1 = y1.max(c1);
    let y_2 = y2.min(d2);
    if y_1 >= y_2 {
        return None;
    }
    let z_1 = z1.max(e1);
    let z_2 = z2.min(f2);
    if z_1 >= z_2 {
        return None;
    }
    Some([x_1, x_2, y_1, y_2, z_1, z_2])
}

#[inline]
fn clipped(clipper: &[i32; 6], clipees: &[[i32; 6]]) -> Vec<[i32; 6]> {
    clipees
        .iter()
        .filter_map(|clipee| clip(clipee, clipper))
        .collect()
}

fn sum_vol(cubes: &[[i32; 6]]) -> u64 {
    if cubes.is_empty() {
        return 0;
    }
    let cube = cubes[0];
    let cubes = &cubes[1..];
    let overlap = sum_vol(&clipped(&cube, cubes));
    vol(cube) + sum_vol(cubes) - overlap
}

fn solve(inp: &[(bool, [i32; 6])]) -> u64 {
    if inp.is_empty() {
        return 0;
    }
    let (on, cube) = inp[0];
    let rest = &inp[1..];
    if !on {
        return solve(rest);
    }
    let cubes = rest.iter().map(|(_, c)| *c).collect_vec();
    let overlap = sum_vol(&clipped(&cube, &cubes));
    vol(cube) + solve(rest) - overlap
}

pub fn part1(inp: &[(bool, [i32; 6])]) -> u64 {
    let mut v = Vec::with_capacity(200);
    for &(o, c) in inp {
        if c.iter().all(|&f| -50 <= f && f <= 50) {
            v.push((o, c));
        }
    }
    solve(&v)
}

pub fn part2(inp: &[(bool, [i32; 6])]) -> u64 {
    solve(inp)
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day22.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
