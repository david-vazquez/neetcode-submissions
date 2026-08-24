class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)<2:
            return len(arr)

        maxLength = 1
        curLength = 1
        lastComp = 0
        L = 0
        

        for R in range(1, len(arr)):
            if arr[R]==arr[R-1]:
                curComp = 0
                curLength = 1
                L = R
            else:
                # Get the comparison side
                if arr[R]>arr[R-1]:
                    curComp = 1
                else:
                    curComp = -1
                
                # Act accordingly
                if curComp != lastComp:
                    maxLength = max (maxLength, R-L+1)
                else:
                    L = R-1

                lastComp = curComp
        
        return maxLength



