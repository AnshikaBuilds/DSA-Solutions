class Solution(object):
    def removeDuplicates(self, nums):
        count = 0
        unique = []
        for el in nums:
            if el not in unique:
                unique.append(el)
                count += 1
        nums[:count] = unique
        return count