class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen, currentSum = 10**6, nums[0]
        n = len(nums)
        i, j = 0, 1
        while j <= n and i < n:
            if currentSum >= target:
                minLen = min(minLen, j-i)
                currentSum -= nums[i]
                i += 1
                continue
            elif j < n:
                currentSum += nums[j]
            j += 1
        if minLen == 10**6:
            return 0
        return minLen
