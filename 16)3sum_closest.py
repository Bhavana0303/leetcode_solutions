class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the input array in ascending order.
        closest_sum = float('inf')  # Initialize the closest sum to positive infinity.

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

            # Check if the current sum is closer to the target than the previous closest sum.
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum

# Example usage:
nums = [-1, 2, 1, -4]
target = 1
result = Solution().threeSumClosest(nums, target)
print(result)  # Output will be 2, which is the closest sum to the target 1.
  