class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for val in s:
            if val=='(' or val=='[' or val=='{':
                stack.append(val)
            else:
                if len(stack)==0:
                    return False
                else:
                    val2 = stack.pop()
                
                if (val2=='{' and val=='}' or 
                   val2=='(' and val==')' or
                   val2=='[' and val==']'):
                    continue
                else:
                    return False
        return len(stack)==0

                