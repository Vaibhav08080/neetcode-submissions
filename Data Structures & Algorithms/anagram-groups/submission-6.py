class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for _ in strs:
            srtds=''.join(sorted(_))
            res[srtds].append(_)
        return list(res.values())
        