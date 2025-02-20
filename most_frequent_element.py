from collections import Counter
arr =[1,2,3,4,5,3,223,2,45,5,3232,2,3,4,53,2,2,32,1]
count = Counter(arr)
print(count.most_common(3))