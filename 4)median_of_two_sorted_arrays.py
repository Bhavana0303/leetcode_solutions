class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged=sorted(nums1+nums2)
        total_len=len(merged)

        if total_len%2==0:
            mid1=merged[total_len//2]
            mid2=merged[total_len//2-1]
            median=(mid1+mid2)/2.0
        else:
            median=merged[total_len//2]

        return median
nums1=[1,3]
nums2=[2]
median=Solution().findMedianSortedArrays(nums1,nums2)
print(median)

