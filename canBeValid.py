def canBeValid(self, s: str, locked: str) -> bool:
 
        
        openP = 0
        closeP = 0
        flipA = 0
    
        if not s or len(s) % 2 != 0:
            return False
        
        
        for i in range(len(s)):
            
            if locked[i] == '0':
                flipA += 1
                
            else:
                if s[i] == '(':
                    openP += 1
                else:
                    closeP += 1
            
            if flipA + openP < closeP:
                return False
        
#         reverse
        openP = 0
        closeP = 0
        flipA = 0
        
        
        for i in range(len(s) - 1, -1, -1):
            
            if locked[i] == "0":
                flipA += 1
                
            else:
                if s[i] == '(':
                    openP += 1
                else:
                    closeP += 1
            
            if flipA + closeP < openP:
                return False
            
            
        return True
                
