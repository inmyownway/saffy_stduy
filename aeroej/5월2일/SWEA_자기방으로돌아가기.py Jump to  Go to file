t = int(input())
for test_case in range(1, t + 1 ):
    n = int(input())
    visited = [0] * 401
    
    for _ in range(n):
        x, y = map(int, input().split())
        if x > y: 
            x, y = y, x
            
        x = (x + 1) // 2
        y = (y + 1) // 2
        
        for i in range(x, y+1):
            visited[i] += 1
            
    ans = max(visited)
    print('#{0} {1}'.format(test_case, ans))
