class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        esq = 0
        dir = len(nums)-1

        while esq <= dir:
            meio = (esq + dir) // 2

            if nums[meio] == target:
                return meio

            elif nums[meio] < target:
                esq = meio + 1

            elif nums[meio] > target:
                dir = meio - 1

        return esq
