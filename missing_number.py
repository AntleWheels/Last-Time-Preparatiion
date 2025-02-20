arr =[1,2,3,4,5,8,9,20,21]
arr_set =set(arr)
full_set =set(range(arr[0],arr[-1]+1))
print(full_set-arr_set)