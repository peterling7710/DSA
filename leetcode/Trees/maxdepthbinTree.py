def maxDepth(root: TreeNode) -> int:
    
        vals = []
        count = 0
        
        def traverse(n, c):
               
            
            if n:
                c += 1
                vals.append(c)  
                
                if n.left:
                    traverse(n.left, c)
                if n.right:
                    traverse(n.right, c)
            
            
                
        traverse(root, count)
        
        if len(vals) == 0:
            return 0
        
        
        return max(vals)