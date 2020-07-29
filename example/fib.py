"""
斐波那契数列
输入：max:所需获取的数列位数
输出：相应位数所有的数列值
"""
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        n,a,b = n+1,b,a+b
    return "done"

#for循环迭代
for i in fib(3):
    print(i)

# x = fib(6)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))