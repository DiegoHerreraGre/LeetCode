/// `Solution` Struct
///
/// This is the main struct used in the program. The struct has no fields, and its sole purpose is to
/// provide a namespace for the implemented methods on it.
///
/// The methods implemented on the `Solution` struct are designed to solve various problems.
/// One such problem includes finding median of two sorted arrays.
///
/// An instance of `Solution` struct is not intended to be created. It rather serves as a placeholder
/// for implementing methods.
///
/// # Note
/// Fields of the struct can't be directly accessed as they are not defined.

struct Solution;

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let mut merged = vec![];
        let (mut i, mut j) = (0, 0);
        while i < nums1.len() && j < nums2.len() {
            if nums1[i] < nums2[j] {
                merged.push(nums1[i]);
                i += 1;
            } else {
                merged.push(nums2[j]);
                j += 1;
            }
        }
        while i < nums1.len() {
            merged.push(nums1[i]);
            i += 1;
        }
        while j < nums2.len() {
            merged.push(nums2[j]);
            j += 1;
        }
        let mid = merged.len() / 2;
        if merged.len() % 2 == 0 {
            (merged[mid - 1] + merged[mid]) as f64 / 2.0
        } else {
            merged[mid] as f64
        }
    }
}

fn main() {
    let nums1 = vec![1, 3, 5];
    let nums2 = vec![2, 4, 6];
    let median = Solution::find_median_sorted_arrays(nums1, nums2);
    println!("The median is: {}", median);
}
