class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) // 2:
            return candidate
        else:
            return None

