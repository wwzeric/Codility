# A non-empty array A consisting of N integers is given.

# A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

# For example, the following array A:

#     A[0] = 1
#     A[1] = 5
#     A[2] = 3
#     A[3] = 4
#     A[4] = 3
#     A[5] = 4
#     A[6] = 1
#     A[7] = 2
#     A[8] = 3
#     A[9] = 4
#     A[10] = 6
#     A[11] = 2
# has exactly four peaks: elements 1, 3, 5 and 10.

# You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure below. You have to choose how many flags you should take with you. The goal is to set the maximum number of flags on the peaks, according to certain rules.



# Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

# For example, given the mountain range represented by array A, above, with N = 12, if you take:

# two flags, you can set them on peaks 1 and 5;
# three flags, you can set them on peaks 1, 5 and 10;
# four flags, you can set only three flags, on peaks 1, 5 and 10.
# You can therefore set a maximum of three flags in this case.



def solution(A):
    la=len(A)
    lb=0
    B=[]
    if la<3:
        return 0
    else:
        for i in range(1,la-1):
            if A[i]>A[i-1] and A[i]>A[i+1]:
                B.append(i)
                lb+=1
                
        # check the gap between peaks
        if lb<1: 
            return 0
        elif lb==1:
            return 1
        else:
            gap=B[lb-1]-B[0]
            mf=0
            k=gap**(0.5) # this is related to the number of flags, nf=i
            k=int(k//1)+1
            mv=min(lb,k)
            # total_distance>=nf*d(>=nf)>=nf**2, if gap<total_distance, then flag cannot be fully set.
            for i in range(mv,0,-1):
                lastF=B[0]
                c=1
                for j in range(lb):
                    if B[j]-lastF>=i and c<i:
                        c+=1
                        lastF=B[j]
                if c<mf:
                    return mf
                elif c>mf:
                    mf=c
        return mf
