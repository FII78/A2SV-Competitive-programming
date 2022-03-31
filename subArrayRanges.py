def subArrayRanges(self, nums: List[int]) -> int:
        rangeN=0
        
        for i in range ( len(nums) ):            
            for j in range( i , len(nums) ):
                
                if i == j:    
                    minmum = nums[i]
                    maxmum = nums[i]
                    
                else:
                    minmum = min( minmum , nums[j] )
                    maxmum = max( maxmum , nums[j] )                   
                    rangeN += maxmum - minmum
                    
        
        return rangeN
        
