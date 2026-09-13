class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i not in "+-*/":
                st.append(int(i))
            elif i=="+":
                a=st.pop()
                b=st.pop()
                st.append(b+a)
            elif i=="-":
                a=st.pop()
                b=st.pop()
                st.append(b-a)
            elif i=="*":
                a=st.pop()
                b=st.pop()
                st.append(a*b)
            else:
                a=st.pop()
                b=st.pop()
                st.append(int(b/a))
        return st[0]

