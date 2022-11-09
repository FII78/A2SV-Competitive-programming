 def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        self.output = root.val
        self.max_lvl = 1
        
        def dfs(node,cur_lvl):
            
            if not node:
                return
            
            if self.max_lvl < cur_lvl:
                self.max_lvl = cur_lvl
                self.output = node.val
            
            dfs(node.left, cur_lvl + 1)
            dfs(node.right, cur_lvl + 1)
                
        dfs(root,1)
        
        return self.output
        
