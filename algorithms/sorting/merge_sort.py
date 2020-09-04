# Link: https://www.geeksforgeeks.org/merge-sort/
# Divide and Conquer Paradigm
from typing import List

def merge_sort(arr: List[int]) -> None:
    """
    """
    if (len(arr) > 1):
        mid_index = len(arr)//2

        left_array = arr[:mid_index]
        right_array = arr[mid_index:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0
        print (f"Left : {left_array}")
        print (f"Right : {right_array}")
        print (f"Original Array: {arr}")
        while i< len(left_array) and j < len(right_array):
            if (left_array[i] < right_array[j]):
                arr[k] = left_array[i]
                i += 1
                print (arr)
            else:
                arr[k] = right_array[j]
                j += 1
                print (arr)
            print (arr)
            k += 1
        print (f"After while completion: {arr}")
        # Make sure no element is left from the left array
        while i < len(left_array):
            arr[k] = left_array[i]
            i+=1
            k+=1
        print (f"After left subarray: {arr}")
        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1
        print (f"After right subarray: {arr}")

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end =" ")
    print()



# driver code to test the above code
if __name__ == '__main__':
    arr = [38, 27, 43, 3, 9, 82, 10]
    print ("Given array is", end ="\n")
    printList(arr)
    merge_sort(arr)
    print("Sorted array is: ", end ="\n")
    printList(arr)
