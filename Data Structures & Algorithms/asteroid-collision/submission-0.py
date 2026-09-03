class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        res = []

        for i in asteroids:

            while res and res[-1] > 0 and i < 0:

                if res[-1] < -i:
                    res.pop()
                    continue

                elif res[-1] == -i:
                    res.pop()

                break

            else:
                res.append(i)

        return res