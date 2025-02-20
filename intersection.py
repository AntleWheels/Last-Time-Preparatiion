arr1 =[1,2,3,4,5,643,6,7,8,9,10]
arr2 = [1,2,3,4,5,6,7,8,9,10]
intersection=[]
for i in arr1:
    if i in arr2:
        intersection.append(i)
print(intersection)
print(sorted(arr1))