class TreeNode(object): 
 
    def __init__(self, x): 
        self.value = x
        self.left = None
        self.right = None
  
def Max_Depth(node): 
    if node is None: 
        return 0 ;  
  
    else : 
    
        left_Depth = Max_Depth(node.left) 
        right_Depth = Max_Depth(node.right) 
    
        if (left_Depth > right_Depth): 
            return left_Depth+1
        else: 
            return right_Depth+1
 
root = TreeNode(3) 
root.left = TreeNode(9) 
root.right = TreeNode(20) 
root.left.left = TreeNode(0) 
root.left.right = TreeNode(0) 
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
root.left.left.left=TreeNode(3)
root.left.left.right=TreeNode(7)
  
print "Maximum Depth of Binary tree is %d" %(Max_Depth(root)) 

