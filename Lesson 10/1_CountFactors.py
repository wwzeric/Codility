# A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

# For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

def solution(N):
  if N==1:
    return 1
  else:
    i=2
    count=2
    while i*i<N:
      if N%i==0:
        count+=2
    if i*i==N:
      count+=1
    return count
