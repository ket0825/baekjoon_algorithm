"""
행렬
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	26699	11551	9324	43.123%
문제
0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

입력
첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.

예제 입력 1 
3 4
0000
0010
0000
1001
1011
1001
예제 출력 1 
2
예제 입력 2 
3 3
111
111
111
000
000
000
예제 출력 2 
1
예제 입력 3 
1 1
1
0
예제 출력 3 
-1
예제 입력 4 
18 3
001
100
100
000
011
010
100
100
010
010
010
110
101
101
000
110
000
110
001
100
011
000
100
010
011
100
101
101
010
001
010
010
111
110
111
001
예제 출력 4 
7
---
3 3
000
000
000
000
000
001

-1
---
3 3
000
010
000
111
100
000
---
4 4
0000
0001
0001
0001
0000
0000
0000
0000

-1
---
4 4
0000
0000
0000
0000
1001
0000
0000
1001

4
---
4 4
0000
0000
0000
0000
0111
1001
1001
1110

-2
---
4 4
0000
0000
0000
0000
0111
1001
1001
1110

2
---
4 4
0000
0000
0000
0000
1001
0111
0111
1110

3

"""

import sys
input = sys.stdin.readline

def sol():
    N, M = map(int, input().strip().split()) #  N과 M은 50보다 작거나 같은 자연수
    # 50**4*2 = 12500000
    mat_A = [list(map(lambda x: bool(int(x)), input().strip())) for _ in range(N)]
    mat_B = [list(map(lambda x: bool(int(x)), input().strip())) for _ in range(N)]
    
    # 같은지 확인
    def is_same():
        for i in range(N):
            for j in range(M):
                if mat_A[i][j] != mat_B[i][j]:
                    return False        
        return True
    
    # 이 부분 에러였음...
    if is_same():
        print(0)
        return
    
    if N <= 2 or M <= 2:
        print(-1)
        return        
                   
    inverted_count = [[0 for _ in range(M-2)] for _ in range(N-2)]
        
    def inversion(r, c):
        for i in range(r, r+3):
            for j in range(c, c+3):                
                mat_A[i][j] = not mat_A[i][j]
                
        inverted_count[r][c] += 1
    
    cnt = 0
    while True:
        if is_same():
            print(cnt)
            return
        
        inverted = False
        for r in range(N):
            for c in range(M):
                if mat_A[r][c] != mat_B[r][c]:
                    nearest_r = r if r < N - 2 else N - 3
                    nearest_c = c if c < M - 2 else M - 3
                    # print("nearest r, c:",nearest_r, nearest_c)               
                    inversion(nearest_r, nearest_c)
                    # print(inverted_count[nearest_r][nearest_c])
                    if inverted_count[nearest_r][nearest_c] >= 2:
                        print(-1)
                        return
                    inverted = True
                    cnt+=1
                    break
            if inverted:
                break
            
        # print(*mat_A, sep="\n")
        # print("----------------------")
        # print(*mat_B, sep="\n")
        # print("----------------------")
    # 첫째 줄에 문제의 정답을 출력한다. 
    # 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.
    
if __name__ == '__main__':
    sol()    
    
    