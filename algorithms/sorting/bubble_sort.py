# https://www.geeksforgeeks.org/bubble-sort/
"""

- In Place Sorting
- Stable: Yes
- Space Complexity: O(1)
- Time Complexity  (Average and Worst): O(n^2)
- Time Complexity  (Best): O(n)

"""


from typing import List

def bubble_sort(arr: List[int]):

    for i in range(len(arr)):
        # Flag to stop the iteration if inner loop didn't swap any item
        is_swappable = False
        for j in range(i+1,  len(arr)):
            if (arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
                is_swappable = True
        if not is_swappable:
            break
    return arr


if __name__ == "__main__":
    arr = [3, 1, 2, 5, 10, 12]
    output = bubble_sort(arr)
    print (output)