/**
 * This is the main class, Solution, that houses the function findMedianSortedArrays.
 *
 * This class is mainly responsible for finding the median value of two sorted lists of integers.
 * This is accomplished within the findMedianSortedArrays method.
 *
 * @property findMedianSortedArrays function that takes two lists of integers as parameters.
 * It merges the two lists and sorts them.
 * If the length of the merged list is even, it returns the average of the two middle elements as a double.
 * If the length is odd, it returns the middle element as a double.
 */

class Solution {
	fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {
		val mergedList = (nums1 + nums2).sorted()
		val length = mergedList.size
		return if (length % 2 == 0) {
			(mergedList[length / 2 - 1] + mergedList[length / 2]) / 2.0
		} else {
			mergedList[length / 2].toDouble()
		}
	}
}

fun main() {
	println(Solution().findMedianSortedArrays(listOf(2, 4, 6, 1, 30, 55, 23), listOf(2, 8, 3, 3))) // result --> 3.5
}