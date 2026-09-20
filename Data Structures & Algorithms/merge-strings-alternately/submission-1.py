class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        k=0
        s=""
        while i < len(word1) and j < len(word2):
            s+=word1[i]
            i+=1
            s+=word2[j]
            j+=1
        if word1:
            s+=word1[i:]
        if word2:
            s+=word2[j:]
        return s