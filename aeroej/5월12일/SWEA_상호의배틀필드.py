

T = int(input())

for test_case in range(1, T + 1):
    H , W = map(int, input().split())
    map_list = [['' for _ in range(W)] for _ in range(H)]
    for i in range(H):
        map_list[i] = list(input())
    for i in range(H):
        for j in range(W):
            if map_list[i][j] =='<' or map_list[i][j] =='^' or map_list[i][j] == 'v' or map_list[i][j] == '>':
                a, b = i,j
                break
    N = int(input())
    cmd_line = list(input())
    for cmd in cmd_line:
        if cmd =='S':
            if b<W and map_list[a][b] == '>':
                for i in range(b+1, W):
                    if map_list[a][i] == '#':
                        break
                    else: 
                        if map_list[a][i] =='*':
                            map_list[a][i] = '.'
                            break
            elif b>0 and map_list[a][b] == '<':
                for i in range(b-1,-1,-1):
                    if map_list[a][i] == '#':
                        break
                    else:
                        if map_list[a][i] =='*':
                            map_list[a][i] = '.'
                            break
            elif a>0 and map_list[a][b] == '^':
                for i in range(a-1,-1,-1):
                    if map_list[i][b] == '#':
                        break
                    else:
                        if map_list[i][b] =='*':
                            map_list[i][b] = '.'
                            break
            elif a<H and map_list[a][b] =='v' :
                for i in range(a+1, H):
                    if map_list[i][b] == '#':
                        break
                    else:
                        if map_list[i][b] =='*':
                            map_list[i][b] = '.'
                            break
        elif cmd == 'U':
            map_list[a][b] ='^'
            if a>0 and map_list[a-1][b] =='.':
                map_list[a][b] = '.'
                map_list[a-1][b] = '^'
                a=a-1
        elif cmd == 'D':
            map_list[a][b] ='v'
            if a<H-1 and map_list[a+1][b] =='.':
                map_list[a][b] = '.'
                map_list[a+1][b] = 'v'
                a= a+1
        elif cmd == 'L':
            map_list[a][b] ='<'
            if b>0 and map_list[a][b-1] =='.':
                map_list[a][b] = '.'
                map_list[a][b-1] = '<'
                b= b-1
        else:
            map_list[a][b] ='>'
            if b<W-1 and map_list[a][b+1] =='.':
                map_list[a][b] = '.'
                map_list[a][b+1] = '>'
                b = b+1

    print(f'#{test_case}', end = ' ')
    for i in range(H):
        for j in range(W):
            print(map_list[i][j], end = '')
        print()
