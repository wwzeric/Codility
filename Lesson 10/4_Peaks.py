# A non-empty array A consisting of N integers is given.

# A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

# For example, the following array A:

#     A[0] = 1
#     A[1] = 2
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
# has exactly three peaks: 3, 5, 10.

# We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

# A[0], A[1], ..., A[K − 1],
# A[K], A[K + 1], ..., A[2K − 1],
# ...
# A[N − K], A[N − K + 1], ..., A[N − 1].
# What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

# The goal is to find the maximum number of blocks into which the array A can be divided.

# Array A can be divided into blocks as follows:

# one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
# two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
# three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
# However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

# The maximum number of blocks that array A can be divided into is three.

def solution(A):
    la=len(A)
    index=[0]*la
    count=0
    if la<3:
        return 0
    else:
        for i in range(1,la-1):
            if A[i]>A[i-1] and A[i]>A[i+1]:
                count+=1
            index[i]=count
        index[la-1]=count
        if count<=1:
            return count
        else:
            kl=[]
            kn=[]
            i=2
            aaa=0
            while i*i<=la:
                if la%i==0:
                    value=la//i
                    kl.append(i)
                    kn.append(value)
                    if value>count:
                        aaa+=1
                i+=1
            kl=kl+kn[::-1]
            kn=kl[::-1]
            del kl[:aaa]
            del kn[:aaa]
            ll=len(kl)
            if ll==0: # this is a prime number
                return 1
            else:
                k=0
                while k<ll:
                    length=kl[k]
                    ind_s=0
                    ind_e=length-1
                    while ind_e<=la-1:
                        if index[ind_s]<index[ind_e]:
                            ind_s=ind_e
                            ind_e+=length
                        else:
                            break
                    if ind_e==la-1+length:
                        return kn[k]
                    k+=1
                return 1
