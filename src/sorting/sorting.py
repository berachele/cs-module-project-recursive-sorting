# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    joinedArr = arrA + arrB
    for i in joinedArr:
        merged_arr.pop(0)
        merged_arr.append(i)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        #recursively breaking down left and right side
        merge_sort(left)
        merge_sort(right)

        


    return arr





#TESTING
# arrA = [1, 2, 3, 4, 5]
# arrB = [6, 7, 8, 9, 10]

# print(merge(arrA, arrB))


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
