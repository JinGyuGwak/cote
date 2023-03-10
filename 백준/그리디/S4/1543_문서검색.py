a=input()
m=input()
count=0
index=0
for i in range(len(a)):

    sw=a[i:i+len(m)]

    if sw == m and i>=index:
        count+=1
        index=i+len(m)

print(count)