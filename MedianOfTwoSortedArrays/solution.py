class Solution:
	def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
		mergeList = sorted(nums1 + nums2)
		length = len(mergeList)
		if length % 2 == 0:
			return (mergeList[length // 2 - 1] + mergeList[length // 2]) / 2
		else:
			return mergeList[length // 2]


print(Solution().findMedianSortedArrays([2, 4, 6, 1, 30, 55, 23], [2, 8, 3, 3]))  # result --> 2.000000)
