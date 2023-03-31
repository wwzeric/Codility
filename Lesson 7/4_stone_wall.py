# You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

# The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

# Write a function:

# def solution(H)

# that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

# For example, given array H containing N = 9 integers:

#   H[0] = 8    H[1] = 8    H[2] = 5
#   H[3] = 7    H[4] = 9    H[5] = 8
#   H[6] = 7    H[7] = 4    H[8] = 8
# the function should return 7. The figure shows one possible arrangement of seven blocks.


def solution(H):
    last=0
    c=0
    s=[]
    lh=len(H)
    for i in range(lh):
        if H[i]>last:
            last=H[i]
            c+=1
            s.append(H[i])
        elif H[i]<last:
            ls=len(s);j=0
            # kill all the higher wall, remain all the lower wall in the history
            while j<ls and H[i]<s[-1]:
                s.pop()
                j+=1
            if j==ls or H[i]!=s[-1]:
                c+=1
                s.append(H[i])
            last=H[i]
    return c
