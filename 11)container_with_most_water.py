class Solution(object):
    def maxArea(self, height):
        left, right, res = 0, len(height)-1, 0
        while right > left:
            a = (right-left)*min(height[right],height[left])
            res = a if a > res else res
            if height[left] > height[right]: right -= 1
            else: left += 1
        return res
height= [1, 8, 6, 2, 5, 4, 8, 3, 7]
result=Solution().maxArea(height)
print(result)
  