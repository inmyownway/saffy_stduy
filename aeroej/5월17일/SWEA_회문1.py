for test_case in range(1, 11):
    n = int(input())
    graph = [input() for _ in range(8)]
    cnt = 0
    
    # 가로로 이어진 회문 탐색
    for i in range(8):
        q = []
        for j in range(8):
            q.append(graph[i][j])
            if len(q) == n:
                if q == q[::-1]:
                    cnt += 1
                q.pop(0)
                
    # 세로로 이어진 회문 탐색
    for j in range(8):
        q = []
        for i in range(8):
            q.append(graph[i][j])
            if len(q) == n:
                if q == q[::-1]:
                    cnt += 1
                q.pop(0)

    print('#{} {}'.format(test_case, cnt))
