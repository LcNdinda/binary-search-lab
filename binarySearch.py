
# Searches the input array 'arr' for specified value 'val'
def binary_search(arr, val): # define function

# if our input is empty or we only have a single element and that element is
#NOT the value we're sarching for, return false
    if len(arr)==0 or (len(arr) ==1 and arr[0]!= val):
        return False
    # value at the middle of array
    mid = arr[len(arr)/2]

    if val == mid:
        return True
    if val < mid:
         return binary_search(arr[:len(arr)/2], val)
    if val > mid:
        return binary_search(arr[len(arr)/2+1:],val)
