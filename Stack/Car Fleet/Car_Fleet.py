from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        p = [] # pair: [pos, speed]

        for i, pos in enumerate(position):
            p.append([pos, speed[i]])
        p.sort(key=lambda x: x[0], reverse=True)
        print(p)

        timeStack = []
        for pos, speed in p:
            # speed * time + pos = target
            time = (target - pos) / speed
            timeStack.append(time)
            print("[",pos,", ",speed,"]:",time)
            if len(timeStack) >= 2 and timeStack[-1] <= timeStack[-2]:
                timeStack.pop()

        return len(timeStack)