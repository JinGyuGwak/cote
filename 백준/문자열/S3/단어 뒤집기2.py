a=input()
result=[]
sw=0
s=[]
for i in a:
    if i == " ":
        while s:
            result.append(s.pop())
        result.append(" ")
    elif i == ">":
        sw=0
        result.append(i)
    elif i == "<":
        while s:
            result.append(s.pop())
        result.append(i)
        sw=1
    elif sw == 0:
        s.append(i)
    elif sw == 1:
        result.append(i)
while s:
    result.append(s.pop())
for i in result:
    print(i,end='')

