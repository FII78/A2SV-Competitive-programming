 def largestValues(self, root: Optional[TreeNode]) -> List[int]:
          
        if not root:
            return []
        
        queue = collections.deque([root])
        ans = []
        
        while queue:
            
            maxim = float("-inf")
            n = len(queue)
            
            for i in range(n):
                
                current = queue.popleft()
                
                if current.val > maxim:
                    maxim = current.val 
                    
                if current.left:
                    queue.append(current.left)
                    
                if current.right:
                    queue.append(current.right)
                    
            ans.append(maxim)
        
        return ans
        
