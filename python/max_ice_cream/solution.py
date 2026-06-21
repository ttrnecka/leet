from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        m = max(costs)
        count_arr = [0] * (m+1)

        for cost in costs:
            count_arr[cost]+=1
        
        ice_bars = 0

        for i in range(1,len(count_arr)):
            if count_arr == 0:
                continue
            if coins < i:
                break

            can_buy = min(coins // i, count_arr[i])
            coins -= can_buy * i
            ice_bars += can_buy

        return ice_bars

        
if __name__ == "__main__":
    solution = Solution()

    print(solution.maxIceCream([1,3,2,4], 7)) # should print 3
    print(solution.maxIceCream([10,6,8,7,7,8], 5)) # should print 0
    print(solution.maxIceCream([5,6,7,8,9], 20)) # should print 3