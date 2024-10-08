"""
배열 돌리기 1
1 초	512 MB
문제
크기가 N×M인 배열이 있을 때, 배열을 돌려보려고 한다. 배열은 다음과 같이 반시계 방향으로 돌려야 한다.

A[1][1] ← A[1][2] ← A[1][3] ← A[1][4] ← A[1][5]
   ↓                                       ↑
A[2][1]   A[2][2] ← A[2][3] ← A[2][4]   A[2][5]
   ↓         ↓                   ↑         ↑
A[3][1]   A[3][2] → A[3][3] → A[3][4]   A[3][5]
   ↓                                       ↑
A[4][1] → A[4][2] → A[4][3] → A[4][4] → A[4][5]
예를 들어, 아래와 같은 배열을 2번 회전시키면 다음과 같이 변하게 된다.

1 2 3 4       2 3 4 8       3 4 8 6
5 6 7 8       1 7 7 6       2 7 8 2
9 8 7 6   →   5 6 8 2   →   1 7 6 3
5 4 3 2       9 5 4 3       5 9 5 4
 <시작>         <회전1>        <회전2>
배열과 정수 R이 주어졌을 때, 배열을 R번 회전시킨 결과를 구해보자.

입력
첫째 줄에 배열의 크기 N, M과 수행해야 하는 회전의 수 R이 주어진다.

둘째 줄부터 N개의 줄에 배열 A의 원소 Aij가 주어진다.

출력
입력으로 주어진 배열을 R번 회전시킨 결과를 출력한다.

제한
2 ≤ N, M ≤ 300
1 ≤ R ≤ 1,000
min(N, M) mod 2 = 0
1 ≤ Aij ≤ 108
예제 입력 1 
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
예제 출력 1 
3 4 8 12
2 11 10 16
1 7 6 15
5 9 13 14
예제 입력 2 
5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28
예제 출력 2 
28 27 26 25
22 9 15 19
16 8 21 13
10 14 20 7
4 3 2 1
예제 입력 3 
2 2 3
1 1
1 1
예제 출력 3 
1 1
1 1
"""
import sys
input = sys.stdin.readline

def sol():
    N, M, R = map(int, input().rstrip().split())    
    mat = [list(map(int, input().rstrip().split())) for _ in range(N)]
    mat_copy = [[col for col in row] for row in mat]
    def rotate_mat(row_idx, col_idx):                
        track = []        
                    
        track.extend([(r, col_idx) for r in range(row_idx, N-row_idx-1)])
        track.extend([(N-row_idx-1, c) for c in range(col_idx, M-col_idx-1)])
        track.extend([(r, M-col_idx-1) for r in range(N-row_idx-1, row_idx, -1)])
        track.extend([(row_idx, c) for c in range(M-col_idx-1, col_idx, -1)])
                        
        move = R % len(track)                
        
        
        for track_idx in range(len(track)):
        
            change_idx = (track_idx+move) % len(track)                   
            prev_row, prev_col = track[change_idx]
            cur_row, cur_col = track[track_idx]      
        
            mat[prev_row][prev_col] = mat_copy[cur_row][cur_col]         

    row_idx = 0
    col_idx = 0
    while row_idx != (N // 2) and col_idx != (M // 2):            
        rotate_mat(row_idx, col_idx)
        row_idx+=1
        col_idx+=1            
                    
    for row in mat:
        print(*row)        
            
    
if __name__ == "__main__":
    sol()
    