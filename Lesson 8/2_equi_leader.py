# A non-empty array A consisting of N integers is given.

# The leader of this array is the value that occurs in more than half of the elements of A.

# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# we can find two equi leaders:

# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.
def solution(A):
    la=len(A)
    if la==1:
        return 0
    else:
        s=[]
        s.append(A[0])
        sc=1
        result=0
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
            return 0
        else:
            value=s[0]
            count=0
        for i in range(la):
            if value==A[i]:
                count+=1
            # the total outnumber is sc, so the rc<sc means we reserve 1 more leader for the right side (sc-rc>0)
            # we have to make the left side is 1 more leader (rc>0) and right side is 1 more leader (rc<sc)
            # cannot do this, because the sc is not accurate if we can try the following array
            # import numpy as np
            # A=list(np.random.randint(low = 3,high=8,size=50))+[-10**9]*200+list(np.random.randint(low = 3,high=8,size=50))
            # print(solution(A)) 
        if count>la//2:
            # return result1
            rc=0
            for i in range(la):
                if value==A[i]:
                    rc+=1
                else:
                    rc-=1
                # here I use the same principle, rc>0 for the left side, rc<count-(la-count) for the right side. real sc=count-(la-count)
                if rc>0 and rc<2*count-la:
                    result+=1
            return result
        else:
            return 0
          
          
       
