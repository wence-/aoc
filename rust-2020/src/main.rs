use aoc;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let days;
    if args.len() == 2 {
        match &args[1].parse::<usize>() {
            Ok(n) => days = vec![*n],
            _ => panic!("Couldn't handle argument"),
        }
    } else {
        days = (1..12).collect()
    }

    for d in days {
        println!("Running day {}", d);
        match d {
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
            8 => {
                let (a, b) = aoc::day08::run();
                println!("Part 1: {}", a);
                println!("Part 2: {}", b);
            }
            9 => {
                let (a, b) = aoc::day09::run();
                println!("Part 1: {}", a);
                println!("Part 2: {}", b);
            }
            10 => {
                let (a, b) = aoc::day10::run();
                println!("Part 1: {}", a);
                println!("Part 2: {}", b);
            }
            11 => {
                let (a, b) = aoc::day11::run();
                println!("Part 1: {}", a);
                println!("Part 2: {}", b);
            }
            13 => {
                let (a, b) = aoc::day13::run();
                println!("Part 1: {}", a);
                println!("Part 2: {}", b);
            }
            15 => {
                let (a, b) = aoc::day15::run();
                println!("Part 1: {}", a);
                println!("Part 2: {}", b);
            }
            _ => {
                panic!("Unhandled day");
            }
        };
    }
}
