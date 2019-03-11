class Node: 
  
    def __init__(self, x): 
        self.data = x 
        self.left = None
        self.right = None
   
def PathSum(node, sum): 
       
    if node is None: 
        return (sum == 0) 
  
    else: 
        answer = 0 
        subSum = sum - node.data  
        if(subSum == 0 and node.left == None and node.right == None): 
            return True 
  
        if node.left is not None: 
            answer = answer or PathSum(node.left, subSum) 
        if node.right is not None: 
            answer = answer or PathSum(node.right, subSum) 
  
        return answer  
 
sum = 22
root = Node(5) 
root.left = Node(4) 
root.left.left = Node(11)
root.left.left.right = Node(2)  
if PathSum(root, sum): 
    print "There is a root-to-leaf path with sum %d" %(sum) 
else: 
    print "There is no root-to-leaf path with sum %d" %(sum)
