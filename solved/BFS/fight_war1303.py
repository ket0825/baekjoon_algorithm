"""
전쟁 - 전투
시간 제한	메모리 제한
2 초	128 MB
문제
전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다. 그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다. 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.

N명이 뭉쳐있을 때는 N2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가? 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

입력
첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 당신의 병사와 적국의 병사는 한 명 이상 존재한다.

출력
첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.

예제 입력 1 
5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW
예제 출력 1 
130 65

1 3
WWW

9 0

1 1
W

1 0

1 3
B
B
B

0 9

3 3
WWW
WWW
WWW

81 0

2 4
WB
WB
WW
WW

36 4
"""
import sys
from collections import deque

input = sys.stdin.readline

def sol():
    N, M = map(int, input().strip().split())
    soldiers = [input().strip() for _ in range(M)]
    
    dr = [0,0,-1,1]
    dc = [1,-1,0,0]
    
    visited = [[False]*N for _ in range(M)]
    
    def bfs(start, r, c):
        q = deque([(r,c)])
        cnt = 1
        
        while q:
            r, c = q.pop()            
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]
                
                if (0 <= nr < M 
                    and 0 <= nc < N 
                    and not visited[nr][nc] 
                    and soldiers[nr][nc] == start
                    ):
                    q.appendleft((nr, nc))
                    cnt+=1
                    visited[nr][nc] = True
        
        return cnt**2            
    
    w_score = 0
    b_score = 0
    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                if soldiers[i][j] == 'W':
                    w_score+=bfs(soldiers[i][j], i, j)
                else:
                    b_score+=bfs(soldiers[i][j], i, j)
    
    print(w_score, b_score)
    

if __name__ == "__main__":    
    sol()
