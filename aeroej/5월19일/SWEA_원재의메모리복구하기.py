t = int(input())

for test_case in range(1, t+1):
    data = list(map(int, input()))

    cnt = 0
    bit = -1

    # 역방향 탐색
    for i in range(len(data) - 1, -1, -1):
        if bit != data[i]:
            bit = data[i]
            cnt += 1

    if bit == 0:
        cnt -= 1

    print('#{} {}'.format(test_case, cnt))
