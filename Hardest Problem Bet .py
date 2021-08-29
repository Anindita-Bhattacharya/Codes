t=int(input())
while(t>0):
    A,B,C=map(int,input().split())
    if A<B and A<C:
        print("Draw")
    if B<A and B<C:
        print("Bob")
    if C<A and C<B:
        print("Alice")
    t=t-1
