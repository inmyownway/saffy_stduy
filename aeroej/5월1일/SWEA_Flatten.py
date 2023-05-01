for test_case in range(1, 11):
  n = int(input())
  dump = sorted(list(map(int, input().split())))

  for _ in range(n):
    if dump[-1] - dump[0] <= 1:
        break
        
    dump[0], dump[-1] = dump[0]+1, dump[-1]-1
    dump = sorted(dump)
      
  ans = dump[-1] - dump[0]
  print('#{0} {1}'.format(test_case, ans))
