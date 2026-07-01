class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = ['+', '-', '*', '/']
        for x in tokens:
            if x not in operators:
                st.append(int(x))

            else:
                second = st.pop()
                first = st.pop()
                if x == '+':
                    st.append(first + second)
                elif x == '-':
                    st.append(first - second)
                elif x == '*':
                    st.append(first * second)
                elif x == '/':
                    st.append(int(first / second))
        return st.pop()