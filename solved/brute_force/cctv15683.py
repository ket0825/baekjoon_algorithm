"""
감시
시간 제한	메모리 제한
1 초	512 MB
문제
스타트링크의 사무실은 1×1크기의 정사각형으로 나누어져 있는 N×M 크기의 직사각형으로 나타낼 수 있다. 사무실에는 총 K개의 CCTV가 설치되어져 있는데, CCTV는 5가지 종류가 있다. 각 CCTV가 감시할 수 있는 방법은 다음과 같다.

				
1번	2번	3번	4번	5번
1번 CCTV는 한 쪽 방향만 감시할 수 있다. 2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고, 3번은 직각 방향이어야 한다. 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.

CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다. 사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다. CCTV가 감시할 수 없는 영역은 사각지대라고 한다.

CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며, 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.

0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호이다. 위의 예시에서 1번의 방향에 따라 감시할 수 있는 영역을 '#'로 나타내면 아래와 같다.

0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 # 6 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
# # 1 0 6 0
0 0 0 0 0 0
0 0 # 0 0 0
0 0 # 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 # 0 0 0
→	←	↑	↓
CCTV는 벽을 통과할 수 없기 때문에, 1번이 → 방향을 감시하고 있을 때는 6의 오른쪽에 있는 칸을 감시할 수 없다.

0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
위의 예시에서 감시할 수 있는 방향을 알아보면 아래와 같다.

0 0 0 0 0 #
# 2 # # # #
0 0 0 0 6 #
0 6 # # 2 #
0 0 0 0 0 #
# # # # # 5
0 0 0 0 0 #
# 2 # # # #
0 0 0 0 6 #
0 6 0 0 2 #
0 0 0 0 # #
# # # # # 5
0 # 0 0 0 #
0 2 0 0 0 #
0 # 0 0 6 #
0 6 # # 2 #
0 0 0 0 0 #
# # # # # 5
0 # 0 0 0 #
0 2 0 0 0 #
0 # 0 0 6 #
0 6 0 0 2 #
0 0 0 0 # #
# # # # # 5
왼쪽 상단 2: ↔, 오른쪽 하단 2: ↔	왼쪽 상단 2: ↔, 오른쪽 하단 2: ↕	왼쪽 상단 2: ↕, 오른쪽 하단 2: ↔	왼쪽 상단 2: ↕, 오른쪽 하단 2: ↕
CCTV는 CCTV를 통과할 수 있다. 아래 예시를 보자.

0 0 2 0 3
0 6 0 0 0
0 0 6 6 0
0 0 0 0 0
위와 같은 경우에 2의 방향이 ↕ 3의 방향이 ←와 ↓인 경우 감시받는 영역은 다음과 같다.

# # 2 # 3
0 6 # 0 #
0 0 6 6 #
0 0 0 0 #
사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 

CCTV의 최대 개수는 8개를 넘지 않는다.

출력
첫째 줄에 사각 지대의 최소 크기를 출력한다.

예제 입력 1 
4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
예제 출력 1 
20
예제 입력 2 
6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
예제 출력 2 
15
예제 입력 3 
6 6
1 0 0 0 0 0
0 1 0 0 0 0
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 0 0 0 1
예제 출력 3 
6
예제 입력 4 
6 6
1 0 0 0 0 0
0 1 0 0 0 0
0 0 1 5 0 0
0 0 5 1 0 0
0 0 0 0 1 0
0 0 0 0 0 1
예제 출력 4 
2
예제 입력 5 
1 7
0 1 2 3 4 5 6
예제 출력 5 
0
예제 입력 6 
3 7
4 0 0 0 0 0 0
0 0 0 2 0 0 0
0 0 0 0 0 0 4
예제 출력 6 
0

"""

# 핵심. 어떤 것으로 되돌릴 지 알아야 함. 여기서는 변경한 것을 진행. 상태 자체로 되돌리려면 흠... 


import sys
input = sys.stdin.readline

def sol(N, M, board):
    area = 0
    cctvs = [] # type
    cctv_loc = [] # locations. [r, c]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                area+=1
            elif board[i][j] == 6:
                continue
            else:
                cctvs.append(board[i][j])
                cctv_loc.append([i, j])
    
    cctv_cases = [[], [1,2,3,4], [1,2], [1,2,3,4], [1,2,3,4], [1]]
    
    cctv_all = [] # [1, 1, 1, 1, 1], [1, 1, 1, 1, 2], ... 5개인 경우.
    CCTV_COUNT = len(cctvs)
    
    def make_all_cases(cnt, cctv_case):
        if cnt == CCTV_COUNT:
            cctv_all.append(cctv_case.copy())
            return
                
        cctv_type = cctvs[cnt]
        for d in cctv_cases[cctv_type]:
            cctv_case.append(d)
            make_all_cases(cnt+1, cctv_case)
            cctv_case.pop()
    
    make_all_cases(0, [])
    
    def cctv_coloring(board, cctv_type, d, cctv_rc):
        reset_coord = []
        r,c = cctv_rc          
        if cctv_type == 1:
            if d == 1: # 왼, 위, 오, 하                
                for j in range(c-1, -1, -1):
                    if not 0 <= j < M:
                        continue
                    if board[r][j] == 6:
                        break
                    if board[r][j] == 0:
                        board[r][j] = -1
                        reset_coord.append((r, j))                                
            elif d == 2:
                for i in range(r-1, -1, -1):
                    if not 0 <= i < N:
                        continue
                    if board[i][c] == 6:
                        break
                    if board[i][c] == 0:
                        board[i][c] = -1
                        reset_coord.append((i, c))                       
            elif d == 3:
                for j in range(c+1, M):
                    if not 0 <= j < M:
                        continue                    
                    if board[r][j] == 6:
                        break                           
                    if board[r][j] == 0:             
                        board[r][j] = -1
                        reset_coord.append((r, j))
            elif d == 4:
                for i in range(r+1, N):
                    if not 0 <= i < N:
                        continue
                    if board[i][c] == 6:
                        break
                    if board[i][c] == 0:
                        board[i][c] = -1
                        reset_coord.append((i, c))            
        elif cctv_type == 2:
            if d == 1:
                reset_coord = cctv_coloring(board, 1, 1, cctv_rc) + cctv_coloring(board, 1, 3, cctv_rc)
            elif d == 2:
                reset_coord = cctv_coloring(board, 1, 2, cctv_rc) + cctv_coloring(board, 1, 4, cctv_rc)
            
        elif cctv_type == 3:
            if d == 1:
                reset_coord = cctv_coloring(board, 1, 1, cctv_rc) + cctv_coloring(board, 1, 2, cctv_rc)
            elif d == 2:
                reset_coord = cctv_coloring(board, 1, 2, cctv_rc) + cctv_coloring(board, 1, 3, cctv_rc)
            elif d == 3:
                reset_coord = cctv_coloring(board, 1, 3, cctv_rc) + cctv_coloring(board, 1, 4, cctv_rc)
            elif d == 4:
                reset_coord = cctv_coloring(board, 1, 4, cctv_rc) + cctv_coloring(board, 1, 1, cctv_rc)
        elif cctv_type == 4:
            if d == 1:
                reset_coord = cctv_coloring(board, 1, 1, cctv_rc) + cctv_coloring(board, 1, 2, cctv_rc) + cctv_coloring(board, 1, 3, cctv_rc)            
            elif d == 2:
                reset_coord = cctv_coloring(board, 1, 2, cctv_rc) + cctv_coloring(board, 1, 3, cctv_rc) + cctv_coloring(board, 1, 4, cctv_rc)                
            elif d == 3:
                reset_coord = cctv_coloring(board, 1, 3, cctv_rc) + cctv_coloring(board, 1, 4, cctv_rc) + cctv_coloring(board, 1, 1, cctv_rc)                
            elif d == 4:
                reset_coord = cctv_coloring(board, 1, 4, cctv_rc) + cctv_coloring(board, 1, 1, cctv_rc) + cctv_coloring(board, 1, 2, cctv_rc)
        elif cctv_type == 5:
            reset_coord = cctv_coloring(board, 1, 1, cctv_rc) + cctv_coloring(board, 1, 2, cctv_rc) + cctv_coloring(board, 1, 3, cctv_rc) + cctv_coloring(board, 1, 4, cctv_rc)
        return reset_coord

    answer = area
    for cctv_case in cctv_all:
        reset_pos = []
        removed = area
        for i in range(CCTV_COUNT):
            d = cctv_case[i] # directions
            cctv_type = cctvs[i] # cctv 타입
            cctv_rc = cctv_loc[i] # cctv 위치
            # 되돌릴 위치 추가            
            for pos in cctv_coloring(board, cctv_type, d, cctv_rc):
                reset_pos.append(pos)                
            
        # 위치를 통해 되돌리기
        for pos in reset_pos:
            board[pos[0]][pos[1]] = 0
            removed -= 1                    
        # 사각지대 갱신        
        answer = min(answer, removed)
        if answer == 0:
            break
    
    print(answer)


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    board = [list(map(int, input().strip().split())) for _ in range(N)]
    # N, M = 8, 1
    # board = [[0], [6], [4], [6], [1], [0], [3], [4]]
    # N, M = 2, 2
    # board = [[0, 0], [0, 0]]
    sol(N, M, board)
    
"""
6 6
1 0 0 0 0 0
0 2 0 0 0 0
0 0 3 0 0 0
0 0 0 4 0 0
0 0 0 0 5 0
0 0 0 0 0 6

1 -1 -1 -1 -1 -1
-1 2 -1 -1 -1 -1
-1 -1 3 0 -1 0
-1 -1 -1 4 -1 -1
-1 -1 -1 -1 5 -1
0 0 -1 -1 -1 6
"""
3, 1, 4, 3, 1