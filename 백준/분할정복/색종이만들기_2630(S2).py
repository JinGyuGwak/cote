n=int(input())
result=[0,0]

def solution(x,y,z):
   check=a[x][y]
   for i in range(x,x+z):
      for j in range(y,y+z):
         if check !=a[i][j]:
            solution(x,y,z//2)
            solution(x,y+z//2,z//2)
            solution(x+z//2,y,z//2)
            solution(x+z//2,y+z//2,z//2)
            return 

   if check == 1 :
      result[1]+=1
   elif check == 0 :
      result[0]+=1


a=[]
for i in range(n):
   a1=list(map(int,input().split()))
   a.append(a1)
solution(0,0,n)
print(result)
