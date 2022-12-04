#[derive(Debug, PartialEq, Eq)]
pub enum Command {
    N(i32),
    E(i32),
    R(i32),
    F(i32),
}

pub fn read(lines: &str) -> Vec<Command> {
    use Command::{E, F, N, R};
    lines
        .lines()
        .filter_map(|line| {
            let ins = &line[0..1];
            let n = line[1..].parse::<i32>().unwrap();
            match ins {
                "N" => Some(N(n)),
                "S" => Some(N(-n)),
                "E" => Some(E(n)),
                "W" => Some(E(-n)),
                "R" => Some(R(n / 90)),
                "L" => Some(R(4 - (n / 90))),
                "F" => Some(F(n)),
                _ => None,
            }
        })
        .collect()
}

#[derive(Debug)]
struct Ship {
    x: i32,
    y: i32,
    wx: i32,
    wy: i32,
}

impl Ship {
    fn new(wx: i32, wy: i32) -> Ship {
        Ship { x: 0, y: 0, wx, wy }
    }

    fn apply_command(&mut self, c: &Command) {
        use Command::{F, R};
        match c {
            F(n) => {
                self.x += self.wx * n;
                self.y += self.wy * n;
            }
            R(1) => {
                let tx = self.wx;
                self.wx = self.wy;
                self.wy = -tx;
            }
            R(2) => {
                self.wx = -self.wx;
                self.wy = -self.wy;
            }
            R(3) => {
                let ty = self.wy;
                self.wy = self.wx;
                self.wx = -ty;
            }
            _ => unreachable!(),
        }
    }
    fn apply_command1(&mut self, c: &Command) {
        use Command::{E, N};
        match c {
            N(n) => self.y += n,
            E(n) => self.x += n,
            _ => self.apply_command(c),
        }
    }

    fn apply_command2(&mut self, c: &Command) {
        use Command::{E, N};
        match c {
            N(n) => self.wy += n,
            E(n) => self.wx += n,
            _ => self.apply_command(c),
        }
    }
}

pub fn part1(data: &[Command]) -> i32 {
    let mut ship = Ship::new(1, 0);
    for c in data {
        ship.apply_command1(c);
    }
    ship.x.abs() + ship.y.abs()
}

pub fn part2(data: &[Command]) -> i32 {
    let mut ship = Ship::new(10, 1);
    for c in data {
        ship.apply_command2(c);
    }
    ship.x.abs() + ship.y.abs()
}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day12.input"));
    let data = read(contents);
    let p1 = part1(&data).to_string();
    let p2 = part2(&data).to_string();
    (p1, p2)
}
