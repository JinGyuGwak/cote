n=int(input())
ar=[]
for i in range(n) :
    data=input().split()
    ar.append((data[0],int(data[1])))
def setting(key):
    return key[1]

result=sorted(ar,key=setting)
print(result)

