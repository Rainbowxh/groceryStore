class bubble():
    def __init__(self,arr):
        self.arr = arr
        self.length = len(arr)

    def compare(a,b):
        if(a>b):
            return 1
        else:
            return 0
    
    def exchange(a,b):
        a,b = b,a 

    def sort(self):
        while self.length>0:
            self.length -= 1
            current = 0
            while current < self.length:
                if(self.compare(self.arr[current],self.arr[current+1])):
                   self.exchange(self.arr[current],self.arr[current+1])
                current + 1 
            
    def sort2(self):
        arr = self.arr
        for i in arr:
            print(i)


arr = bubble([1,2,3,4,5,6])
arr.compare(2,3)