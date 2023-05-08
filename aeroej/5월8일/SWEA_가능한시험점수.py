t = int(input())

for test_case in range(1, t+1):
  n = int(input())
  point = list(map(int, input().split()))
  #중복을 허용하지 않으므로 set 사용
  score = set([0])

  for x in point:
    new_score = set()
    
    for y in score:
      #가능한 시험점수와 새로운 배점의 합
      new_score.add(x + y)
    
    score = score.union(new_score)
    
  ans = len(score)
  print('#{} {}'.format(test_case, ans))
  

  
