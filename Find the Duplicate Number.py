class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h_map = set()
        for i in nums:
            if i in h_map:
                return i
            else:
                h_map.add(i)