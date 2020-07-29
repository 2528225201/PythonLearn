n=[]
sum=0
m=int(input('请输入成绩个数：'))
for i in range(0,m):
    x=int(input('请输入你的成绩：'))
    n.append(x)
    sum=sum+x
average_value=sum/(len(n))
print('平均成绩为：',average_value)