n,k= map(int,input().split())
a=list(map(int,input().split()))
# k 연속적인 일 수
b=[]
hap=0
start=0
for i in range(k):
    hap+=a[i]
b.append(hap)
for i in range(k,n):
    hap+=a[i]
    hap-=a[start]
    start+=1
    b.append(hap)
print(max(b))
