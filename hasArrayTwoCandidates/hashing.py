# Python program to find if there are
# two elements wtih given sum

# function to check for the given sum
# in the array
def printPairs(arr, arr_size, sum):
    # Create an empty hash set
    s = set()

    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp in s):
            print(
            "Pair with given sum " + str(sum) +
    " is (" + str(arr[i]) + ", " + str(temp) + ")")
    s.add(arr[i])


# driver code
A = [1, 4, 45, 6, 10, 8]
n = 16
printPairs(A, len(A), n)

# This code is contributed by __Devesh Agrawal__