n = int(input())
day = 666
count = 0

while True:
    if '666' in str(day):
        count+=1
    if count == n:
        print(day)
        break
    day+=1