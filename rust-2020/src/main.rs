use aoc;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        panic!("Need to specify day");
    }

    let day: usize = match &args[1].parse::<usize>() {
        Ok(n) => *n,
        Err(_) => {
            panic!("Could not parse argument '{}' as day", args[1]);
        }
    };

    println!("Running day {}", day);
    match day {
        1 => {
            let (a, b) = aoc::day01::run();
            println!("Part 1: {}", a);
            println!("Part 2: {}", b);
        }
        2 => {
            let (a, b) = aoc::day02::run();
            println!("Part 1: {}", a);
            println!("Part 2: {}", b);
        }
        3 => {
            let (a, b) = aoc::day03::run();
            println!("Part 1: {}", a);
            println!("Part 2: {}", b);
        }
        4 => {
            let (a, b) = aoc::day04::run();
            println!("Part 1: {}", a);
            println!("Part 2: {}", b);
        }
        5 => {
            let (a, b) = aoc::day05::run();
            println!("Part 1: {}", a);
            println!("Part 2: {}", b);
        }
        6 => {
            let (a, b) = aoc::day06::run();
            println!("Part 1: {}", a);
            println!("Part 2: {}", b);
        }
        7 => {
            let (a, b) = aoc::day07::run();
            println!("Part 1: {}", a);
            println!("Part 2: {}", b);
        }
        _ => {
            panic!("Unhandled day");
        }
    };
}
