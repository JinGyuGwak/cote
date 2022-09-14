N = int(input())
time = []
for i in range(N):
    a=list(map(int,input().split()))
    time.append(a)

#time = sorted(time, key = lambda a : a[0]) # start 기준으로 오름차순 정렬
# [1,3], [8,8], [4,8] 이 되면 1과 8만 카운트 하므로 start 기준으로 정렬 후 end기준 정렬
#time = sorted(time, key = lambda a : a[1])

#회의의 시작시간과 끝나는 시간이 같을 수 있으므로 둘 다 정렬함
## 오름차순 정렬 시 시간복잡도 : O(NlogN)
## 2차원 요소를 기준으로 정렬할 때 sorted(list, key = lambda a:a[n]) 사용


time.sort(key=lambda a:a[0])
time.sort(key=lambda a:a[1])
last_end = 0
cnt = 0

for start, end in time:
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)
