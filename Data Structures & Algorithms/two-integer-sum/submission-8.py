class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look_up = {}
        for index in range(len(nums)):
            num = nums[index]
            diff = target - num

            if diff not in look_up:
                look_up[num] = index
            else:
                diff_index = look_up[diff]
                return [diff_index, index] if diff_index < index else [index, diff_index]
        