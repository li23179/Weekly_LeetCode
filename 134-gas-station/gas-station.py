class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        """
        gas = [1,2,3,4,5], cost = [3,4,5,1,2]
               i                   i
        """

        if sum(gas) < sum(cost):
            return -1

        total_tank = 0
        start = 0 

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            
            if total_tank < 0:
                total_tank = 0
                start = i + 1
        
        return start