class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mapping = {']': '[', '}': '{', ')': '('}

        for ch in s:
            if ch in mapping:
                top = st.pop() if st else '#'
                if mapping[ch] != top:
                    return False
            else:
                st.append(ch)

        return not st
