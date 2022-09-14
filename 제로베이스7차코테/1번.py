def solution(img):
    n=len(img[0])
    dfs(0,0,n,img)

def dfs(x,y,n,a:list):
    global answer
    check = a[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=a[i][j]:
                check=-1
                break
    if check==-1:
        print("(",end="")
        answer+="("
        n=n//2
        dfs(x,y,n,a)
        dfs(x,y+n,n,a)
        dfs(x+n,y,n,a)
        dfs(x+n,y+n,n,a)
        print(")",end="")
        answer+=")"
    elif check==1:
        print(1,end='')
        answer+="1"
    else:
        print(0,end='')
        answer+="0"
answer=""
solution(
[[0, 0, 0, 0, 1, 1, 1, 1],
 [0, 0, 0, 0, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 1, 1],
 [1, 1, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1]])
print()
print(answer)