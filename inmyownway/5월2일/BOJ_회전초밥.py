n,d,k,c=map(int,input().split())
l=[]
for i in range(n):
    sushi=int(input())
    l.append(sushi)

answer=[]
l=l+l[:k]
min=-1
for i in range(len(l)-k):
    temp=l[i:i+k]
    if c not in temp:
        min=max(len(set(temp))+1,min)
    else:
        min = max(len(set(temp)), min)

print(min)



