# def find(arr,k):
#     arr.sort()
#     return arr[-k]

# arr = [4,54654,32,64,32,4,5,4,55,8]
# print(find(arr,3))
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot =arr[len(arr)//2]
        left = [x for x in arr if x<pivot]
        middle =[x for x in arr if x == pivot]
        right =[x for x in arr if x>pivot]
        return (quick_sort(left))+middle+(quick_sort(right))

arr = [4,54654,32,64,32,4,5,4,55,8]
k=1
sorted_arr =quick_sort(arr)
print(f"The {k}th largest element is {sorted_arr[-k]}")