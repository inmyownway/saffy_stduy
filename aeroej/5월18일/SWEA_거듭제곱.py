def recursion(cnt):
    if cnt == 0:
        return 1
    return recursion(cnt-1) * n


for _ in range(10):
    test_case = int(input())
    n, m = map(int, input().split())
    print('#{} {}'.format(test_case, recursion(m)))
