use std::fs;

fn count_neighbors(diagram: &Vec<Vec<bool>>, x: i16, y: i16) -> u32 {
    let directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ];
    let mut count = 0;
    let rows = diagram.len() as i16;
    let cols = diagram[0].len() as i16;

    for (dx, dy) in directions.iter() {
        let nx = x + dx;
        let ny = y + dy;
        if nx < 0 || ny < 0 || nx >= cols || ny >= rows {continue;}
        if diagram[ny as usize][nx as usize] { count += 1; }
    }

    count
}

fn main(){
    let mut diagram: Vec<Vec<bool>> = fs::read_to_string("input.txt").expect("Failed to read input file")
        .lines()
        .map(|line| line.chars().map(|c| c == '@').collect())
        .collect();

    let mut count = 0;
    for y in 0..diagram.len() {
        for x in 0..diagram[0].len() {
            if !diagram[y][x] { continue; }
            let neighbors = count_neighbors(&diagram, x as i16, y as i16);
            if neighbors < 4 {count += 1;}
        }
    }
    println!("{}", count);

    let mut count = 0;
    loop {
        let mut changed = false;
        for y in 0..diagram.len() {
            for x in 0..diagram[0].len() {        
                if !diagram[y][x] { continue; }
                let neighbors = count_neighbors(&diagram, x as i16, y as i16);
                if neighbors < 4 {
                    count += 1;
                    changed = true;
                    diagram[y][x] = false;
                }
            }
        }
        if !changed { break; }
    }  
    println!("{}", count);
}