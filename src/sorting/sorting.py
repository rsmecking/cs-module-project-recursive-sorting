# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        left = arr[:mid] # Dividing the array elements  
        right = arr[mid:] # into 2 halves 
  
        merge_sort(left) # Sorting the first half 
        merge_sort(right) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays left[] and right[] 
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+= 1
            else: 
                arr[k] = right[j] 
                j+= 1
            k+= 1
            
        # Checking if any element was left 
        while i < len(left): 
            arr[k] = left[i] 
            i+= 1
            k+= 1
          
        while j < len(right): 
            arr[k] = right[j] 
            j+= 1
            k+= 1

    return arr

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
