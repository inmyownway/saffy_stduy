t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    p = int(input())
    station = [int(input()) for _ in range(p)]
    result = [0]*p

    for a, b in graph:
        for c in range(p):
            if a <= station[c] <= b:
                result[c] += 1

    print('#{}'.format(test_case), *result)
    
