fn read(contents: &str) -> (i32, Vec<(i32, i32)>) {
    let lines = contents.lines().collect::<Vec<&str>>();
    let target = lines[0].parse::<i32>().unwrap();
    let buses = lines[1]
        .split(",")
        .enumerate()
        .filter_map(|(i, n)| match n {
            "x" => None,
            n => Some((i as i32, n.parse::<i32>().unwrap())),
        })
        .collect::<Vec<_>>();
    return (target, buses);
}

pub fn part1(target: i32, buses: &[(i32, i32)]) -> i32 {
    let (bus, wait) = buses
        .iter()
        .map(|(_, bus)| (bus, bus - target % bus))
        .min_by_key(|k| k.1)
        .unwrap();
    return bus * wait;
}

pub fn part2_lcm(buses: &[(i32, i32)]) -> i64 {
    let mut time: i64 = 0;
    let mut lcm = 1;
    for (i, bus) in buses {
        while ((time + (*i as i64)) % (*bus as i64)) != 0 {
            time += lcm;
        }
        lcm = lcm * (*bus as i64);
    }
    return time;
}

fn egcd(a: i64, b: i64) -> (i64, i64, i64) {
    if a == 0 {
        (b, 0, 1)
    } else {
        let (g, x, y) = egcd(b % a, a);
        (g, y - (b / a) * x, x)
    }
}

fn mod_inv(x: i64, n: i64) -> Option<i64> {
    let (g, x, _) = egcd(x, n);
    if g == 1 {
        Some((x % n + n) % n)
    } else {
        None
    }
}

fn chinese_remainder(residues: &[i64], modulii: &[i64]) -> Option<i64> {
    let prod = modulii.iter().product::<i64>();
    Some(
        residues
            .iter()
            .zip(modulii)
            .map(|(&residue, &modulus)| {
                let p = prod / modulus;
                residue * mod_inv(p, modulus).unwrap() * p
            })
            .sum::<i64>()
            % prod,
    )
}

pub fn part2_crt(buses: &[(i32, i32)]) -> i64 {
    let (a, n): (Vec<_>, Vec<_>) = buses
        .iter()
        .map(|(i, bus)| ((bus - i) as i64, *bus as i64))
        .unzip();
    let prod = n.iter().product::<i64>();
    return (chinese_remainder(a.as_slice(), n.as_slice()).unwrap() + prod) % prod;
}

pub fn run() -> (i32, i64) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day13.input"));
    let (target, buses) = read(&contents);
    let p1 = part1(target, &buses);
    let p2 = part2_crt(&buses);
    return (p1, p2);
}
