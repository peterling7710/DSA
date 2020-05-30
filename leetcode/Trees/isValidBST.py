
def isValidBST(root: TreeNode) -> bool:

    if not root:
            return True
        
        def traverse(node, low, high):
            if type(node) != TreeNode:
                print("Not TN")
                return False
        
            if node.left:
                if node.left.val >= low:
                    print("Too high")
                    return False
                
                if node.left.val < low:
                    low = node.left.val
                    
                return traverse(node.left, low, high)
                
            if node.right:
                if node.right.val <= high:
                    print("Too low")
                    return False  
                
                return traverse(node.right, low, high)
             
        return traverse(root, root.val, root.val)