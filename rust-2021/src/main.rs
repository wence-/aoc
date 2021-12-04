use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let functions: Vec<fn() -> (String, String)> = vec![
        aoc::day01::run,
        aoc::day02::run,
        aoc::day03::run,
        aoc::day04::run,
    ];
    if args.len() == 2 {
        let (a, b) = match args[1].parse::<usize>() {
            Ok(n) if (1..=25).contains(&n) => functions[n - 1](),
            _ => {
                eprintln!("Invalid day: '{}'", args[1]);
                return;
            }
        };
        println!("Running day {}", args[1]);
        println!("Part 1: {}", a);
        println!("Part 2: {}", b);
    } else {
        for (i, day) in itertools::enumerate(functions) {
            println!("Running day {}", i + 1);
            let (a, b) = day();
            println!("Part 1: {}", a);
            println!("Part 2: {}", b);
        }
    }
}
