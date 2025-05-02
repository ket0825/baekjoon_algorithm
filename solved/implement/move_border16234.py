"""인구 이동
시간 제한	메모리 제한
2 초	512 MB

문제
N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 
각각의 땅에는 나라가 하나씩 존재하며,
r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 
인접한 나라 사이에는 국경선이 존재한다. 
모든 나라는 1×1 크기이기 때문에, 
모든 국경선은 정사각형 형태이다.

오늘부터 인구 이동이 시작되는 날이다.

인구 이동은 하루 동안 다음과 같이 진행되고, 
더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면,
두 나라가 공유하는 국경선을 오늘 하루 동안 연다.

위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 
그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 
(연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 


MARK: ****편의상 소수점은 버린다.****

연합을 해체하고, 
모든 국경선을 닫는다.
각 나라의 인구수가 주어졌을 때, 
인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)

둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. 
r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)

인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

출력
인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.

예제 입력 1 
2 20 50
50 30
20 40
예제 출력 1 
1
초기 상태는 아래와 같다.

L = 20, R = 50 이기 때문에, 모든 나라 사이의 국경선이 열린다. (열린 국경선은 점선으로 표시)



연합은 하나 존재하고, 연합의 인구는 (50 + 30 + 20 + 40) 이다. 연합의 크기가 4이기 때문에, 각 칸의 인구수는 140/4 = 35명이 되어야 한다. 



예제 입력 2 
2 40 50
50 30
20 40
예제 출력 2 
0
경계를 공유하는 나라의 인구 차이가 모두 L보다 작아서 인구 이동이 발생하지 않는다.

예제 입력 3 
2 20 50
50 30
30 40
예제 출력 3 
1"""

# 최대: N^2이면 500만... (이동 2000회 이하)

# 연합을 이루고 있는 각 칸의 인구수는 
# (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 
# 편의상 소수점은 버린다.

# BFS 미사용 및 그냥 merge 하는 방식 사용 
# (path compression abd disjoint set 공부 필요!)
# sum을 동시에 진행했으면 더욱 빨랐을 수도.

# import sys
# input = sys.stdin.readline

# def sol():
#     N, L, R = map(int, input().rstrip().split())    
#     mat = [list(map(int, input().rstrip().split()))for _ in range(N)]
    
#     move = 0
    
#     dr = [0, 1]
#     dc = [1, 0]
    
#     open_border = {}
    
#     def find_and_merge_root(a, b):
#         root_a = open_border[a][0]
#         root_b = open_border[b][0]
#         # 같은 root면 바로 종료
#         if root_a == root_b:            
#             return
        
#         if len(open_border[root_a]) > len(open_border[root_b]):
            
#             for tup in open_border[root_b]:
#                 if root_b == tup:
#                     continue
#                 open_border[tup] = [root_a] # 전부 root_a 소속으로 바꿈.
#                 open_border[root_a].append(tup)
#                 # print("---------",tup)
            
#             open_border[root_b] = [root_a]
#             open_border[root_a].append(root_b)
#             # print(f"root_a: {root_a}")
#             # print(f"root_b: {root_b}")
            
#         else:
#             for tup in open_border[root_a]:
#                 # print("a 길이:",len(open_border[root_a]))
#                 if tup == root_a:
#                     continue
#                 open_border[tup] = [root_b] # 전부 root_b 소속으로 바꿈.
#                 open_border[root_b].append(tup)
#                 # print("---------",tup)
#             open_border[root_a] = [root_b]     
#             open_border[root_b].append(root_a)
#             # print(f"root_a: {root_a}")
#             # print(f"root_b: {root_b}")
            
    
#     def is_open_border():
#         # visited = [[0]*N for _ in range(N)]
#         for r in range(N):            
#             for c in range(N):
#                 for ddr, ddc in zip(dr, dc):
#                     nr = r + ddr
#                     nc = c + ddc                    
#                     if 0 <= nr < N and 0 <= nc < N:
#                         can_open = L <= abs(mat[r][c] - mat[nr][nc]) <= R
#                         # print(f"r:{r}, c:{c}, nr:{nr} , nc: {nc}, can_open:{can_open}")
#                         if can_open:
#                             # 만약 r,c가 등록되어 있지 않으면...
#                             if not open_border.get((r,c)) and not open_border.get((nr,nc)):
#                                 # print(f"register nr,nc:{nr},{nc} -> r,c: {r},{c}")
#                                 # 자신 root에 등록                        
#                                 open_border[(r,c)] = [(r,c)] # 자기 자신 등록
#                                 open_border[(r,c)].append((nr,nc)) # 자기 자식 등록
#                                 # print("register open border complete")
#                                 # 자신 소속 설정
#                                 open_border[(nr,nc)] = [(r,c)]
#                                 # r,c가 이미 누군가의 소속
#                             elif open_border.get((r,c)) and open_border.get((nr,nc)):
#                                 # print("Both are 소속되어 있음")
#                                 find_and_merge_root((r,c),(nr,nc))
#                                 continue                                
#                             elif open_border.get((r,c)):
#                                 root_r, root_c = open_border[(r,c)][0] # open_border[(r,c)]는 [(루트r, 루트c)]
#                                 # print(f"find root: {root_r},{root_c}")
#                                 open_border[(root_r,root_c)].append((nr,nc))                            
#                                 open_border[(nr,nc)] = [(root_r,root_c)]                            
#                             elif open_border.get((nr,nc)):
#                                 root_r, root_c = open_border[(nr,nc)][0] # open_border[(r,c)]는 [(루트r, 루트c)]
#                                 # print(f"find root: {root_r},{root_c}")
#                                 open_border[(root_r,root_c)].append((r,c))                            
#                                 open_border[(r,c)] = [(root_r,root_c)]                                                                                                                                  
                        
#         # print(open_border)
#         if len(open_border) > 0:            
#             return True
#         else:
#             # print("No open border")
#             return False
                    
#     def move_border():
#         # check all border
#         for k, v in open_border.items():
#             if len(v) > 1:
#                 cnt = 0
#                 s = 0
#                 for r,c in v:
#                     s+=mat[r][c]
#                     cnt+=1
#                 avg = s // cnt
#                 for r,c in v:
#                     mat[r][c] = avg      
        
#     while is_open_border():
#         move_border()
#         open_border = {} # clear open_border
#         # print(f"mat: {mat}")
#         move+=1
#         # print(f"move: {move}")
    
#     print(move)

# sol()

## 일반 BFS로 풀어도 가능.
# 네 곳의 방향과 자신의 root를 queue로 계속 기억하고 있으면 가능.
### 그 외: visited로 지난 날을 기억하면서 풀기. 동일한 날이라면 integrate함.
# from sys import stdin
# input = stdin.readline

# def integrate(row, col, visited, date):
#     global L, R, population, neigh

#     queue = [(row, col)]
#     pivot = 0
#     q_len = 1
#     pop_tot = population[row][col]
#     visited[row][col] = date
#     while pivot < q_len:
#         r, c = queue[pivot]
#         for nr, nc in neigh[(r,c)]:
#             if (visited[nr][nc] < date) and (L <= abs(population[r][c] - population[nr][nc]) <= R):
#                 visited[nr][nc] = date
#                 queue.append((nr, nc))
#                 pop_tot += population[nr][nc]
#                 q_len += 1
#         pivot += 1
#     return queue, q_len, pop_tot

# def solve():
#     global population

#     queue = [(r, c) for c in range(N) for r in range(c%2, N, 2)]
#     visited = [[-1] * N for _ in range(N)]
#     for day in range(2000):
#         next_q = []
#         for r, c in queue:
#             if visited[r][c] < day:
#                 q, q_len, pop_tot = integrate(r, c, visited, day)
#                 if q_len > 1:
#                     avg = pop_tot//q_len
#                     next_q += q
#                     for x, y in q:
#                         population[x][y] = avg

#         if not next_q:
#             print(day)
#             break
#         else:
#             queue = next_q


# if __name__ == "__main__":
#     N, L, R = map(int, input().split())
#     population = [list(map(int, input().split())) for _ in range(N)]
#     neigh = {}
#     for r in range(N):
#         for c in range(N):
#             tmp = []
#             for nr, nc in [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]:
#                 if (0 <= nr < N) and (0 <= nc < N):
#                     tmp.append((nr, nc))
#             neigh[(r,c)] = tmp
#     solve()

# 내 새로운 풀이


