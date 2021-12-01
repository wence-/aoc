pub struct Field<'a> {
    lo: usize,
    hi: usize,
    chr: char,
    passwd: &'a str,
}

pub fn read(contents: &str) -> Vec<Field> {
    let mut data = Vec::<Field>::new();
    for line in contents.lines() {
        match *line
            .split([' ', '-'].as_ref())
            .collect::<Vec<_>>()
            .as_slice()
        {
            [lo, hi, chr, passwd] => {
                data.push(Field {
                    lo: lo.parse().unwrap(),
                    hi: hi.parse().unwrap(),
                    chr: chr.chars().next().unwrap(),
                    passwd,
                });
            }
            _ => unreachable!(),
        }
    }
    data
}

pub fn part1(data: &[Field]) -> usize {
    data.iter().fold(0, |acc, field| {
        let c = field.passwd.chars().filter(|&c| c == field.chr).count();
        if field.lo <= c && c <= field.hi {
            acc + 1
        } else {
            acc
        }
    })
}

pub fn part2(data: &[Field]) -> usize {
    data.iter().fold(0, |acc, field| {
        let loc: char = field.passwd.chars().nth(field.lo - 1).unwrap();
        let hic: char = field.passwd.chars().nth(field.hi - 1).unwrap();
        acc + ((loc == field.chr) ^ (hic == field.chr)) as usize
    })
}

pub fn run() -> (String, String) {
    let contents = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day02.input"));
    let data = read(&contents);
    let p1 = format!("{}", part1(&data));
    let p2 = format!("{}", part2(&data));
    (p1, p2)
}
