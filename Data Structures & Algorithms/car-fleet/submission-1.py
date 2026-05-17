class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        n = len(position)
        pos_sp = []

        for i in range(len(position)):
            pos_sp.append([position[i], speed[i]])

        pos_sp.sort(reverse=True)

        for pos, speed in pos_sp:
            dist = target-pos
            time = dist/speed

            if stk and stk[-1] >= time:
                continue
            else:
                stk.append(time)

        return len(stk)