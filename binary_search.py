def binary_search(arr,val_find):
  low =0
  high = len(arr)
  while low < high:
    mid = (low+high)//2
    if val_find == arr[mid]:
      return mid
    if val_find < arr[mid]:
      high = mid-1
    else:
      low = mid+1
    return "nothing"  

 
array = [1, 2, 5, 12, 22, 33, 98]
value = 22
binary_search(array,value)