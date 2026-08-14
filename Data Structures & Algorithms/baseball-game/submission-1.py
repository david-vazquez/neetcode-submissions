class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        res = 0
        for o in operations:
            if o == '+':
                val = record[-1]+record[-2]
                res += val
                record.append(val)
            elif o == 'D':
                val = record[-1]*2
                res += val
                record.append(val)
            elif o == 'C':
                val = record.pop()
                res -= val
            else:
                val = int(o)
                res += val
                record.append(val)
        return res    