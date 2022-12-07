use aoc::*;
use criterion::{criterion_group, criterion_main, Criterion};

macro_rules! bench {
    ($c:expr, $module:path) => {{
        use $module::*;
        let contents = include_bytes!(concat!(
            env!("CARGO_MANIFEST_DIR"),
            "/inputs/",
            stringify!($module),
            ".input"
        ));
        let data = read(contents);

        $c.bench_function(concat!(stringify!($module), "::read"), |b| {
            b.iter(|| read(contents))
        });
        $c.bench_function(concat!(stringify!($module), "::part1"), |b| {
            b.iter(|| part1(&data))
        });
        $c.bench_function(concat!(stringify!($module), "::part2"), |b| {
            b.iter(|| part2(&data))
        });
    }};
}

pub fn criterion_benchmark(c: &mut Criterion) {
    bench!(c, day01);
    bench!(c, day02);
    bench!(c, day03);
    bench!(c, day04);
    bench!(c, day05);
    bench!(c, day06);
    // bench!(c, day07);
    // bench!(c, day08);
    // bench!(c, day09);
    // bench!(c, day10);
    // bench!(c, day11);
    // bench!(c, day12);
    // bench!(c, day13);
    // bench!(c, day14);
    // bench!(c, day15);
    // bench!(c, day16);
    // bench!(c, day17);
    // bench!(c, day18);
    // bench!(c, day19);
    // bench!(c, day20);
    // bench!(c, day21);
    // bench!(c, day22);
    // bench!(c, day23);
    // bench!(c, day24);
    // bench!(c, day25);
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
