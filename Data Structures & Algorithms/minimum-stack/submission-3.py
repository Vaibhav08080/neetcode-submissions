class MinStack:

    def __init__(self):
        self.st=[]
        self.s2=[]
    def push(self, val: int) -> None:
        self.st.append(val)
        val=min(val , self.s2[-1] if self.s2 else val)
        self.s2.append(val)
    def pop(self) -> None:
        self.st.pop()
        self.s2.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.s2[-1]

        
