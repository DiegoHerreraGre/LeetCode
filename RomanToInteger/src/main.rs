use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut map_charts = HashMap::new();
        map_charts.insert('I', 1);
        map_charts.insert('V', 5);
        map_charts.insert('X', 10);
        map_charts.insert('L', 50);
        map_charts.insert('C', 100);
        map_charts.insert('D', 500);
        map_charts.insert('M', 1000);

        let mut result = 0;
        let chars: Vec<char> = s.chars().collect();
        for i in 0..chars.len() {
            if i + 1 < chars.len() && map_charts[&chars[i]] < map_charts[&chars[i + 1]] {
                result -= map_charts[&chars[i]];
            } else {
                result += map_charts[&chars[i]];
            }
        }

        result
    }
}

fn main() {
    let result = Solution::roman_to_int("III".to_string());
    println!("{}", result);
}
