import sys
n=sys.stdin.readline().strip()

a=[0]*2
sw=n[0]
for i in n[1:] :
    if sw != i :
        sw = i
        a[int(sw)]+=1

print(max(a))