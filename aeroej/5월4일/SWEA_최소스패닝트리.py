#Kruskal's algorithm을 이용할 경우, Disjoint Set(서로소 집합) 혹은 Union-Find 알고리즘을 이용해야 한다.

def find(x):
  if p[x] < 0:  #x가 루트노드
    return x

  p[x] = find(p[x])  #x의 최종 루트노드 탐색
  return p[x]


def union(x, y):
  if p[y] < p[x]:  #y의 집합의 개수(음수)가 더 많은 경우, y를 루트노드로 설정
    p[y] += p[x]  #y가 x의 집합을 merge
    p[x] = y  #x의 루트노드는 y
  else:
    p[x] += p[y]  
    p[y] = x  


t = int(input())

for test_case in range(1, t+1):
  #p[x]가 양수: x의 루트노드는 y라는 뜻. 정점 y
  #p[x]가 음수: x가 루트노드라는 뜻. -(집합의 개수)
  v, e = map(int, input().split())
  p = [-1 for _ in range(v+1)]  
  
  #가중치 x[2]를 기준으로 오름차순 정렬
  graph = [list(map(int, input().split())) for _ in range(e)]
  graph.sort(key = lambda x: (x[2], x[0], x[1]))  
  weight = 0
  
  for a, b, c in graph:
    a = find(a)
    b = find(b)
    
    if a != b:  #a와 b의 루트노드가 다름. 즉 a와 b가 연결되지 않은 상태
      weight += c
      union(a, b)
  
  print('#{} {}'.format(test_case, weight))
  
  
