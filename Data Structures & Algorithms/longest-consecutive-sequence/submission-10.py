class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 1
        if len(nums) == 0:
            output = 0
            return output

        nums = sorted(nums)
        run = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] - nums[i-1] == 1:
                run += 1 
            else:
                run = 1
            output = max(output, run)
        return output
 