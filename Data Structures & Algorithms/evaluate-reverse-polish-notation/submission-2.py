class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for i in tokens:
            if i not in "+-*/":
                st.append(int(i))
            else:
                num1 = st.pop()
                num2 = st.pop()

                if i == "+":
                    st.append(num2 + num1)
                elif i == "-":
                    st.append(num2 - num1)
                elif i == "*":
                    st.append(num2 * num1)
                else:
                    st.append(int(num2 / num1))

        return st[0]