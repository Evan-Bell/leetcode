class MyQueue:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        while(self.q1):
            self.q2.append(self.q1.pop())
        self.q1.append(x)
        while(self.q2):
            self.q1.append(self.q2.pop())
        

    def pop(self) -> int:
        return self.q1.pop()
        

    def peek(self) -> int:
        return self.q1[-1]
        

    def empty(self) -> bool:
        return self.q1 == []



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)