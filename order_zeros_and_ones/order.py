def order(arr):
    left_index = len(arr) - 1
    right_index = 0
    if len(arr) <= 1:
        return arr
    
    while left_index > right_index:
        while (left_index >= 0) and arr[left_index] == 1:
            left_index -= 1
        while (right_index <= len(arr)-1) and arr[right_index] == 0:
            right_index += 1
        if left_index > right_index:
            switch(arr, left_index, right_index)
            left_index -= 1
            right_index += 1
    return arr


def switch(arr, left_index, right_index):
        temp = arr[left_index]
        arr[left_index] = arr[right_index]
        arr[right_index] = temp


        
