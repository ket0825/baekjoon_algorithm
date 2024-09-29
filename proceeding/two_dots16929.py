"""
Two Dots
시간 제한	메모리 제한	제출
2 초	512 MB

입력
첫째 줄에 게임판의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에 게임판의 상태가 주어진다. 게임판은 모두 점으로 가득차 있고, 게임판의 상태는 점의 색을 의미한다. 점의 색은 알파벳 대문자 한 글자이다.

출력
사이클이 존재하는 경우에는 "Yes", 없는 경우에는 "No"를 출력한다.

제한
2 ≤ N, M ≤ 50

예제 입력 1 
3 4
AAAA
ABCA
AAAA
예제 출력 1 
Yes
예제 입력 2 
3 4
AAAA
ABCA
AADA
예제 출력 2 
No
예제 입력 3 
4 4
YYYR
BYBY
BBBY
BBBY
예제 출력 3 
Yes
예제 입력 4 
7 6
AAAAAB
ABBBAB
ABAAAB
ABABBB
ABAAAB
ABBBAB
AAAAAB
예제 출력 4 
Yes
예제 입력 5 
2 13
ABCDEFGHIJKLM
NOPQRSTUVWXYZ
예제 출력 5 
No

"""
import time
import sys
input = sys.stdin.readline


def sol():
    N, M = map(int, input().split()) # 2 ≤ N, M ≤ 50
        
    mat = [input() for _ in range(N)]
    visited = [[False] *M for _ in range(N)]
    
    # dfs로 풀자.            
    def get_possible_next(
        color:str, row:int, col:int,
        prev_move: tuple[int, int] | None # or None (for cycle check)
        ) -> list[tuple[int, int, tuple]]:
        possible_positions = []
        dy_list = [0, 0, -1, 1]
        dx_list = [-1, 1, 0, 0]        
        for dy, dx in zip(dy_list, dx_list):            
            n_row = row + dy
            n_col = col + dx
                        
            if prev_move == (-dy, -dx): # for cycle check
                # print(f"same position: {prev_move}")
                continue
            if (
                0 <= n_col < M # possible range
                and 0 <= n_row < N # possible range
                and mat[n_row][n_col] == color # same_color
                ):                
                
                possible_positions.append((n_row, n_col, (dy, dx)))
        # print(f"possible_positions: {possible_positions}")
        return possible_positions 
                
    # cycle -> 같은 색깔로 이루어진 list 속에서 전에 왔던 방향을 제외하고 움직였는데, 
    # 이미 방문했던 것이라면 cycle이다!        
    def dfs() -> bool:
        for i in range(N):
            for j in range(M):
                if not visited[i][j]:                    
                    cycle = []
                    stack = [(i, j, None)]
                    while stack:
                        row, col, prev_move = stack.pop() 
                        # time.sleep(3)
                        cycle.append((row, col))
                        # print(f"cycle: {cycle}")
                        possible_positions = get_possible_next(mat[row][col], row, col, prev_move) 
                        
                        for possible_pos in possible_positions:                                                                                    
                            if possible_pos[0:2] in cycle:
                                # print(f"possible_pos: {possible_pos}")        
                                # print(f"cycle: {cycle}")
                                return True
                            
                        stack.extend(possible_positions)
                    
                    # visited check
                    for visited_pos in cycle:
                        r, c = visited_pos
                        visited[r][c] = True                                
        
        return False                

    is_cycle = dfs()       
    if is_cycle:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    sol()
    
"""
출처: chrishyunbok.	visited는 루프가 나오는 곳에서만 시작. 두 번 방문한다면 ok. 
단점: b와 같은 형태의 첫 말단부에서는 안되는 것으로 간주.반드시 2방향이상 open되어있는 곳에서 시작하여야만 loop를 찾을 수 있음.
2차원 배열 visited를 여러 번 생성해야 함.
def dfs(jump,c,ni,nj,v):
    global check
    if check:
        return
    for nx, ny in ((ni + 1, nj), (ni, nj + 1), (ni - 1, nj), (ni, nj - 1)):
        if 0 <= nx < N and 0 <= ny < M and v[nx][ny]==2:
            if jump>=4:
                check = True
            return
        elif 0 <= nx < N and 0 <= ny < M and v[nx][ny] == 0 and arr[nx][ny] == c:
            v[nx][ny]^=1
            dfs(jump+1,c,nx,ny,v)
from sys import stdin
input = stdin.readline
N,M = map(int,input().split())
arr = list(input().rstrip() for _ in range(N))
check = False
for i in range(N):
    for j in range(M):
        cnt = 0
        for x,y in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
            if 0<=x<N and 0<=y<M and arr[i][j]==arr[x][y]:
                cnt+=1
        if cnt>=2:
            visited =[[0]*M for _ in range(N)]
            visited[i][j]=2
            dfs(1,arr[i][j],i,j,visited)
            if check:
                break
    if check:
        break
print("Yes" if check else "No")
"""


"""
출처:	krw8732
인접한 거리 차이가 1이라는 것을 count가 3이상이고, 인접한 거리 차이가 1이면 된다는 것으로
루프를 확인함.
    
n, m = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(list(input()))

# n, m = 4, 4
# lst = [
#     ['Y', 'Y', 'Y', 'R'],
#     ['B', 'Y', 'B', 'Y'],
#     ['B', 'B', 'B', 'Y'],
#     ['B', 'B', 'B', 'Y']
# ]

d = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, c):
    d[x][y] = 1 
    start_lst.append((x, y, c))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and lst[x][y] == lst[nx][ny]:
            if d[nx][ny] == 0:
                dfs(nx, ny, c+1)
def check():
    N = len(start_lst)
    if N < 4:
        return
    for i in range(N):
        for j in range(i+1, N):
            if abs(start_lst[j][2] - start_lst[i][2]) >= 3:
                if abs(start_lst[i][0] - start_lst[j][0]) + abs(start_lst[i][1] - start_lst[j][1]) == 1: # 인접해있다. (3이상 거리 차이 나면서 x, y 거리차이 1이면...)
                    return True
    return False

for i in range(n):
    for j in range(m):
        if d[i][j] == 0:
            start_lst = []
            dfs(i, j, 0)
            if check():
                print('Yes')
                exit()
print('No')
"""