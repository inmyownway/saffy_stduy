from collections import deque

for _ in range(10):
  test_case = int(input())
  pw = deque(list(map(int, input().split())))

  #다섯 번의 사이클 * n회 수행한 나머지 구하기
  five_times = min(pw) // 15
  if five_times > 0:
    
    if min(pw) % 15 == 0:
      five_times -= 1
      
    for idx in range(8):
      pw[idx] = pw[idx] % (five_times * 15)  

  #한 사이클씩 수행
  number = deque([1, 2, 3, 4, 5])
  while True:
    x = pw.popleft()
    y = number.popleft()

    if (x - y) <= 0:
      pw.append(0)
      break

    pw.append(x-y)
    number.append(y)

  print('#{}'.format(test_case), *pw)
    
