'''求最大公约数和最小公倍数：'''
def max_min(num1,num2):
    m = max(num1, num2)
    n = min(num1, num2)
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    print(num1, "和", num2, "的最大公约数为", n)
    l=num1*num2/n
    print(num1, "和", num2, "的最小公倍数为", l)
num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第一个数字："))
max_min(num1,num2)