# Bubble sort code dry run


def bubble_sort(arr):
    n = len(arr)  # n = 5

    for i in range(n - 1): # i = [0,1,2,3] (for first iteration)
        for j in range(n - i - 1): # j = [0,1,2,3] (for first iteration)
            if arr[j] > arr[j + 1]:
                # left is more than right, so swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [5, 1, 3, 4, 2]
print(arr)
bubble_sort(arr)
print(arr)
















# full dry run of Bubble Sort for arr = [5, 1, 3, 4, 2]:

# Initial Array:
# [5, 1, 3, 4, 2]

# Pass 1 (i = 0, j = 0 to 3)
# Compare 5 & 1 → Swap → [1, 5, 3, 4, 2]
# Compare 5 & 3 → Swap → [1, 3, 5, 4, 2]
# Compare 5 & 4 → Swap → [1, 3, 4, 5, 2]
# Compare 5 & 2 → Swap → [1, 3, 4, 2, 5]
# Pass 2 (i = 1, j = 0 to 2)
# Compare 1 & 3 → No swap → [1, 3, 4, 2, 5]
# Compare 3 & 4 → No swap → [1, 3, 4, 2, 5]
# Compare 4 & 2 → Swap → [1, 3, 2, 4, 5]
# Pass 3 (i = 2, j = 0 to 1)
# Compare 1 & 3 → No swap → [1, 3, 2, 4, 5]
# Compare 3 & 2 → Swap → [1, 2, 3, 4, 5]
# Pass 4 (i = 3, j = 0 to 0)
# Compare 1 & 2 → No swap → [1, 2, 3, 4, 5]
# Final Sorted Array:
# [1, 2, 3, 4, 5] ✅