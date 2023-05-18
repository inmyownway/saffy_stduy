def find(x):
    if p[x] < 0:
        return x

    p[x] = find(p[x])
    return p[x]


def union(x, y):
    if p[x] < p[y]:  # p[x]의 절대값이 더 크므로 y를 x로 병합
        p[x] += p[y]
        p[y] = x
    else:
        p[y] += p[x]
        p[x] = y


t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    # 양수 : 루트노드, 음수 : 루트노드이며 집합원소의 개수
    p = [-1] * (n + 1)
    result = ''

    for _ in range(m):
        c, a, b = map(int, input().split())
        a, b = find(a), find(b)

        if c == 0:
            if a != b:
                union(a, b)

        elif c == 1:
            if a == b:
                result += '1'
            else:
                result += '0'

    print('#{} {}'.format(test_case, result))
