# Python3 program to find whether an array
# is subset of another array

# Return 1 if arr2[] is a subset of arr1[]


def isSubset(arr1, arr2, m, n):
    i = 0

    quickSort(arr1, 0, m - 1)
    for i in range(n):
        if (binarySearch(arr1, 0, m - 1, arr2[i]) == -1):
            return 0

    # If we reach here then all elements
    # of arr2[] are present in arr1[]
    return 1


# FOLLOWING FUNCTIONS ARE ONLY FOR
# SEARCHING AND SORTING PURPOSE
# Standard Binary Search function


def binarySearch(arr, low, high, x):
    if (high >= low):
        mid = (low + high) // 2

        # Check if arr[mid] is the first
        # occurrence of x.
        # arr[mid] is first occurrence if x is
        # one of the following
        # is true:
        # (i) mid == 0 and arr[mid] == x
        # (ii) arr[mid-1] < x and arr[mid] == x
        if ((mid == 0 or x > arr[mid - 1]) and (arr[mid] == x)):
            return mid
        elif (x > arr[mid]):
            return binarySearch(arr, (mid + 1), high, x)
        else:
            return binarySearch(arr, low, (mid - 1), x)

    return -1

def partition(A, si, ei):
    x = A[ei]
    i = (si - 1)

    for j in range(si, ei):
        if (A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[ei] = A[ei], A[i + 1]
    return (i + 1)


# Implementation of Quick Sort
# A[] --> Array to be sorted
# si --> Starting index
# ei --> Ending index


def quickSort(A, si, ei):
    # Partitioning index
    if (si < ei):
        pi = partition(A, si, ei)
        quickSort(A, si, pi - 1)
        quickSort(A, pi + 1, ei)

    # Driver code


arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

m = len(arr1)
n = len(arr2)

if (isSubset(arr1, arr2, m, n)):
    print("arr2[] is subset of arr1[] ")
else:
    print("arr2[] is not a subset of arr1[] ")

    # This code is contributed by chandan_jnu