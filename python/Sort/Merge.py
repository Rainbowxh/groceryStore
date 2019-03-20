class Sort:
    def mergeSort(self, alist):
        if len(alist) <= 1:
            return alist

        mid = len(alist) / 2
        left = self.mergeSort(alist[:mid])
        #print("left = " + str(left))
        right = self.mergeSort(alist[mid:])
        #print("right = " + str(right))
        return self.mergeSortedArray(left, right)

    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        sortedArray = []
        l = 0
        r = 0
        while l < len(A) and r < len(B):
            if A[l] < B[r]:
                sortedArray.append(A[l])
                l += 1
            else:
                sortedArray.append(B[r])
                r += 1
        print (sortedArray)
        sortedArray += B[r:]
        sortedArray += A[l:]
        print (sortedArray)
        return sortedArray

unsortedArray = [9,8,7,6,5,4,3,2,1]
merge_sort = Sort()
print(merge_sort.mergeSort(unsortedArray))