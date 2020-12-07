use aoc;
use criterion::{criterion_group, criterion_main, Criterion};

pub fn criterion_benchmark(c: &mut Criterion) {
    c.bench_function("Day 01", |b| b.iter(|| aoc::day01::run()));
    c.bench_function("Day 02", |b| b.iter(|| aoc::day02::run()));
    c.bench_function("Day 03", |b| b.iter(|| aoc::day03::run()));
    c.bench_function("Day 04", |b| b.iter(|| aoc::day04::run()));
    c.bench_function("Day 05", |b| b.iter(|| aoc::day05::run()));
    c.bench_function("Day 06", |b| b.iter(|| aoc::day06::run()));
    c.bench_function("Day 07", |b| b.iter(|| aoc::day07::run()));
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
