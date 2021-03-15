# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example
# n = 7
# arr = [1,1,3,2,2,3,1]

# There is one pair of color and one of color . There are three odd socks left, one of each color. The number of pairs is .

# Function Description

# Complete the sockMerchant function in the editor below.

# sockMerchant has the following parameter(s):

# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns

# int: the number of pairs
# Input Format

# The first line contains an integer, the number of socks represented in .
# The second line contains  space-separated integers, , the colors of the socks in the pile.

from collections import Counter

def SockCount(arr):
    cols = Counter(arr)
    c = 0
    print(cols)
    for key, val in cols.items():
        if val % 2 == 0:
            c  += val // 2
        else:
            val -= 1
            c += val // 2
    return c        

print(SockCount([1,1,2]))    


