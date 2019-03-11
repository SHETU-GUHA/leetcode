class Node: 
    def __init__(self , x): 
        self.value = x  
        self.left = None
        self.right = None
  
def min_Depth(root): 
    if root is None: 
        return 0 
    if root.left is None and root.right is None: 
        return 1
      
    if root.left is None: 
        return min_Depth(root.right)+1
    if root.right is None: 
        return min_Depth(root.left) +1 
      
    return min(min_Depth(root.left), min_Depth(root.right))+1
  
root = Node(3) 
root.left = Node(9) 
root.right = Node(20) 
root.right.left = Node(15)
root.right.right = Node(7) 
print "Minimum Depth of Binary tree is %d" %(min_Depth(root)) 
