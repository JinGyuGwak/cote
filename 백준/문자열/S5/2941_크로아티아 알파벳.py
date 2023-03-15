a=input()
b=["c=","c-","dz=","d-","lj","nj","s=","z="]

idx=0
count=0
for i in range(len(a)):
    if idx!=i : continue
    if i<len(a)-2 and a[i] + a[i+1] + a[i+2] in b :
        idx+=3
        count+=1
    elif i<len(a)-1 and a[i] + a[i+1] in b:
        idx+=2
        count+=1

    else :
        idx+=1
        count+=1


print(count)