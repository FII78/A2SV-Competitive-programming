    def characterReplacement(self, s: str, k: int) -> int:
        hashCount = {}
        result = 0
        left = 0
        maxFreq = 0
        
        for right in range(len(s)):
            
            hashCount [s[right]] = 1 + hashCount.get(s[right] , 0)
            maxFreq = max(maxFreq , hashCount[s[right]])
            
            while  (right - left + 1) - maxFreq > k:
                hashCount[s[left]] -= 1
                left += 1

            
            result = max(result , right - left + 1)
        return result
