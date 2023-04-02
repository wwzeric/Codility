# A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

# Write a function:

# def solution(A)

# that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

# For example, given array A such that:

# A[0] = 3  A[1] = 2  A[2] = -6
# A[3] = 4  A[4] = 0
# the function should return 5 because:

# (3, 4) is a slice of A that has sum 4,
# (2, 2) is a slice of A that has sum −6,
# (0, 1) is a slice of A that has sum 5,
# no other slice of A has sum greater than (0, 1).




def solution(A):
    la=len(A)
    if la==1:
        return A[0]
    elif la>1:
        ma=max(A)
        if ma<0:
            return ma
        else:
            max_slice=0
            max_ending=0
            for a in A:
                # the whole array can be divided into three parts: A[0]--A[j-1]|A[j]--A[i]|A[i+1]--A[n-1]
                # the A[j] should be a really big number, so if sum(A[:j])<0: so max_ending=0. 
                # then if max_ending>0: current max_ending can accumulate with later value
                max_ending=max(0,max_ending+a)
                max_slice=max(max_slice,max_ending)
            return max_slice
