use std::{
    env,
    time::{Duration, Instant},
};

const W_PART: usize = 13;

fn run(day: fn() -> (String, String), reps: u64) -> Duration {
    let now = Instant::now();
    for _ in 0..reps {
        day();
    }
    now.elapsed()
}

fn mini_bench(day: fn() -> (String, String)) -> (f64, (String, String)) {
    let mut reps = 10;
    let mut duration = run(day, reps);
    while duration.as_micros() < 1_000 {
        reps *= 2;
        duration = run(day, reps);
    }
    (duration.as_micros() as f64 / reps as f64, day())
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let functions: Vec<fn() -> (String, String)> = vec![
        aoc::day01::run,
        aoc::day02::run,
        aoc::day03::run,
        aoc::day04::run,
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
    println!(
        "{:10} {:<w$} {:<w$} {:>10}",
        "Day",
        "Part 1",
        "Part 2",
        "Time [μs]",
        w = W_PART
    );
    println!("{:-<w$}", "", w = 2 * W_PART + 20 + 3);
    let mut total_time = 0f64;
    if args.len() == 2 {
        let n = match args[1].parse::<usize>() {
            Ok(n) if (1..=25).contains(&n) => n,
            _ => {
                eprintln!("Invalid day: '{}'", args[1]);
                return;
            }
        };
        let (duration, (a, b)) = mini_bench(functions[n - 1]);
        println!(
            "{:10} {:<w$} {:<w$} {:>n$.2}",
            format!("Day {:02}", n),
            a,
            b,
            duration,
            w = W_PART,
            n = 10,
        );
        total_time += duration;
    } else {
        for (i, &day) in functions.iter().enumerate() {
            let (duration, (a, b)) = mini_bench(day);
            println!(
                "{:10} {:<w$} {:<w$} {:>n$.2}",
                format!("Day {:02}", i + 1),
                a,
                b,
                duration,
                w = W_PART,
                n = 10,
            );
            total_time += duration;
        }
    }
    println!("{:-<w$}", "", w = 2 * W_PART + 20 + 3);
    println!("{:>w$.2}", total_time, w = 2 * W_PART + 10 + 10 + 3);
}
