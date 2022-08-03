class Solution:
    def calculate(self, s: str) -> int:
        """
        >>> Solution().calculate("1 + 1")
        2
        >>> Solution().calculate(" 2-1 + 2 ")
        3
        """
        
        stack = []
        cur_num = 0
        op = '+'
        while s:
            char = s[0]
            s = s[1:]
            if char in '0123456789':
                cur_num = cur_num*10 + int(char)
            if (char != " " and char not in '0123456789') or not s:
                
                if op == "-":
                    stack.append(-cur_num)
                if op == "+":
                    stack.append(cur_num)
                if op == "*":
                    stack[-1]*= cur_num
                if op == "/":
                    if stack[-1] < 0 and stack[-1]%cur_num != 0:
                        stack[-1] = stack[-1]//cur_num+1
                    else:
                        stack[-1] = stack[-1]//cur_num
                op = char
                cur_num = 0
            
        return sum(stack)+cur_num
        
        
        #-------------------------------------------
        #SOL WORKS BUT TOO SLOW
        def eval(inp):
            if "+" in inp or '-' in inp:
                for i in range(len(inp)-1,-1,-1):
                    if inp[i] == '+':
                        return eval(inp[:i]) + eval(inp[i+1:])
                    if inp[i] == '-':
                        return eval(inp[:i]) - eval(inp[i+1:])
            if '*' in inp or '/' in inp:
                for i in range(len(inp)-1,-1,-1):
                    if inp[i] == '*':
                        return eval(inp[:i]) * eval(inp[i+1:])
                    if inp[i] == '/':
                        return eval(inp[:i])//eval(inp[i+1:])
                
            return int(inp.strip())
        
        return eval(s)
                
                


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)