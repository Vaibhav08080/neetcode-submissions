class Solution:
    def isValid(self, s: str) -> bool:
        # Quick check: if odd length, cannot be valid
        if len(s) % 2 != 0:
            return False

        stack = []
        CloseToOpen = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for c in s:
            if c in CloseToOpen:  # closing bracket
                if stack and stack[-1] == CloseToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:  # opening bracket
                stack.append(c)

        return not stack
