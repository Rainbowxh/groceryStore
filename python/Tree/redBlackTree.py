class node:
    def __init__(self,key):
        self.key = key
        self.left = None 
        self.right = None
        self.color = 'red'
    
    def isRed():
        if self.color == 'red':
            return True
        else: 
            return False


class RedBlackTree:
    def __init__(self):
        self.root = None
    
    def insert(self,key):
        if self.root  is None:
            self.root = node(key)
        else:
            self.node = self._insert(key)

    def _insert(self,node,key):
        if node is None:
            node = node(key)
            return 
        #递归
        elif key < node.key:
            node = self._insert(self,node.left,key)
        elif key > node.key:
            node = self._insert(self,node.right,key)
        #回溯
        if(node.right.isRed() and not node.left.isRed()):
            node = self.leftRotate(node)
        if(node.isRed() and node.right.isRed()):
            node = self.rightRotate(node)
        if(node.left.isRed() and node.left.isRed()):
            node = self.centerRotate(node)
        
    def leftRotate(node):
        node_left = node
        node = node.right 
        node_left.right = node.left 
        node.left = node_left
        return node 
    
    def rightRotate(node):
        node_right = node
        node = node.left
        node_right.left = node.right
        node.right = node_right
        return node 
    
    def centerRotate(node):
        if node.right.color == 'red' and node.left.color == 'red':
            node.color = 'black' 
            node.left.color = 'black' 
            node.right.color = 'black' 
        
        

