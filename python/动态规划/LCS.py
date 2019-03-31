#-*- coding:utf-8 -*- #

# 状态转移方程
def lcs(arr): 
    l = len(arr)
    dp = [[0  for i in range(7)] for j in range(7)]
    tmp = []
    for i in range(l):
        dp[i][0] = arr[i]
    for i in range(l):
        for j in range(1,2):
            c = dp[i-1][j-1] + arr[i]
            if c == 0:
                tmp.append([arr[i],c[i-1][j-1]])
    return tmp

if __name__ == '__main__':
    arr= [1,2,3,-1,-3,-4,-5]
    print(lcs(arr))