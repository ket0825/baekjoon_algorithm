# 최대 25000개 입력 (500 x 500), 각 입력은 1000을 넘지 않는 자연수.


# import sys

# input = sys.stdin.readline

# def main():    
#     N, M = map(int, input().rstrip("\n").split(" "))
#     paper = [list(map(int, input().rstrip("\n").split(" "))) for i in range(N)]

#     # 인접한 4개를 찾도록 하면 됨.
#     max_value = 0
#     prev_value = 0
#     # line_shape_right
#     for i in range(N):
#         for j in range(M-3):
#             max_value = max(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3], max_value)
    
#     # line_shape_down
#     for i in range(N-3):
#         for j in range(M):
#             max_value = max(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j], max_value)
    
#     # square
#     for i in range(N-1):
#         for j in range(M-1):
#             max_value = max(paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1], max_value)

#     # ㄱ-eastside and ㄱ-westside and  ㅜ ㄱ ㅜ 
#     for i in range(N-1):
#         for j in range(M-2):
#             max_value = max(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j], max_value)
#             max_value = max(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+1], max_value)
#             max_value = max(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+2], max_value)
    
#     # ㄱ-southside and ㄱ-northside and ㅏ ㅏ L
#     for i in range(N-2):
#         for j in range(M-1):
#             max_value = max(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i][j+1], max_value)
#             max_value = max(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+1][j+1], max_value)
#             max_value = max(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1], max_value)
    
#     # 새로로 긴 기억 and ㄱ-westside and  ㅜ 
#     for i in range(N-1):
#         for j in range(M-2):
#             max_value = max(paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2], max_value)
#             max_value = max(paper[i][j+1] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2], max_value)
#             max_value = max(paper[i][j+2] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2], max_value)
                
#     # ㄱ-southside and ㄱ-northside and ㅏ
#     for i in range(N-2):
#         for j in range(M-1):
#             max_value = max(paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1], max_value)
#             max_value = max(paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1], max_value)
#             max_value = max(paper[i+2][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1], max_value)
    
#     # zigzag-vertical
#     for i in range(N-2):
#         for j in range(M-1):
#             max_value = max(paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j+1], max_value)
#             max_value = max(paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j] + paper[i+2][j], max_value)

#     # zigzag-horizontal
#     for i in range(N-1):
#         for j in range(M-2):
#             max_value = max(paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j+2], max_value)
#             max_value = max(paper[i+1][j] + paper[i+1][j+1] + paper[i][j+1] + paper[i][j+2], max_value)
            
#     print(max_value)


# if __name__ == '__main__':
#     main()


# 최대 25000개 입력 (500 x 500), 각 입력은 1000을 넘지 않는 자연수.
## 2
import sys

input = sys.stdin.readline

def main():    
    N, M = map(int, input().rstrip("\n").split(" "))
    paper = [list(map(int, input().rstrip("\n").split(" "))) for i in range(N)]

    # 인접한 4개를 찾도록 하면 됨.
    max_value = 0
    prev_value = 0
    # line_shape_right
    for i in range(N):
        for j in range(M-3):
            max_value = max(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3], max_value)
    
    # line_shape_down
    for i in range(N-3):
        for j in range(M):
            max_value = max(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j], max_value)
    
    # square
    for i in range(N-1):
        for j in range(M-1):
            max_value = max(paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1], max_value)

    # ㄱ-eastside and ㄱ-westside and  ㅜ ㄱ ㅜ 
    for i in range(N-1):
        for j in range(M-2):
            max_value = max(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j], max_value)
            max_value = max(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+1], max_value)
            max_value = max(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+2], max_value)
            max_value = max(paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2], max_value)
            max_value = max(paper[i][j+1] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2], max_value)
            max_value = max(paper[i][j+2] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2], max_value)
            max_value = max(paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j+2], max_value)
            max_value = max(paper[i+1][j] + paper[i+1][j+1] + paper[i][j+1] + paper[i][j+2], max_value)
    
    # ㄱ-southside and ㄱ-northside and ㅏ ㅏ L
    for i in range(N-2):
        for j in range(M-1):
            max_value = max(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i][j+1], max_value)
            max_value = max(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+1][j+1], max_value)
            max_value = max(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1], max_value)
            max_value = max(paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1], max_value)
            max_value = max(paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1], max_value)
            max_value = max(paper[i+2][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1], max_value)
            max_value = max(paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j+1], max_value)
            max_value = max(paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j] + paper[i+2][j], max_value)
 
    print(max_value)


if __name__ == '__main__':
    main()


## 3 : 다른 사람 풀이: DFS    
# import sys

# N, M = list(map(int, sys.stdin.readline().split()))
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# visited = [[0] * M for _ in range(N)]
# res = 0    # 최종 결과
# max_of_board = max(map(max, board))    # board에서 최댓값

# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]

# def DFS(x, y, L, total):
#   ''' board를 DFS로 탐색하는 함수 (모든 테트로미노 모양을 만들 수 있음)
#   parameters
#   x, y : DFS를 시작할 board의 좌표 
#   L : DFS를 한 횟수
#   total: L번의 DFS를 하면서 거쳐온 좌표에서의 자연수의 합
#   ''' 

#   # 현재 최댓값(res)이 L번의 DFS를 통해 합한 값(total)과 board의 최댓값 * (나머지 횟수)보다 클 때 DFS를 할 필요가 없으므로 빠르게 종료
#   global res
#   if res >= total + max_of_board*(4-L):
#     return
    
#   # 4번째 돌았을 때 == 테트로미노가 만들어진 것
#   if L == 4:
#     res = max(res, total)

#   else:
#     # 상하좌우 탐색
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
  
#       if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
#         # 블럭이 2개 모였을 때, 상하좌우에 갔다치고 현재 좌표에서 탐색 -> (x, y)로 탐색하지만 L에 +1 해주고, total에도 board[nx][ny]를 더해줌
#         if L == 2:
#           visited[nx][ny] = 1
#           DFS(x, y, L+1, total + board[nx][ny])
#           visited[nx][ny] = 0
          
#         visited[nx][ny] = 1
#         DFS(nx, ny, L+1, total + board[nx][ny])
#         visited[nx][ny] = 0

# for i in range(N):
#   for j in range(M):
#     visited[i][j] = 1
#     DFS(i, j, L=1, total=board[i][j])
#     visited[i][j] = 0

# print(res)