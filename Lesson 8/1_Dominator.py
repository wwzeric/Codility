# An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

# For example, consider array A such that

#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

def solution(A):
    
    la=len(A)
    if la>0:
        s=[]
        s.append(A[0])
        sc=1
        for i in range(1,la):
            if sc>0:
                if A[i]!=s[-1]:
                    s.pop()
                    sc-=1
                else:
                    s.append(A[i])
                    sc+=1
            else:
                s.append(A[i])
                sc+=1
        if sc==0:   # s has no element, no dominator
            return -1
        else:
            value=s[0]
            index=[]
            count=0
        for i in range(la):
            if value==A[i]:
                index.append(i)
                count+=1
        if count>la//2:
            return index[0]
        else:
            return -1
    else:
        return -1
