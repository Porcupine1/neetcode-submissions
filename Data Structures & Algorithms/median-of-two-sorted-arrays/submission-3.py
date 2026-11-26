class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        lenA, lenB = len(a), len(b)
        total = lenA + lenB
        half = total // 2
        
        if lenA > lenB:
            a, b = b, a
            lenA, lenB = lenB, lenA
        
        l, r = 0, len(a) - 1
        print(b)
        while True:
            i = l+(r-l)//2
            j = half - i - 2

            aRight = a[i+1] if (i+1) < lenA else float("infinity")
            aLeft = a[i] if i >= 0 else float("-infinity")
            bRight = b[j+1] if (j+1) < lenB else float("infinity")
            bLeft = b[j] if j >= 0 else float("-infinity")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                print(aLeft, bLeft)
                print(aRight, bRight)
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            else:
                if aLeft > bRight:
                    print('here')
                    r = i - 1
                else:
                    l = i + 1