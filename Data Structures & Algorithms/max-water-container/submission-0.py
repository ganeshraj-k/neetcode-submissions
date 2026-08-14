class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
        left = 0
        right = len(heights) -1


        maxvol = 0

        while left < right:

            smaller_side = 'right'
            if heights[left] < heights[right]:
                smaller_side = 'left'

            vol = min(heights[left], heights[right]) * (right-left)

            maxvol = max(vol, maxvol)

            if smaller_side == 'left':
                left+=1
            else:
                right-=1

        return maxvol




        