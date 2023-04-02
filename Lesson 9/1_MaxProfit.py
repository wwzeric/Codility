# An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. 
# If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. 
# Otherwise, the transaction brings loss of A[P] − A[Q].

# For example, consider the following array A consisting of six elements such that:

#   A[0] = 23171
#   A[1] = 21011
#   A[2] = 21123
#   A[3] = 21366
#   A[4] = 21013
#   A[5] = 21367
# If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. 
# If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. 
# It would occur if a share was bought on day 1 and sold on day 5.


def solution(A):
    la=len(A)
    if la<2:
        return 0
    else:
        # transfer the problem to the max slices problem by calculating the gap of numbers:
        # A[0],A[1],A[2],A[3],A[4],A[5],A[6]
        # G[0],G[1],G[2],G[3],G[4],G[5]
        # we just want to find the max slice in gap
        max_slice=max_ending=0
        for i in range(1,la):
            gap=A[i]-A[i-1]
            # the whole array can be divided into three parts: A[0]--A[j-1]|A[j]--A[i]|A[i+1]--A[n-1]
            # the A[j] should be a really big number, so if sum(A[:j])<0: so max_ending=0. then if max_ending>0: current max_ending can accumulate with later value
            max_ending=max(0,max_ending+gap)
            max_slice=max(max_slice,max_ending)
        return max_slice
