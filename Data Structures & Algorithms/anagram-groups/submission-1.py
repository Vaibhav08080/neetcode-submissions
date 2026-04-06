from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_anagram = defaultdict(list)
        result = []
        for s in strs:
            sorted_s= tuple(sorted(s))
            grp_anagram[sorted_s].append(s)
        for value in grp_anagram.values():
            result.append(value)  
        return result    

        