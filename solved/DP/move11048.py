"""
이동하기
시간 제한	메모리 제한	
1 초	256 MB
문제
준규는 N×M 크기의 미로에 갇혀있다. 
미로는 1×1크기의 방으로 나누어져 있고, 
각 방에는 사탕이 놓여져 있다. 
미로의 가장 왼쪽 윗 방은 (1, 1)이고, 가장 오른쪽 아랫 방은 (N, M)이다.

준규는 현재 (1, 1)에 있고, (N, M)으로 이동하려고 한다. 
준규가 (r, c)에 있으면, (r+1, c), (r, c+1), (r+1, c+1)로 이동할 수 있고, 
각 방을 방문할 때마다 방에 놓여져있는 사탕을 모두 가져갈 수 있다. 
또, 미로 밖으로 나갈 수는 없다.

준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값을 구하시오.

입력
첫째 줄에 미로의 크기 N, M이 주어진다. (1 ≤ N, M ≤ 1,000)

둘째 줄부터 N개 줄에는 총 M개의 숫자가 주어지며, 
r번째 줄의 c번째 수는 (r, c)에 놓여져 있는 사탕의 개수이다. 
사탕의 개수는 0보다 크거나 같고, 100보다 작거나 같다.

출력
첫째 줄에 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수를 출력한다.

예제 입력 1 
3 4
1 2 3 4
0 0 0 5
9 8 7 6
예제 출력 1 
31
예제 입력 2 
3 3
1 0 0
0 1 0
0 0 1
예제 출력 2 
3
예제 입력 3 
4 3
1 2 3
6 5 4
7 8 9
12 11 10
예제 출력 3 
47
"""

import sys
input = sys.stdin.readline

def sol():
    N, M = map(int, input().strip().split())
    candies = [list(map(int, input().strip().split())) for _ in range(N)]
    dps = [[0]* M for _ in range(N)]
    dr = [0,1,1]
    dc = [1,0,1]
    
    def check(r, c):        
        for i in range(3):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                dps[nr][nc] = max(dps[nr][nc], dps[r][c]+candies[nr][nc])

    dps[0][0] = candies[0][0]
    for i in range(N):
        for j in range(M):
            check(i,j)

    print(dps[N-1][M-1])        
    

if __name__ == '__main__':
    sol()


















# import sys
# input = sys.stdin.readline

# def sol1():
#     N, M = map(int, input().rstrip().split())# (1 ≤ N, M ≤ 1,000)
#     mat = []
#     drc = [(1, 0), (0, 1), (1, 1)]
#     for _ in range(N):
#         l = list(map(int, input().rstrip().split()))
#         l.append(0)
#         mat.append(l)
#     mat.append([0]*(M+1))            
#     # r과 d가 같이 가는 대각선
#     # 이동 가능한 장소: (+1, 0), (0, 1), (1, 1)                
#     for d in range(N+M+2):
#         for r in range(min(d, N), -1 ,-1): 
#             r = r
#             c = d - r
#             if c > M:
#                 break
#             sum_candidate = [mat[r-dr][c-dc] for dr, dc in drc if r - dr >= 0 and c - dc >= 0]            
#             if sum_candidate:
#                 mat[r][c] += max(sum_candidate)
    
#     print(mat[N][M])        

# # 일반적인 방식 (역으로 접근하진 않음.)    
# def sol2():
#     N, M = map(int, input().rstrip().split())
#     mat = [list(map(int, input().rstrip().split())) for _ in range(N)]
    
#     drc = [(-1, 0), (-1, -1), (0, -1)]
#     for r in range(N):
#         for c in range(M):            
#             candidate = [mat[r+dr][c+dc] for dr, dc in drc if r + dr >= 0 and c + dc >= 0]
#             if candidate:
#                 mat[r][c] += max(candidate)            

#     print(mat[N-1][M-1])

# sol2()
