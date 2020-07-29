n=[]

for i in range(2,1000):
    if i==2 or i==3:
        print(i)
        n.append(i)

    elif i%2==0:
        continue
    else:
        m=i%6
        if m!=1 and m!=5:
            continue
        else:
            for j in range(3,int(i**0.5)+1,2):
                if i%j==0:
                    break
            else:
                print(i)
                n.append(i)
sum_total=sum(n)
print('1000以内的素数之和为：',sum_total)
