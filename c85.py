import collections, heapq, sys

cases = int(sys.stdin.readline())
for case in range(1, cases + 1):
    N, K       = map(int, sys.stdin.readline().split())
    a, b, c, r = map(int, sys.stdin.readline().split())

    # Reduce N to range (K..2K]:
    if N > K + K + 1:
        N = K + (N - K)%(K + 1)

    # Generate first K elements from PRNG parameters:
    M = [a]
    for i in range(1, K):
        M.append((M[i - 1]*b + c)%r)

    # Initialize sliding window data structures.
    present = collections.Counter(M)
    missing = list(e for e in range(K + 1) if not present[e])
    heapq.heapify(missing)

    # Update rest of the elements using sliding window:
    for i in range(K, N):
        M.append(heapq.heappop(missing))
        present[M[i]] += 1
        present[M[i - K]] -= 1
        if not present[M[i - K]]:
            heapq.heappush(missing, M[i - K])

    print('Case #{}: {}'.format(case, M[N - 1]))
'''def c85(n=78,k=51,a=3,b=5,c=5,r=51230):
    m = []
    m.append(a)
    for i in range(1,k):
        m.append((b * m[i-1] + c) % r)
    m = sorted(m)
    nk = n - k
    db = []
    #0 is the lowest non-negative value to start with...
    for i in range(0,n):
        if not i in m:
            db.append(i)
            nk-=1
        if nk == 0:
            print(db, i)
            break
    return i
'''
