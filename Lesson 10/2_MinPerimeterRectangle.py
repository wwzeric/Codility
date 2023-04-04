# An integer N is given, representing the area of some rectangle.

# The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

# The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

# For example, given integer N = 30, rectangles of area 30 are:

# (1, 30), with a perimeter of 62,
# (2, 15), with a perimeter of 34,
# (3, 10), with a perimeter of 26,
# (5, 6), with a perimeter of 22.

def solution(N):
    index=1
    divisor=N
    i=2
    while i*i<N:
        if N%i==0:
            index=i
            divisor=N//i
        i+=1
    if i*i==N:
        return 4*i
    return 2*(divisor+index)
