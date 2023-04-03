# A non-empty array A consisting of N integers is given.

# A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

# The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

# For example, array A such that:

#     A[0] = 3
#     A[1] = 2
#     A[2] = 6
#     A[3] = -1
#     A[4] = 4
#     A[5] = 5
#     A[6] = -1
#     A[7] = 2
# contains the following example double slices:

# double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
# double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
# double slice (3, 4, 5), sum is 0.
# The goal is to find the maximal sum of any double slice.


def solution(A):
    la=len(A)

    left_end=right_end=0
    LR=[0]*la;RL=[0]*la
    for i in range(1,la-1):
        # here we dont want the max_slice, the max_slice cannot meet the requirement that only one element between left and right array [6 5|-1 -1| 4 3]
        # in this case, we can only use the accumulator, when the accumulate<0, discard the accumulated part, otherwise move on
        left_end=max(0,left_end+A[i])
        LR[i]=left_end
        right_end=max(0,right_end+A[la-i-1])
        RL[la-1-i]=right_end

    mv=0
    for i in range(1,la-1):
        mv=max(mv,LR[i-1]+RL[i+1])
    return mv
