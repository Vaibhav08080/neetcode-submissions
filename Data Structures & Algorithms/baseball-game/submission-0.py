class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for i in operations:

            if i not in ["C", "D", "+"]:
                res.append(int(i))

            elif i == "+":
                num1 = res.pop()
                num2 = res.pop()

                res.append(num2)
                res.append(num1)
                res.append(num1 + num2)

            elif i == "C":
                res.pop()

            elif i == "D":
                res.append(res[-1] * 2)

        return sum(res)