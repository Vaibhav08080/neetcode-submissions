class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in "({[":
                st.append(i)
            elif i =="}":
                if not st or st[-1]!="{":
                    return False
                st.pop()
            elif i =="]":
                if not st or st[-1]!="[":
                    return False
                st.pop()
            elif i ==")":
                if not st or st[-1]!="(":
                    return False
                st.pop()
        return not st