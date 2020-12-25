use aoc;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let functions: Vec<fn() -> (String, String)> = vec![
        aoc::day01::run,
        aoc::day02::run,
        aoc::day03::run,
        aoc::day04::run,
        aoc::day05::run,
        aoc::day06::run,
        aoc::day07::run,
        aoc::day08::run,
        aoc::day09::run,
        aoc::day10::run,
        aoc::day11::run,
        aoc::day12::run,
        aoc::day13::run,
        aoc::day14::run,
        aoc::day15::run,
        aoc::day16::run,
        aoc::day17::run,
        aoc::day18::run,
        aoc::day19::run,
        aoc::day20::run,
        aoc::day21::run,
        aoc::day22::run,
        aoc::day23::run,
        aoc::day24::run,
        aoc::day25::run,
    ];

    if args.len() == 2 {
        let (a, b) = match args[1].parse::<usize>() {
            Ok(n) if 1 <= n && n <= 25 => functions[n - 1](),
            _ => {
                eprintln!("Invalid day: '{}'", args[1]);
                return;
            }
        };
        println!("Running day {}", args[1]);
        println!("Part 1: {}", a);
        println!("Part 2: {}", b);
    } else {
        for day in 1..=25 {
            println!("Running day {}", day);
            let (a, b) = functions[day - 1]();
            println!("Part 1: {}", a);
            println!("Part 2: {}", b);
        }
    }
}
