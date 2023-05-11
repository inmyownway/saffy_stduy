def bfs():
    global room_num
    global cnt
 
    temp = [[q,w]]
 
    temp_cnt = 1
    temp_num = room[q][w]
 
    while len(temp):
        i,j = temp.pop(0)
 
        for e in range(4):
            ii = i + x[e]
            jj = j + y[e]
 
            if 0 <= ii < n and 0 <= jj < n:
                if room[ii][jj] - room[i][j] == 1:
                    temp.append([ii,jj])
                    temp_cnt += 1
                    break
 
    if temp_cnt > cnt:
        cnt = temp_cnt
        room_num = temp_num
 
    elif temp_cnt == cnt:
        if room_num > temp_num:
            room_num = temp_num
 
    return
 
T = int(input())
 
x = [-1,1,0,0]
y = [0,0,-1,1]
 
for tc in range(1,1+T):
 
    # 방의 크기 n*n
    n = int(input())
 
    room = [list(map(int,input().split())) for _ in range(n)]
 
    room_num = 0
    cnt = 0
 
    for q in range(n):
        for w in range(n):
            if cnt < n*n-room[q][w]+1:
                bfs()
 
    print('#{} {} {}'.format(tc,room_num,cnt))
