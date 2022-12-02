use std::{env, time::Instant};

const W_PART: usize = 14;

fn main() {
    let args: Vec<String> = env::args().collect();
    let functions: Vec<fn() -> (String, String)> = vec![
        aoc::day01::run,
        aoc::day02::run,
        // aoc::day03::run,
        // aoc::day04::run,
        // aoc::day05::run,
        // aoc::day06::run,
        // aoc::day07::run,
        // aoc::day08::run,
        // aoc::day09::run,
        // aoc::day10::run,
        // aoc::day11::run,
        // aoc::day12::run,
        // aoc::day13::run,
        // aoc::day14::run,
        // aoc::day15::run,
        // aoc::day16::run,
        // aoc::day17::run,
        // aoc::day18::run,
        // aoc::day19::run,
        // aoc::day20::run,
        // aoc::day21::run,
        // aoc::day22::run,
        // aoc::day23::run,
        // aoc::day24::run,
        // aoc::day25::run,
    ];
    println!("{:10} {:<w$} {:<w$} {:>w$}", "Day", "Part 1", "Part 2", "Time [μs]", w = W_PART);
    println!("{:-<w$}", "", w = 3 * W_PART + 10 + 3);
    let start = Instant::now();
    if args.len() == 2 {
        let n = match args[1].parse::<usize>() {
            Ok(n) if (1..=25).contains(&n) => n,
            _ => {
                eprintln!("Invalid day: '{}'", args[1]);
                return;
            }
        };
        let now = Instant::now();
        let (a, b) = functions[n - 1]();
        println!(
            "{:10} {:<w$} {:<w$} {:>w$}",
            format!("Day {:02}", n),
            a,
            b,
            now.elapsed().as_micros(),
            w = W_PART
        );
    } else {
        for (i, day) in functions.iter().enumerate() {
            let now = Instant::now();
            let (a, b) = day();
            println!(
                "{:10} {:<w$} {:<w$} {:>n$}",
                format!("Day {:02}", i + 1),
                a,
                b,
                now.elapsed().as_micros(),
                w = W_PART,
                n = 11,
                    
            );
        }
    }
    println!("{:-<w$}", "", w = 3 * W_PART + 10 + 3);
    println!("{:>w$}", start.elapsed().as_micros(), w = 3 * W_PART + 10 + 3);
}
