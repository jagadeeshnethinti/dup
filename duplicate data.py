n=int(input())
l=list(map(int,input.split()))
a=[]
for i in range(0,n):
    for j in range(1,i+1):
        t=a[i]
        a[i]=a[j]
        a[j]=t
if a[i]==a[j]:
    print('duplicate')