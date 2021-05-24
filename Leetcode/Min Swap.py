#Bookmarked

class Solution:
    
    def minSwap(self, nums1, nums2) -> int:
        n = min(len(nums1), len(nums2))
        c = 0
        dp = [0]*n
        dp[0] = (0, 1)
        for i in range(1, n):
            min1 = 10**5
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                min1 = dp[i-1][0]
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                min1 = min(min1, dp[i-1][1])
            min2 = 10**5
            if nums2[i] > nums1[i-1] and nums1[i] > nums2[i-1]:
                min2 = dp[i-1][0]+1
            if nums2[i] > nums2[i-1] and nums1[i] > nums1[i-1]:
                min2 = min(min2, dp[i-1][1]+1)
            dp[i] = (min1, min2)
        if (len(nums1) > n and nums1[n] > max(nums1[n-1], nums2[n-1])) or (len(nums2) > n and nums2[n] > max(nums1[n-1], nums2[n-1])):
            return min(dp[n-1][0], dp[n-1][1])
        if((len(nums1) > n and nums1[n] < nums1[n-1]) or (len(nums2) > n and nums2[n] < nums2[n-1])):
            return dp[n-1][1]
        if((len(nums1) > n and nums1[n] < nums2[n-1]) or (len(nums2) > n and nums2[n] < nums1[n-1])):
            return dp[n-1][0]
        return min(dp[n-1][0], dp[n-1][1])




obj = Solution().minSwap([0,1,4,6,8],[1,2,2,7,10])
print(obj)
