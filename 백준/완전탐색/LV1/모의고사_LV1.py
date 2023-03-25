def solution(answer):
    a1=[1,2,3,4,5]
    a2=[2,1,2,3,2,4,2,5]
    a3=[3,3,1,1,2,2,4,4,5,5]
    s=[0,0,0]
    for i in range(len(answer)):
        if a1[i % 5] == answer[i]: s[0]+=1
        if a2[i % 8] == answer[i]: s[1] += 1
        if a3[i % 10] == answer[i]: s[2] += 1

    k=max(s)
    dap=[]
    if k == s[0] : dap.append(1)
    if k == s[1]: dap.append(2)
    if k == s[2]: dap.append(3)
    return dap
