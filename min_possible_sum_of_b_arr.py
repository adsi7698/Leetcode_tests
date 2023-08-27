class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        hash_list = [True]*(10**6)
        
        counter = 0
        increment = 1
        sum_of_result = 0
        
        if n == 1:
            return 1
        
        while counter < n and increment <= 10**6:
            if target != 1 and target-increment >= 1 and target-increment != increment:
                hash_list[target-increment-1] = False
            
            if hash_list[increment-1]:
                sum_of_result += increment
                counter += 1
                
            increment += 1
            
        return sum_of_result
                
                
        
        