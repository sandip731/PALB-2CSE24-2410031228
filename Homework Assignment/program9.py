class Solution:
    def twoSum(self, nums, target):
        seen = {}   # value -> index

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i
nums = [2, 7, 11, 15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))
