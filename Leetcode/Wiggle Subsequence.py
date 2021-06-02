#Bookmarked

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        if n<=1:
            return n
        arr1=[0]*n
        arr2=[0]*n
        arr1[0]=1
        arr2[0]=1
        for i in range(1,n):
            for j in range(i):
                #for positive
                numPairs=arr1[j]-1
                if (numPairs%2==0 and nums[i]>nums[j]) or (numPairs%2==1 and nums[i]<nums[j]):
                    arr1[i]=max(arr1[i], arr1[j]+1)
                    
                #for negative
                numPairs=arr2[j]-1
                if (numPairs%2==0 and nums[i]<nums[j]) or (numPairs%2==1 and nums[i]>nums[j]):
                    arr2[i]=max(arr2[i], arr2[j]+1)
        return max(max(arr1),max(arr2))
