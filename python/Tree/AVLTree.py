#-*- coding:utf-8 -*- #

class  AVLTreeNode(object):
    def __init__(self,key):
        self.key = key 
        self.left = None 
        self.right = None
        self.height = 0  

class AVLTree(object):
    def __init__(self):
        self.root = None
    
    def getHeight(self,node):
        if node is None:
            return -1
        return node.height

    #深度为左右节点深度+1 如果左右节点为空 则深度为0
    def updateHeight(self,node):
        a = self.getHeight(node.right)
        b = self.getHeight(node.left)
        node.height = max(a,b)+1 

    #差值为2的时候则为不平衡，由于时时的缘故不需要
    def balanced(self,node):
        value = abs(self.getHeight(node.left)-self.getHeight(node.right)) 
        return value is  2

    # 全偏向左边则将整个树向右方向旋转
    def right_Rotation(self,node):
        node_right = node
        node = node.left
        node_right.left = node.right
        node.right = node_right
        self.updateHeight(node.right)
        self.updateHeight(node)
        return node

    def left_Rotation(self,node):
        node_left = node
        node  = node.right
        node_left.right = node.left
        node.left = node_left
        self.updateHeight(node.left)
        self.updateHeight(node)
        return node

    def leftRightRotation(self,node):
        node.right = self.left_Rotation(node.left)
        return self.right_Rotation(node)

    def rightLeftRotation(self,node):
        node.left = self.right_Rotation(node.right)
        return self.left_Rotation(node)

    def insert(self, key):
        if self.root is None:
            self.root = AVLTreeNode(key)
        else:
            self.root = self._insert1(self.root,key)
    
    def _insert(self,node,key):
        if node is None:
            node = AVLTreeNode(key)
        elif key < node.key:
            node.left = self._insert(node.left,key)
            if self.balanced(node):
                if key < node.left.key:
                    node = self.right_Rotation(node)
                else :
                    node = self.leftRightRotation(node)    
        elif key > node.key:
            node.right = self._insert(node.right,key)
            if self.balanced(node):
                if key > node.right.key:
                    node = self.left_Rotation(node)
                else:
                    node = self.rightLeftRotation(node)
        self.updateHeight(node)
        return node  

    def _insert1(self,node,key):
        if node is None:
            node = AVLTreeNode(key)
            self.updateHeight(node)
            return node 
        #递归
        if key < node.key:
            node.left = self._insert1(node.left,key)
        else:
            node.right = self._insert1(node.right,key)
        #回溯
        if self.balanced(node):
            if node.left is not None and key < node.left.key:
                print('right')
                node = self.right_Rotation(node)
            if node.right is not None and key > node.right.key:
                print('left')
                node = self.left_Rotation(node)
            if node.left is not None and  key < node.key and key > node.left.key:
                print('leftRight')
                node = self.leftRightRotation
            if node.right is not None and key > node.key and key < node.right.key:
                print('rightLeft')
                node = self.rightLeftRotation(node)
        self.updateHeight(node)
        return node 

Array = map(int,"1 2 3 5 6 7 8 9".split())
Tree = AVLTree()
for i in Array:
    Tree.insert(i)
    print(Tree.root.height)