"""
컴백홈 다국어
시간 제한	메모리 
2 초	128 MB
문제
한수는 캠프를 마치고 집에 돌아가려 한다. 한수는 현재 왼쪽 아래점에 있고 집은 오른쪽 위에 있다. 그리고 한수는 집에 돌아가는 방법이 다양하다. 단, 한수는 똑똑하여 한번 지나친 곳을 다시 방문하지는 않는다.

      cdef  ...f  ..ef  ..gh  cdeh  cdej  ...f 
      bT..  .T.e  .Td.  .Tfe  bTfg  bTfi  .Tde 
      a...  abcd  abc.  abcd  a...  a.gh  abc. 
거리 :  6     6     6     8     8    10    6
위 예제는 한수가 집에 돌아갈 수 있는 모든 경우를 나타낸 것이다. T로 표시된 부분은 가지 못하는 부분이다. 문제는 R x C 맵에 못가는 부분이 주어지고 거리 K가 주어지면 한수가 집까지도 도착하는 경우 중 거리가 K인 가짓수를 구하는 것이다.

입력
첫 줄에 정수 R(1 ≤ R ≤ 5), C(1 ≤ C ≤ 5), K(1 ≤ K ≤ R×C)가 공백으로 구분되어 주어진다. 두 번째부터 R+1번째 줄까지는 R×C 맵의 정보를 나타내는 '.'과 'T'로 구성된 길이가 C인 문자열이 주어진다.

출력
첫 줄에 거리가 K인 가짓수를 출력한다.

예제 입력 1 
3 4 6
....
.T..
....
예제 출력 1 
4
"""

import sys
input = sys.stdin.readline

def sol():
    R, C, K = map(int, input().strip().split())
    mat = [input().strip() for _ in range(R)]
    visited = [[False]*C for _ in range(R)]
    visited[R-1][0] = True
    cnt = 0
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    
    def search(r, c, move):
        if move == K:
            if r == 0 and c == C-1:
                nonlocal cnt                
                cnt+=1                
            return        
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # print(f"nr: {nr}, nc: {nc}, move: {move}")
            if 0 <= nr < R and 0 <= nc < C:                
                if mat[nr][nc] == 'T': # 막혀있으면 탐색 금지.
                    continue
                # print(nr, nc)
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    search(nr, nc, move+1)
                    visited[nr][nc] = False
    
    search(R-1, 0, 1)
    print(cnt)                                    
    
sol()

