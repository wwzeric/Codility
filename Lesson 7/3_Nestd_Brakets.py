# A string S consisting of N characters is called properly nested if:

# S is empty;
# S has the form "(U)" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())" isn't.

# Write a function:

# def solution(S)

# that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

# For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..1,000,000];
# string S is made only of the characters '(' and/or ')'.
# Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.


def solution(S):
    ls=len(S)
    total=0
    if ls==0:
        return 1
    else:
        array=[]
        if S[0]==')':
            return 0
        else:
            for s in S:
                if s=='(':
                    array.append(1)
                elif s==')':
                    array.append(-1)
            for i in range(ls):
                total+=array[i]
                if total<0:
                    return 0
            if total==0:
                return 1
            else: 
                return 0
