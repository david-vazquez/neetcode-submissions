class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = -1
        for i in range(len(arr), 0, -1):
            n = arr[i-1]
            arr[i-1] = biggest
            biggest = max(biggest, n)
        return arr