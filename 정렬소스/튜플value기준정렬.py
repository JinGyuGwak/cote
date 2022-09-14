array = [('b',2),('a',5),('c',3)]
def set(data):
    print(data)
    return data[1]
result=sorted(array,key=set)
print(result)
