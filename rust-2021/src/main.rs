use std::env;

const W_PART: usize = 12;
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
    ];
    println!("{:10} {:<w$} {:<w$}", "Day", "Part 1", "Part 2", w = W_PART);
    println!("{:-<w$}", "", w = 2 * W_PART + 10);
    if args.len() == 2 {
        let n = match args[1].parse::<usize>() {
            Ok(n) if (1..=25).contains(&n) => n,
            _ => {
                eprintln!("Invalid day: '{}'", args[1]);
                return;
            }
        };
                
        let (a, b) = functions[n - 1]();
        println!(
            "{:10} {:<w$} {:<w$}",
            format!("Day {:02}", n),
            a,
            b,
            w = W_PART
        );
    } else {
        for (i, day) in functions.iter().enumerate() {
            let (a, b) = day();
            println!(
                "{:10} {:<w$} {:<w$}",
                format!("Day {:02}", i + 1),
                a,
                b,
                w = W_PART
            );
        }
    }
}
