# https://www.geeksforgeeks.org/bubble-sort/
"""

- In Place Sorting
- Stable: Yes
- Space Complexity: O(1)
- Time Complexity  (Average and Worst): O(n^2)
- Time Complexity  (Best): O(n)

"""


from typing import List

def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    arr = [3, 1, 2, 5, 10, 12]
    output = insertionSort(arr)
    print (output)