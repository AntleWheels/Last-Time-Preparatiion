def bubble_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        n =len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] =arr[j+1],arr[j]

arr =[4,54654,32,64,32,4,5,4,55,8]
bubble_sort(arr)
print(arr)