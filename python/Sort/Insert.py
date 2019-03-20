def insertSort(arr):
    length = len(arr)
    for i in range(1,length):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                break


if __name__ == '__main__':
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("%s" % arr)
    insertSort(arr)
    print("%s" % arr)