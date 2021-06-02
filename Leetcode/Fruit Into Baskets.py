class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        maxFruits, windowStart = 0, 0
        fruitFrequency = {}

        for windowEnd in range(len(tree)):
            rightChar = tree[windowEnd]
            if rightChar not in fruitFrequency:
                fruitFrequency[rightChar] = 0
            fruitFrequency[rightChar] += 1

            while len(fruitFrequency) > 2:
                leftChar = tree[windowStart]
                fruitFrequency[leftChar] -= 1

                if fruitFrequency[leftChar] == 0:
                    del fruitFrequency[leftChar]
                windowStart += 1
            maxFruits = max(maxFruits, sum(list(fruitFrequency.values())))
        return maxFruits
