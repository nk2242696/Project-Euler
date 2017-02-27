# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(raw_input())
for tc in xrange(T):
    N=int(raw_input())
    print sum(map(int,str(2**N)))
