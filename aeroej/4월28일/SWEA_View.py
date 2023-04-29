for tc in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    res = 0
    
    #n개의 건물 탐색
    for i in range(2, n-2):
        view = 255
        
        #좌우로 2개씩 다른 건물과의 높이 차이 연산
        for j in [-1, -2, 1, 2]:
            diff = building[i] - building[i+j]
            view = min(view, diff)
            
        #view가 0보다 작거나 같은 경우, 조망권 확보 실패
        if view > 0: 
            res += view

    print('#{0} {1}'.format(tc, res))
