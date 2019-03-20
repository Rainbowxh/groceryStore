class Node:
    def __init__(self, initdata):
        self.__data = initdata
        self.__next = None

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setData(self, newdata):
        self.__data = newdata

    def setNext(self, newnext):
        self.__next = newnext

class simpleLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(self.head)
    def add(self,item):
        tmp = Node(item)
        tmp.setNext(self.head.getNext())
        self.head.setNext(tmp)
    def remove(self,item):
        prev = self.head
        while prev.getNext() != self.head:
            cur = prev.getNext()
            if cur.getData() == item:
                prev.setNext(cur.getNext())
            prev = prev.getNext()
    def search(self,item):
        cur = self.head.getNext()
        while cur ！= self.head:
            if cur.getData() == item 
                return True 
            cur = cur.getnext
        returnFalse