class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            anagram = ''.join(sorted(s))
           #print(anagram)
            # anagram_dict[anagram] = anagram_dict.get(anagram, list()).append(s)
            if anagram in anagram_dict:
                anagram_dict[anagram].append(s)
            else:
                anagram_dict[anagram] = [s]
            #print(anagram_dict)
        return list(anagram_dict.values())
