class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        total = len1 + len2
        half = total // 2
        
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        
        l, r = 0, len(nums1) - 1
        while True:
            i = l+(r-l)//2
            j = half - i - 2

            aRight = nums1[i+1] if (i+1) < len1 else float("infinity")
            aLeft = nums1[i] if i >= 0 else float("-infinity")
            bRight = nums2[j+1] if (j+1) < len2 else float("infinity")
            bLeft = nums2[j] if j >= 0 else float("-infinity")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            else:
                if aLeft > bRight:
                    r = i - 1
                else:
                    l = i + 1