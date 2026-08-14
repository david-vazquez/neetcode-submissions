class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        # s_dict = {}
        # for i in s:
        #     if i in s_dict:
        #         s_dict[i]+=1
        #     else:
        #         s_dict[i]=1
        s_dict = Counter(s)

        #t_dict = {}
        # for i in t:
        #     if i in t_dict:
        #         t_dict[i]+=1
        #     else:
        #         t_dict[i]=1
        t_dict = Counter(t)
        
        return (s_dict==t_dict)
        

