def yinzi(n):
    for i in range(2,n-1):
        if (n % i == 0):
            print(i)

n = int(input("请输入一个数："))
yinzi(n)
