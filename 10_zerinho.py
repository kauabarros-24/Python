A, B, C = map(int, input().split())

if A == B and B == C:
    print("*")
elif B == C and C != A:
    print("A")
elif C == A and A != B:
    print("B")
else:
    print("C")