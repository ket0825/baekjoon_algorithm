"""
크기가 N×M인 격자판의 각 칸에 정수가 하나씩 들어있다. 이 격자판에서 칸 K개를 선택할 것이고, 선택한 칸에 들어있는 수를 모두 더한 값의 최댓값을 구하려고 한다. 단, 선택한 두 칸이 인접하면 안된다. r행 c열에 있는 칸을 (r, c)라고 했을 때, (r-1, c), (r+1, c), (r, c-1), (r, c+1)에 있는 칸이 인접한 칸이다.

입력
첫째 줄에 N, M, K가 주어진다. 둘째 줄부터 N개의 줄에 격자판에 들어있는 수가 주어진다.

출력
선택한 칸에 들어있는 수를    모두 더한 값의 최댓값을 출력한다.

제한
1 ≤ N, M ≤ 10  (최대 10 * 10)
1 ≤ K ≤ min(4, N×M) (최대 4임)
격자판에 들어있는 수는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

항상 K개의 칸을 선택할 수 있는 경우만 입력으로 주어진다.
"""


import sys
input = sys.stdin.readline
answer = -100000

def main():
    N, M, K = map(int, input().rstrip().split(" "))
    board = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]

    visited = [[0]*M for _ in range(N)]

    def dfs(row_base:int, visit_count:int, sum:int):
        global answer
        if visit_count == K:
            # board_sum = sum([board[row][col] if visited[row][col] == 1 else 0 
            #                  for row in range(N) 
            #                  for col in range(M)])
            print("===========")       
            [print(f"row: {row}, col: {col}") if visited[row][col] == 1 else 0 
                             for row in range(N) 
                             for col in range(M)]
            
            # print(f"board_sum: {board_sum}")
            answer = max(answer, sum)
            print(f"sum:{sum}")
            # answer = max(answer, board_sum)
            return
        
        for row in range(row_base, N):
            for col in range(M):
                if visited[0][0] == 1 and visited[0][2] == 1 and col == 1 and row == 1:
                    print("")

                if visited[row][col] == 1:
                    continue

                try:
                    left_adjacent = (visited[row][col-1] == 1)
                except:
                    left_adjacent = False
                try:
                    right_adjacent = (visited[row][col+1] == 1)
                except:
                    right_adjacent = False
                try:
                    upward_adjacent = (visited[row+1][col] == 1)
                except:
                    upward_adjacent = False
                try:
                    downward_adjacent = (visited[row-1][col] == 1)
                except:
                    downward_adjacent = False
                
                is_adjacent = (left_adjacent or right_adjacent or upward_adjacent or downward_adjacent)
                


                if not is_adjacent:
                    visited[row][col] = 1
                    if col < M:  # col이 증가하는 경우.
                        dfs(row, visit_count+1, sum+board[row][col])
                    elif col == M and row_base < N: # row 증가하는 경우.
                        dfs(row+1, visit_count+1, sum+board[row][col])

                    visited[row][col] = 0

    dfs(0, 0, 0)
    print(answer)


if __name__ == "__main__":
    main()

## 2. ok를 False로 만드는 알고리즘을 참고하자.
## 하나씩 더하고, 빼고를 반복하며 불가능 여부를 체크함.
    
# n, m, k = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# c = [[False] * m for _ in range(n)]
# ans = -2147483647
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def go(px, py, cnt, s):
#     if cnt == k:
#         global ans
#         if ans < s:
#             ans = s
#         return
#     for x in range(px, n):
#         for y in range(py if x == px else 0, m):
#             if c[x][y]:
#                 continue
#             ok = True
#             for i in range(4):
#                 nx, ny = x + dx[i], y + dy[i]
#                 if 0 <= nx < n and 0 <= ny < m:
#                     if c[nx][ny]:
#                         ok = False
#             if ok:
#                 c[x][y] = True
#                 go(x, y, cnt + 1, s + a[x][y])
#                 c[x][y] = False
# go(0, 0, 0, 0)
# print(ans)
    
## 3. 비트 연산 및 해공간을 만들어서 확장시킴 (어려움 주의!)
# N, M, K = map(int, input().split())

# dp = [[[-(10 ** 6) for _ in range(K + 1)] for _ in range(1 << M)] for _ in range(N + 1)]
# for i in range(1 << M):
#     dp[0][i][0] = 0

# adj = [0 for _ in range(1 << M)]
# for i in range(1 << M):
#     if '11' in bin(i)[2:]:
#         adj[i] = -1
#     else:
#         adj[i] = bin(i)[2:].count('1')
# p = [i for i in range(1 << M) if adj[i] >= 0]

# grid = []
# for _ in range(N):
#     grid.append([*map(int, input().split())])

# for a in range(1, N + 1):
#     part_sum = [0 for _ in range(1 << M)]
#     for x in p:
#         p_sum = 0
#         for y in range(M):
#             if x & (1 << y) != 0:
#                 p_sum += grid[a - 1][y]
#         part_sum[x] = p_sum
#     for b in p:
#         for c in p:
#             if b & c == 0:
#                 for d in range(K - adj[c] + 1):
#                     dp[a][c][d + adj[c]] = max(dp[a][c][d + adj[c]], dp[a - 1][b][d] + part_sum[c])

# res = -(10 ** 6)
# for i in range(1 << M):
#     res = max(res, dp[N][i][K])
# print(res)