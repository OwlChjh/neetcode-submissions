class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0] * n 
        for i, t in enumerate(temperatures):
            
            while st and temperatures[st[-1]] < t:
                j = st.pop()
                res[j] = i - j
            st.append(i)
        return res


