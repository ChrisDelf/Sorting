# TO-DO: complete the helpe function below to merge 2 sorted arrays
arr1 = [1, 5, 8, 4, 2]
arr4 = [9, 6, 0, 3, 7]
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i = 0 #<<< this is pivot
    a_index = 0
    b_index = 0

    for i in range(0 , elements):
        if a_index < len(arrA) and  b_index < len(arrB):
            if (arrA[a_index] < arrB[b_index]):
                merged_arr[i] = arrA[a_index]
                a_index += 1
            else:
                merged_arr[i] = arrB[b_index]
                b_index += 1
        elif a_index < len(arrA):
            merged_arr[i] = arrA[a_index]
            a_index += 1
        elif b_index < len(arrB):
            merged_arr[i] = arrB[b_index]
            b_index += 1






    return merged_arr
merge(arr1, arr4)

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
