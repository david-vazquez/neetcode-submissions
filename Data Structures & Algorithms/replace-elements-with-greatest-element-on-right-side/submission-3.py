class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = -1
        for i in range(len(arr)-1, -1, -1):
            n = arr[i]
            arr[i] = biggest
            biggest = max(biggest, n)
        return arr