ab1=int(input())
l2=[]
for i in range (2,ab1+1):
    if(ab1%i)==0:
        l2.append(i)
        ab1=ab1//i
s=sorted(l)
print(*s)
