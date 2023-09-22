class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()
            target = -nums[i]  # Calculate the target for the inner loop
            left, right = i + 1, len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return result

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
res = Solution().threeSum(nums)
print(res)  # Output: [[-1, -1, 2], [-1, 0, 1]]
