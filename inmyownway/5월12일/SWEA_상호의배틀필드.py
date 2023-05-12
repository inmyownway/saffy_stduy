test_case=int(input())




for tc in range(1,test_case+1):
    n,m=map(int,input().split())
    game=[]
    for i in range(n):
        t=list(input())
        game.append(t)

    c=int(input())
    command=input()

    commands=list(command)
    #print(commands)

    dir=""
    for i in range(n):
        for j in range(m):
            if game[i][j]=="<" or game[i][j]==">" or game[i][j]=="v" or game[i][j]=="^":
                dir=game[i][j]
                cx=i
                cy=j
    #print(cx,cy,dir)

    if dir=='<':
        dir="L"
    elif dir=='>':
        dir="R"
    elif dir=="v":
        dir="D"
    elif dir=="^":
        dir="U"
    #print(cx,cy,dir)

    for command in commands:
        #print(command,cx,cy,dir)
        #print(command)
        if command=="U":
            if cx-1>=0:
                if game[cx-1][cy]==".":
                    game[cx][cy]='.'
                    game[cx-1][cy]="^"
                    cx-=1
                    dir="U"
                else:
                    game[cx][cy] = "^"
                    dir="U"

        elif command=="D":
            if cx+1<n:
                if game[cx+1][cy]==".":
                    game[cx][cy] = '.'
                    game[cx+1][cy] = "v"
                    cx+=1
                    dir="D"
                else:
                    game[cx][cy] = "v"
                    dir="D"

        elif command=='L':
            if cy-1>=0:
                if game[cx][cy-1]==".":
                    game[cx][cy] = '.'
                    game[cx][cy-1] = "<"
                    cy-=1
                    dir="L"
                else:
                    game[cx][cy] = "<"
                    dir="L"


        elif command=="R":
            if cy+1<m:
                if game[cx][cy+1]==".":
                    game[cx][cy] = '.'
                    game[cx][cy + 1] = ">"
                    cy+=1
                    dir="R"
                else:
                    game[cx][cy] = ">"
                    dir="R"
        elif command=="S":
            if dir=='U':
                sx=cx
                while True:
                    if sx-1 >=-1:
                        if game[sx][cy]=="*":
                            game[sx][cy]="."
                            break
                        elif game[sx][cy]=="#":
                            break
                    elif sx-1 < -1:
                        break
                    sx-=1
            elif dir=='D':
                sx=cx
                while True:
                    if sx+1 <=n:
                        if game[sx][cy]=="*":
                            game[sx][cy]="."
                            break
                        elif game[sx][cy]=="#":
                            break
                    elif sx+1>n:
                        break
                    sx+=1
            elif dir=='L':
                sy=cy
                while True:
                    if sy-1 >= -1 :
                        if game[cx][sy]=="*":
                            game[cx][sy]="."
                            break
                        elif game[cx][sy]=="#":
                            break
                    elif sy-1< -1:
                        break
                    sy-=1
            elif dir == 'R':
                sy = cy
                while True:
                    if sy +1 <=m:
                        if game[cx][sy] == "*":
                            game[cx][sy] = "."
                            break
                        elif game[cx][sy] == "#":
                            break
                    elif sy + 1 >m :
                        break
                    sy += 1
        #print(cx,cy,dir)
        # for i in game:
        #     print(i)
        # print()
    print("#%d"%(tc),end=' ')
    for i in game:
        print(''.join(i))
