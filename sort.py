arr=[5,4,2,8,9]
size = len(arr)
print(arr)

for j in range(size-1):
    for i in range(size-1):
        if arr[i]>arr[i+1]:
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1] = temp



print(arr)