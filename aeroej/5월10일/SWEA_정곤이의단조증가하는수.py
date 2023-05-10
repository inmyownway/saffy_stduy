def check(num):
  if num < 10:
    return 0
    
  k = str(num)
  for i in range(0, len(k)-1):
    if k[i] > k[i+1]:
      return 0
      
  return num


t = int(input())

for test_case in range(1, t+1):
  n = int(input())
  lst = list(map(int, input().split()))
  value = []
  
  for i in range(0, n):
    for j in range(0, n):
      
      if i < j:
        number = check(lst[i] * lst[j])
        
        if number:
          value.append(number)

  res = -1
  if len(value) > 0:
    res = max(value)
    
  print('#{} {}'.format(test_case, res))
