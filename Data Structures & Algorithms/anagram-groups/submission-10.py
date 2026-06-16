from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for string in strs:
            sortedS="".join(sorted(string))
            hashmap[sortedS].append(string)
        return list(hashmap.values())            

        