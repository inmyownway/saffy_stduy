from collections import defaultdict
visited = defaultdict(int)

def dfs(board, cnt):
  global ans
  if cnt == 0:
    return
  
  for i in range(l-1):
    for j in range(i+1, l):
      board[i], board[j] = board[j], board[i]
      new_num = int(''.join(board))
      
      #현재 교환 횟수가 더 많이 남아있는 경우
      if visited[new_num] < cnt:
        visited[new_num] = cnt

        if cnt%2 == 0:
          #일의 자리와 십의 자리 교환
          new_num = new_num//100*100 + new_num%10*10 + new_num//10%10
        
        ans = max(ans, new_num)
        dfs(board, cnt-1)
        
      board[i], board[j] = board[j], board[i]
      
      
t = int(input())

for test_case in range(1, t+1):
  n, m = input().split()
  l = len(n)
  m = int(m)

  init_board = [_ for _ in n]
  ans = 0
  
  dfs(init_board, m)
  print('#{0} {1}'.format(test_case,ans))

