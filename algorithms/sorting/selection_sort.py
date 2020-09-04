# https://www.geeksforgeeks.org/selection-sort/
"""

- In Place Sorting
- Stable: Yes
- Space Complexity: O(1)
- Time Complexity: O(n^2)

"""

from typing import List

def selection_sort(arr: List[int]):

    # Traverse through all array elements
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    arr = [3, 1, 2, 5, 10, 12]
    output = selection_sort(arr)
    print (output)


"""
3, 1, 2, 5, 10, 12

Iteration1:

"""