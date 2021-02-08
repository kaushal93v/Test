def sortarr(arr):
    sorted_arr= []
    n = len(arr)
    for i in range(n):
        min_val = min(arr)
        print(min_val)
        arr.remove(min_val)
        sorted_arr.append(min_val)
    return sorted_arr