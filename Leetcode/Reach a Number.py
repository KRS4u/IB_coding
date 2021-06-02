class Solution:
    def reachNumber(self, target: int) -> int:
        target=abs(target)
        step=0
        totalSum=0
        while True:
            step+=1
            totalSum+=step
            if totalSum==target:
                return step
            elif totalSum>target and (totalSum-target)%2==0:
                return step
