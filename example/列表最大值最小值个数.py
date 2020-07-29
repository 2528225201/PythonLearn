def mc(x):
    n=[]
    n.append(max(x))
    n.append(min(x))
    n.append(len(x))
    n=tuple(n)
    print(n)

S1 = [9, 7, 8, 3, 2, 1, 55, 6]
S2=['apple','pear','melon','kiwi']
S3='TheQuickBrownFox'
print('List1=',S1)
mc(S1)
print('List2=',S2)
mc(S2)
print('List3=',S3)
mc(S3)
