impl Solution {
    pub fn day_of_the_week(day: i32, month: i32, year: i32) -> String {
        let weekdays = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ];
        let months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        let is_leap_year = |x: i32| -> bool { x % 4 == 0 && (x % 100 != 0 || x % 400 == 0) };

        let num_days = (1971..year)
            .map(|y| 365 + is_leap_year(y) as i32)
            .sum::<i32>()
            + (0..month - 1)
                .map(|m| months[m as usize] + (m == 1 && is_leap_year(year)) as i32)
                .sum::<i32>()
            + day;

        // 01/01/1971 - Friday
        let res_day = (4 + (num_days - 1)) % 7;
        weekdays[res_day as usize].to_string()
    }
}

/// The `Solution` struct represents a solution for a specific problem.
///
/// # Examples
///
/// ```rust
/// let solution = Solution {};
/// ```
///
/// # Safety
/// This struct does not contain any unsafe code and is considered to be safe to use.
struct Solution {}

/// The `Solution` struct contains methods to calculate the day of the week.
fn main() {
    const SOL: Solution = Solution {};
    println!("{}", Solution::day_of_the_week(5, 1, 1994));
}
