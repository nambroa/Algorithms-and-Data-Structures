"""

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

"""

"""

Idea / Proof:

The widest container (using first and last line) is a good candidate, because of its width.
Its water level is the height of the smaller one of the first and last line.

All other containers are less wide and thus would need a higher water level in order to hold more water.
The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from
further consideration.

"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Variables i and j define the container under consideration. Initialized for the widest container.
        i, j = 0, len(height)-1
        max_water = 0
        while i < j:
            # Compute the water level the current container supports
            water = (j - i) * min(height[i], height[j])
            max_water = max(water, max_water)
            # Remove the smaller (height wise) of the two lines from consideration.
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water
