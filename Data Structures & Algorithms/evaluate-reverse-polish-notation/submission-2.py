class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i not in "+-*/":
                st.append(int(i))
                print(st)
            elif len(st) >= 2:
                fstOP = st.pop()
                scndOP = st.pop()
                val = None
                if i == "+":
                    val = scndOP + fstOP
                elif i == "-":
                    val = scndOP - fstOP
                elif i == "*":
                    val = scndOP * fstOP
                    print(f" {scndOP} * {fstOP} = {val}")
                elif i == "/":
                    val = int(scndOP / fstOP)
                st.append(val)
            else:
                return None
        print(st)
        return st[0]
        