def dfs(num, idx):
    global result

    if idx >= n:
        if num == k:
            result += 1
        return

    # idx번째 수를 선택하는 경우
    dfs(num + seq[idx], idx + 1)
    # 그렇지 않은 경우
    dfs(num, idx + 1)


t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))

    result = 0
    dfs(0, 0)
    print('#{} {}'.format(test_case, result))
    
