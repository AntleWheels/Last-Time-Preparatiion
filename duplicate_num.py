arr =[1,2,3,34,5,43,2,1,3,45,6,45]
original =[]
duplicate =[]
for i in arr:
    if i not in original:
        original.append(i)
    else:
        duplicate.append(i)
print(duplicate)
