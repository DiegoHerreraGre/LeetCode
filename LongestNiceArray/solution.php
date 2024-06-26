<?php

class Solution
{
	public $max_len = 1;
	public $start = 0;
	public $compare_and = 0;

	public function longestNiceSubarray($nums)
	{
		$n = count($nums);
		for ($i = 0; $i < $n; $i++) {
			while ($this->compare_and & $nums[$i] != 0) {
				$this->compare_and &= ~$nums[$this->start];
				$this->start += 1;
			}
			$this->compare_and |= $nums[$i];
			$this->max_len = max($this->max_len, $i - $this->start + 1);
		}
		return $this->max_len;
	}
}


