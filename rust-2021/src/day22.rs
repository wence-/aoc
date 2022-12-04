use itertools::Itertools;

const D: usize = 3;

type Cube = [[i32; 2]; D];

pub fn read(inp: &str) -> Vec<(Cube, bool)> {
    let mut v = Vec::with_capacity(420);
    for line in inp.split('\n') {
        if let Some((on, cube)) = line.split(' ').next_tuple() {
            let on = on.chars().nth(1).unwrap() == 'n';
            let mut bounds = [[0i32; 2]; D];
            for (i, bound) in cube.split(',').enumerate() {
                if let Some((lo, hi)) = bound[2..].split("..").next_tuple() {
                    bounds[i][0] = lo.parse::<_>().unwrap();
                    bounds[i][1] = hi.parse::<_>().unwrap();
                }
            }
            v.push((bounds, on));
        }
    }
    v
}

#[inline]
fn vol(cube: Cube) -> u64 {
    (0..D)
        .map(|i| (cube[i][1] - cube[i][0] + 1) as u64)
        .product()
}

#[inline]
fn clip(a: &Cube, b: &Cube) -> Option<Cube> {
    let [x1, x2] = a[0];
    let [a1, a2] = b[0];

    let x_1 = x1.max(a1);
    let x_2 = x2.min(a2);
    if x_1 >= x_2 {
        return None;
    }

    let [y1, y2] = a[1];
    let [b1, b2] = b[1];
    let y_1 = y1.max(b1);
    let y_2 = y2.min(b2);
    if y_1 >= y_2 {
        return None;
    }
    let [z1, z2] = a[2];
    let [c1, c2] = b[2];
    let z_1 = z1.max(c1);
    let z_2 = z2.min(c2);
    if z_1 >= z_2 {
        return None;
    }
    Some([[x_1, x_2], [y_1, y_2], [z_1, z_2]])
}

#[inline]
fn clipped<'a>(
    clipper: &'a Cube,
    clipees: impl Iterator<Item = &'a Cube> + 'a,
) -> impl Iterator<Item = Cube> + 'a {
    clipees.filter_map(|clipee| clip(clipee, clipper))
}

fn sum_vol(mut cubes: impl Iterator<Item = Cube>) -> u64 {
    if let Some(cube) = cubes.next() {
        let cubes = cubes.collect_vec();
        let overlap = sum_vol(clipped(&cube, cubes.iter()));
        vol(cube) + sum_vol(cubes.into_iter()) - overlap
    } else {
        0
    }
}

fn solve(inp: &[(Cube, bool)]) -> u64 {
    if inp.is_empty() {
        return 0;
    }
    let (cube, on) = inp[0];
    let rest = &inp[1..];
    if !on {
        return solve(rest);
    }
    let cubes = rest.iter().map(|(c, _)| c);
    let overlap = sum_vol(clipped(&cube, cubes));
    vol(cube) + solve(rest) - overlap
}

pub fn part1(inp: &[(Cube, bool)]) -> u64 {
    let mut v = Vec::with_capacity(200);
    for &(c, o) in inp {
        if c.iter().all(|&[lo, hi]| -50 <= lo && hi <= 50) {
            v.push((c, o));
        }
    }
    solve(&v)
}

pub fn part2(inp: &[(Cube, bool)]) -> u64 {
    solve(inp)
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day22.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
