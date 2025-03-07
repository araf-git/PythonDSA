# Selection And Insertion Sort



def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
    return arr


print(selectionSort([5, 3, 6, 2, 10]))  # Output: [2, 3, 5, 6, 10]






# Selection Sort finds the minimum and swaps it, while Bubble Sort repeatedly swaps adjacent elements to move the largest to the end.
# Insertion Sort: Inserts each element into its correct position in the sorted part of the array.





# detailed dry run with i and the updated array at each pass:

# Initial Array: [5, 3, 6, 2, 10]
# i loops from 0 to 4 (range [0,1,2,3,4]).

# Pass 1 (i = 0, range [0,1,2,3,4])
# min_index = 0 (5)
# Compare: 3 < 5 → min_index = 1
# Compare: 6 < 3 → No change
# Compare: 2 < 3 → min_index = 3
# Compare: 10 < 2 → No change
# ✔ Swap arr[0] with arr[3]
# Array after Pass 1: [2, 3, 6, 5, 10]

# Pass 2 (i = 1, range [1,2,3,4])
# min_index = 1 (3)
# Compare: 6 < 3 → No change
# Compare: 5 < 3 → No change
# Compare: 10 < 3 → No change
# ✔ No swap needed
# Array after Pass 2: [2, 3, 6, 5, 10]

# Pass 3 (i = 2, range [2,3,4])
# min_index = 2 (6)
# Compare: 5 < 6 → min_index = 3
# Compare: 10 < 5 → No change
# ✔ Swap arr[2] with arr[3]
# Array after Pass 3: [2, 3, 5, 6, 10]

# Pass 4 (i = 3, range [3,4])
# min_index = 3 (6)
# Compare: 10 < 6 → No change
# ✔ No swap needed
# Array after Pass 4: [2, 3, 5, 6, 10]

# Pass 5 (i = 4, range [4])
# ✔ Only one element left, no swap needed

# Final Sorted Array: ✅ [2, 3, 5, 6, 10]


















# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# print(insertionSort([5, 3, 6, 2, 10]))  # Output: [2, 3, 5, 6, 10]


# Detailed Dry Run:
# Initial Array: [5, 3, 6, 2, 10]

# Pass 1 (i = 1)
# key = 3, j = 0
# Compare: 5 > 3 → Shift 5 → Array: [5, 5, 6, 2, 10]
# j = -1, insert key → Array: [3, 5, 6, 2, 10]
# Pass 2 (i = 2)
# key = 6, j = 1
# Compare: 5 < 6 → No shift
# Insert key → Array: [3, 5, 6, 2, 10]
# Pass 3 (i = 3)
# key = 2, j = 2
# Compare: 6 > 2 → Shift 6 → Array: [3, 5, 6, 6, 10]
# j = 1, compare: 5 > 2 → Shift 5 → Array: [3, 5, 5, 6, 10]
# j = 0, compare: 3 > 2 → Shift 3 → Array: [3, 3, 5, 6, 10]
# j = -1, insert key → Array: [2, 3, 5, 6, 10]
# Pass 4 (i = 4)
# key = 10, j = 3
# Compare: 6 < 10 → No shift
# Insert key → Array: [2, 3, 5, 6, 10]
# Final Sorted Array: ✅ [2, 3, 5, 6, 10]
# This is the proper Insertion Sort for DSA.



