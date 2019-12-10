# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        print(f" the current number in the search {arr[cur_index]}")
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            # This is checking to see if the element to the right smaller
            # keeps on iterating unitl it finds a smallest number
            if arr[smallest_index] > arr[j]:
                # if arr[j] is smaller it is assigned as the new smallest_index
                print(f"{arr[smallest_index]} > {arr[j]}")
                smallest_index = j

        # TO-DO: swap
        # since we are going to switch these two elements we want to temporarily
        # store the smaller number
        copy = arr[i]
        print(f" switching {arr[i]}")
        # now
        arr[i] = arr[smallest_index]
        print(f" with {arr[i]}")
        arr[smallest_index] = copy
        print(f"current {arr}")



    return arr
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
selection_sort(arr1)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    i = 1
    while i <= len(arr) - 1:
        if arr[i - 1] > arr[i]:
            # saving the elements for the swap
            copy = arr[i]
            # next we must acutally change the array
            arr[i] = arr[i - 1]
            # now put the copy of the smaller element into the correct position.
            arr[i - 1] = copy
            # need to reset the index to find the next element
            i = 1
        else:
            # we check the next element to see if its sorted.
            i += 1


    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
