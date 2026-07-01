class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))

        st = []
        # cars = [(0, 1), (1, 2), (4, 2), (7, 1)]

        # times = [10, 4.5, 3, 3]
        for pos, spd in cars:
            time = (target - pos) / spd 
            while st and time >= st[-1]:
                st.pop()

            st.append(time)
        return len(st)