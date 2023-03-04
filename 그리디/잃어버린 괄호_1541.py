a=input().split('-')
c=[]
for i in a:
    hap=0
    b=i.split('+')
    for j in b:
        hap+=int(j)
    c.append(hap)
hap=c[0]+c[0]
for i in c :
    hap -= i
print(hap)



