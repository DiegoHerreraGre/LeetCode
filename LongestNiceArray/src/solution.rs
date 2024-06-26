pub fn longest_nice_subarray(nums: Vec<i32>) -> i32 {
    let mut max_len = 1;
    let mut current_and = 0;
    let mut start = 0;

    for end in 0..nums.len() {
        while (current_and & nums[end]) != 0 {
            current_and &= !nums[start];
            start += 1;
        }

        current_and |= nums[end];
        max_len = max_len.max(end - start + 1);
    }

    max_len as i32
}