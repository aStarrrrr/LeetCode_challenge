def interleave_check(A, B, C):
    if len(C) != len(A) + len(B):
        return False
    i=j=k = 0
    while k < len(C):
        if i < len(A) and A[i] == C[k]:
            i += 1
        elif j < len(B) and B[j] == C[k]:
            j += 1
        else:
            return False
        k += 1
    return True
a = "Karthika"
k = "Abhinand"
l = "KarthikaAbhinand"
print(interleave_check(a, k, l))