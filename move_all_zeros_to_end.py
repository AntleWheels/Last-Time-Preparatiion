arr =[1,2,3,4,45,55,0,5,35,6,6,33,5,0,53,0,70,8,0,2,0]
nonZero =[]
zero =[]
for i in arr:
    if i!=0:
        nonZero.append(i)
    else:
        zero.append(i)
print(nonZero+zero)
