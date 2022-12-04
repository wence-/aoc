use std::mem::size_of;

type Chunk = u64;

const CHUNK_SIZE: usize = size_of::<Chunk>() * 2;

const CHUNK_BITS: usize = Chunk::BITS as usize;

pub fn read(inp: &str) -> Vec<Chunk> {
    let parse = |&b| -> u8 {
        if b < b'A' {
            b - b'0'
        } else {
            b - b'A' + 10u8
        }
    };
    inp.as_bytes()
        .chunks(CHUNK_SIZE)
        .map(|chunk| {
            let mut n = 0;
            for b in chunk {
                n <<= 4;
                n |= parse(b) as Chunk;
            }
            n <<= (CHUNK_SIZE - chunk.len()) * 4;
            n
        })
        .collect()
}

#[inline]
fn decode(bytes: &[Chunk], offset: &mut usize, mut nbits: usize) -> u64 {
    let mut val = 0;
    while nbits > 0 {
        // Need to read nbits, starting at offset (also in bits)
        // Get closest byte and then shift out the bits we don't want
        let current = bytes.get(*offset / CHUNK_BITS).unwrap() << (*offset % CHUNK_BITS);
        let remaining = nbits.min(CHUNK_BITS - *offset % CHUNK_BITS);
        val <<= remaining;
        val |= (current >> (CHUNK_BITS - remaining)) as u64;
        *offset += remaining;
        nbits -= remaining;
    }
    val
}

fn parse_literal(bytes: &[Chunk], offset: &mut usize) -> u64 {
    let mut val = 0;
    let mut mask = 0b10000;
    while mask & 0b10000 != 0 {
        mask = decode(bytes, offset, 5);
        val <<= 4;
        val |= mask & 0b1111;
    }
    val
}

fn parse_packet(bytes: &[Chunk], offset: &mut usize) -> (u64, u64) {
    let mut version = decode(bytes, offset, 3);
    let typ = decode(bytes, offset, 3);
    if typ == 4 {
        return (version, parse_literal(bytes, offset));
    }
    let mode = decode(bytes, offset, 1);
    let n = decode(bytes, offset, if mode == 1 { 11 } else { 15 }) as usize;
    let mut value = None;
    let mut i = 0;
    let old_offset = *offset;
    while i < n {
        let (ver, val) = parse_packet(bytes, offset);
        version += ver;
        value = match typ {
            0 => Some(value.unwrap_or(0) + val),               // Sum
            1 => Some(value.unwrap_or(1) * val),               // Product
            2 => Some(value.unwrap_or(u64::MAX).min(val)),     // Min
            3 => Some(value.unwrap_or(u64::MIN).max(val)),     // Max
            5 => value.map(|v| (v > val) as _).or(Some(val)),  // GT
            6 => value.map(|v| (v < val) as _).or(Some(val)),  // LT
            7 => value.map(|v| (v == val) as _).or(Some(val)), // EQ
            _ => unreachable!(),
        };
        if mode == 1 {
            i += 1;
        } else {
            i = *offset - old_offset;
        }
    }
    (version, value.unwrap_or_else(|| unreachable!()))
}

pub fn part1(inp: &[Chunk]) -> u64 {
    parse_packet(inp, &mut 0).0
}

pub fn part2(inp: &[Chunk]) -> u64 {
    parse_packet(inp, &mut 0).1
}

pub fn run() -> (String, String) {
    let inp = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/inputs/day16.input"));
    let data = read(inp);
    let a = part1(&data).to_string();
    let b = part2(&data).to_string();
    (a, b)
}
