// use std::collections::HashMap;
use std::fs;

fn main() {
    let input = "data/day_05.txt";
    let contents = fs::read_to_string(input).unwrap();

    let seeds: Vec<u64> = contents
        .lines()
        .nth(0)
        .unwrap()
        // .split_whitespace()
        .map(|s| s.parse::<u64>())
        .filter_map(Result::ok)
        .collect();

    let mut cat_num: u64 = 0;
    let mut almanac: Vec<Map> = Vec::new();
    let mut almanac_idx_counter = 0;
    for line in contents.lines() {
        if line.contains("seeds") {
            continue;
        }
        if line.contains("map") {
            cat_num += 1;
            let tmp: Vec<Vec<u64>> = Vec::new();
            let map = Map {
                category: cat_num,
                maps: tmp,
            };
            almanac.push(map);
            almanac_idx_counter += 1;

            continue;
        } else if line != "" {
            let params: Vec<u64> = line
                .split_whitespace()
                .map(|s| s.parse::<u64>())
                .filter_map(Result::ok)
                .collect();

            almanac[almanac_idx_counter - 1].maps.push(params);
        };
    }

    let mut next_seeds = seeds;
    for alm in almanac{
    next_seeds = mapping_fast(next_seeds, &alm);
    // println!("{:?}", next_seeds);
    }
    let result = next_seeds.iter().min().unwrap();
    // println!("{}", result);
}

#[derive(Debug)]
struct Map {
    category: u64,
    maps: Vec<Vec<u64>>,
}

fn mapping_fast(seeds: Vec<u64>, map: &Map) -> Vec<u64> {
    // println!("Seeds {:?}", seeds);

    let mut new_seeds: Vec<u64> = Vec::new();
    for s in &seeds {

        let mut found_mapping = false;
        for i in 0..map.maps.len() {
            let a1 = map.maps[i][0];
            let b1 = map.maps[i][0] + map.maps[i][2];
            let a2 = map.maps[i][1];
            let b2 = map.maps[i][1] + map.maps[i][2];
            let dest_range = a1..b1;
            let source_range = a2..b2;
            if source_range.contains(s) {
                found_mapping = true;
                let dest_idx = s - source_range.start;
                let new_seed = dest_range.start + dest_idx;
                new_seeds.push(new_seed);
                println!(
                    "#### NEW MAPPING #### - Seed {:?} in source Range {:?} at destination index {}. We have a mapping from {} -> {}! ",
                    s, source_range, dest_idx, s, new_seed
                );

                // println!("{:?}", dest_range);
                // println!("{:?}", source_range);
            }
        }
        if !found_mapping {
            new_seeds.push(*s);
            // println!("Ok, not so exciting. The mapping is {} -> {}", *s, *s);
        }
    }
    new_seeds
    
}

// too sloooow
fn mapping(seeds: Vec<u64>, map: &Map) -> Vec<u64> {
    let mut source_mapping: Vec<Vec<u64>> = Vec::new();
    let mut destination_mapping: Vec<Vec<u64>> = Vec::new();
    for i in 0..map.maps.len() {
        let a1 = map.maps[i][0];
        let b1 = map.maps[i][0] + map.maps[i][2];
        let a2 = map.maps[i][1];
        let b2 = map.maps[i][1] + map.maps[i][2];
        let dest_range = a1..b1;
        let source_range = a2..b2;
        // println!("{:?}", dest_range.len());
        // println!("{:?}", source_range.len());
        source_mapping.push(source_range.collect());
        destination_mapping.push(dest_range.collect());
    }
    // println!("source_mapping: {:?}", source_mapping);
    // println!("destination_mapping: {:?}", destination_mapping);
    // let mut seeds_mapping: HashMap<u32, u32> = HashMap::new();
    let mut new_seeds = Vec::new();
    for k in &seeds {
        let mut idx1 = 0;
        let mut idx2 = 0;
        let mut found_mapping = false;
        for vs in &source_mapping {
            if vs.contains(k) {
                found_mapping = true;
                idx2 = vs.iter().position(|x| x == k).unwrap();
                new_seeds.push(destination_mapping[idx1][idx2]);
                // seeds_mapping.insert(*k, destination_mapping[idx1][idx2]);
            }
            if idx1 < source_mapping.len() - 1 {
                idx1 += 1;
            }
        }
        if !found_mapping {
            new_seeds.push(*k);
            // seeds_mapping.insert(*k, *k);
        }
    }
    new_seeds
}
