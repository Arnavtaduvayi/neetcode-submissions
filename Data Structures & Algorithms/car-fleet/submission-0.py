class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        fleets = 0
        currHighest = float('-inf')

        while cars :
            carP, carS = cars.pop()
            time = float((target-carP)/carS)
            if time > currHighest :
                fleets += 1
                currHighest = time
        return fleets