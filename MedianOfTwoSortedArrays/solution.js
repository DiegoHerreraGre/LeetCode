/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
const findMedianSortedArrays = function (nums1, nums2) {
	let mergedList = [...nums1, ...nums2].sort((a, b) => a - b);
	let length = mergedList.length;

	if (length % 2 === 0) {
		return (mergedList[length / 2 - 1] + mergedList[length / 2]) / 2;
	} else {
		return mergedList[Math.floor(length / 2)];
	}
};

console.log(findMedianSortedArrays([1, 6, 3, 12, 1, 2], [2, 5, 2]));