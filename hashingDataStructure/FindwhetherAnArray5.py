# Python3 program to find whether an array
# is subset of another array

# Return true if arr2[] is a subset of arr1[]
def isSubset(arr1, m, arr2, n):
    # Create a Frequency Table using STL
    frequency = {}

    # Increase the frequency of each element
    # in the frequency table.
    for i in range(0, m):
        if arr1[i] in frequency:
            frequency[arr1[i]] = frequency[arr1[i]] + 1
        else:
            frequency[arr1[i]] = 1

    # Decrease the frequency if the
    # element was found in the frequency
    # table with the frequency more than 0.
    # else return 0 and if loop is
    # completed return 1.
    for i in range(0, n):
        if (frequency[arr2[i]] > 0):
            frequency[arr2[i]] -= 1
        else:
            return False

    return True


# Driver Code
if __name__ == '__main__':

    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]

    m = len(arr1)
    n = len(arr2)

    if (isSubset(arr1, m, arr2, n)):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[] ")

        # This code is contributed by akhilsaini