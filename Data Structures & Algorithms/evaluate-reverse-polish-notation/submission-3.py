class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i not in "+-*/":
                st.append(int(i))
            elif len(st) >= 2:
                if i == "+":
                    st.append(st.pop() + st.pop())
                elif i == "-":
                    fstOP, scndOP = st.pop(), st.pop()
                    st.append(int(scndOP - fstOP))
                elif i == "*":
                    st.append(st.pop() * st.pop())
                elif i == "/":
                    fstOP, scndOP = st.pop(), st.pop()
                    st.append(int(scndOP / fstOP))
            else:
                return None
        return st[0]
        