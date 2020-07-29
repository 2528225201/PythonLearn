"""
杨辉三角
输入：无
输出：生成器，按需返回下一行
# """
def triangles():
    x = [1]
    while True:
        yield x
        x = [1]+[x[m]+x[m+1] for m in range(len(x)) if m+1<len(x)]+[1]

# def triangles():
#     p = [1]
#     while True:
#         yield p#generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
#         p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
