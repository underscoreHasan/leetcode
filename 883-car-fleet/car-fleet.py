class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)

        times = list(map(lambda car:(target - car[0])/car[1], cars))
        res = []

        for t in times:
            while not res or res[-1] < t:
                res.append(t)

        return len(res)
        
        