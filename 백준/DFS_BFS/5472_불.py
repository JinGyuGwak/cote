ca=int(input())
a=[]
bul=[]
people=[]
for i in range(ca):
    w,h=map(int,input().split())
    a = [list(input()) for i in range(h)]
    for j in range(h):
        for k in range(w):
            if a[j][k]=='*':
                bul.append([j,k])
            elif a[j][k]=='@' :
                people.append([j,k])




