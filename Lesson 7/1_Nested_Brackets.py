def solution(S):
    ls=len(S)
    if ls==0:
        return 1
    else:
        v=[]
        c={'{':1,'[':2,'(':3,'}':-1,']':-2,')':-3}
        for i in range(ls):
            if i==0 and c[S[i]]<0: return 0                     #}....
            if c[S[i]]<0 and len(v)==0: return 0                #...()]...
            if c[S[i]]<0:                                       #...(])...
                if c[S[i]]+v[-1]==0:
                    v.pop()
                else:
                    return 0 
            else:
                v.append(c[S[i]])
        if len(v)==0:
            return 1
        else:
            return 0
