__author__ = 'Nickolas'
L=[[1,2],[1,-1],[5,8],[-4,-2],[4,3]]
M=[]
for i in L:
    n=(max(i))
    M.append((n,i))

print(M)
M.sort()
M.reverse()
print(M)


def mean():
    z=[]
    y =(input("Number to exit press enter"))
    while True:
        if y=="":
            break
        else:
            z.append(y)
            y =(input("Number to exit press enter"))
    print(z)
    sum=0
    for j in z:
        sum+=int(j)
    k=sum/len(z)
    print(k)

mean()