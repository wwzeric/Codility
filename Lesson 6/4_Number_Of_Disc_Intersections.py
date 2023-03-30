def solution(A):
    la=len(A)
    left=[]
    right=[]
    total=0
    for i in range(la):
        left.append(i-A[i])
        right.append(i+A[i])
    left.sort()
    right.sort()
    
    j=0
    # i is for right and j is for the left
    for i in range(la):
      while j<la and left[j]<=right[i]:
        # every time a new open circle come in (left[j]<right[i] (without right side to form a close circle))
        # means the new circle overlapping with previous circles (amount: m).
        # the increasing amount of intersection is C(1,m), which can be shown as j-i
        total+=j-i
        j+=1
      if total>10**7: return -1
    return total

# -4 1  l:-4            r:1     1 open circle (new 1, old 0), 0 intersection C(1,0): j-i=0-0
# -1 4  l:-4 -1         r:1     2 open circle (new 1, old 1), 1 intersection C(1,1): j-i=1-0
#  0 4  l:-4 -1 0       r:1     3 open circle (new 1, old 2), 2 intersection C(1,2): j-i=2-0 
#  0 5  l:-4 -1 0 0     r:1     4 open circle (new 1, old 3), 3 intersection C(1,3): j-i=3-0 
#  2 6
#  5 8
  
A=[1,5,2,1,4,0]
print(solution(A))
