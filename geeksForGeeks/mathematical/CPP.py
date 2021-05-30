# Python3 program to find
# product of N fractions
# in reduced form.

# Function to return
# gcd of a and b
def gcd(a, b):
    if (a == 0):
        return b;
    return gcd(b % a, a);


# Print the Product of N
# fraction in Reduced Form.
def productReduce(n, num, den):
    new_num = 1;
    new_den = 1;

    # finding the product
    # of all N numerators
    # and denominators.
    for i in range(n):
        new_num = new_num * num[i];
        new_den = new_den * den[i];

        # Finding GCD of
    # new numerator
    # and denominator
    GCD = gcd(new_num, new_den);

    # Converting into
    # reduced form.
    new_num = new_num / GCD;
    new_den = new_den / GCD;

    print(int(new_num), "/",
          int(new_den));


# Driver Code
n = 3;
num = [1, 2, 5];
den = [2, 1, 6];
productReduce(n, num, den);

# This code is contributed
# by mits