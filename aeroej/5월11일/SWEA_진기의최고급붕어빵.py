T = int(input())
 
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = sorted(list(map(int, input().split())))
    result = 'Possible'
    
    # 해당시간 만들 수 있는 빵의 최대 갯수
    # 팔린 빵의 갯수
    sold_bread = 0
    for customer in customers:
        # 손님이 도착한 시간에 최대로 만들 수 있는 빵의 갯수
        made_bread = (customer // M) * K
         
        # 남은 빵의 갯수
        remain = made_bread - sold_bread
         
        if remain <= 0:
            result = 'Impossible'
            break
        else:
            sold_bread += 1
 
    print('#{} {}'.format(tc, result))
