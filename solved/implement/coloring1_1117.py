"""
색칠 1
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	2799	833	656	31.120%
문제
지민이는 종이에 색칠하기를 좋아한다. 지민이는 W×H 크기의 직사각형 종이를 가지고 있다. 지민이는 종이에 다음과 같이 색칠 하려고 한다.

종이를 x = f에 맞춰서 접는다. 이때, 왼쪽 종이가 오른쪽 종이 위에 올라오게 접는다.
종이를 가로로 c+1개의 크기가 동일 한 구간으로 나눈다. 그 다음에 c번 가장 위의 구간부터 차례대로 접는다.
왼쪽 아래가 (x1, y1) 이고, 오른쪽 위가 (x2, y2)인 직사각형을 찾는다. 이때, (0, 0)은 현재 접힌 상태에서 가장 왼쪽 아래 점이다. 그 직사각형을 칠한다. 이때, 페인트는 겹쳐있는 모든 곳에 스며든다.
종이를 편다.
다음 예는 5×6 종이에, x=2이고, c=2이고, (x1, y1) = (1, 1), (x2, y2) = (3, 2)인 경우이다.





W, H, f, c, x1, y1, x2, y2가 주어질 때, 색칠되어 있지 않은 면적을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 8개의 정수 W, H, f, c, x1, y1, x2, y2가 주어진다.

출력
첫째 줄에 색칠되지 않은 영역의 넓이를 출력한다.

제한
1 ≤ W, H ≤ 109
0 ≤ f ≤ W
0 ≤ c ≤ 1,000
c+1은 H의 약수
0 ≤ x1 < x2 ≤ max(f, W-f)
0 ≤ y1 < y2 ≤ H/(c+1)
예제 입력 1 
5 6 2 2 1 1 3 2
예제 출력 1 
21
예제 입력 2 
3 13 1 0 1 8 2 12
예제 출력 2 
35
예제 입력 3 
12 12 7 3 3 1 6 2
예제 출력 3 
124
예제 입력 4 
4 5 4 0 0 0 1 1
예제 출력 4 
19
예제 입력 5 
4 8 4 3 0 1 2 2
예제 출력 5 
24
예제 입력 6 
4 8 3 0 1 1 3 2
예제 출력 6 
30

5 6 1 0 2 0 4 2
28

5 6 1 5 0 0 2 1
12

5 6 2 0 0 0 1 2
26



"""
import sys
input = sys.stdin.readline

def sol():
    W, H, f, c_div, x1, y1, x2, y2 = map(int, input().strip().split())    
    if f > W / 2:
        f = W - f # 어차피 같음.
    
    x_double = (0, f)    
    # x1과 x2 범위를 보고 2배 색칠 영역 파악    
    if x1 > x_double[1]: # 한 칸 색칠만 있는 경우,
        x_colored_double = 0
        x_colored_mono = x2 - x1
    elif x1 <= x_double[1] < x2: # 한 칸, 두 칸 색칠 모두 다 있는 경우
        x_colored_double = x_double[1] - x1 # x쪽 2배 색칠 칸수
        x_colored_mono = x2 - x_double[1] # x쪽 1배 색칠 칸수
    elif x2 <= x_double[1]:
        x_colored_double = x2 - x1 # x쪽 2배 색칠 칸수
        x_colored_mono = 0 # x쪽 1배 색칠 칸수                        
    # y1과 y2 범위를 보고 multiple 색칠 영역 파악 (모두 multiple!)
    y_colored_multiple = (y2-y1)*(c_div+1)
    # print(f"f:{f}, x_colored_double: {x_colored_double}, x_colored_mono: {x_colored_mono}, y_colored_multiple: {y_colored_multiple} ")    
    colored = (2*x_colored_double+x_colored_mono) * y_colored_multiple            
    
    non_colored = W*H - colored
    print(non_colored)

def sol2():
    W, H, f, c_div, x1, y1, x2, y2 = map(int, input().strip().split())
    c_bound = 0
    r_bound = 0
    if f > W / 2:
        f = W - f # 어차피 같음.
    
    mat = [[1 for _ in range(W)] for _ in range(H)]    
    # x=f 접기
    c_bound = f
    # print(f"c_bound: {c_bound}")
    
            # mat[r][c] = 0
    # print(mat)
    # c+1로 나눠접기 (올려접는다고 생각해도 무방)
    r_bound = (H // (c_div+1)) 
    # print(f"r_bound: {r_bound}")
    for r in range(r_bound):
        for c in range(c_bound, W):
            mat[r][c] *= c_div+1
    
    # x1, x2 재조정
    x1+=c_bound
    x2+=c_bound
    # print(f"x1: {x1}, x2: {x2}, y1: {y1}, y2: {y2}")
    # print("mat", mat)
    # print(mat[y1:y2][x1:])
    colored = 0
    for i in range(y1, y2):
        for j in range(x1, x2):
            # print(f"{i}, {j}, {mat[i][j]}")
            colored+=mat[i][j]        
    non_colored = W*H - colored
    print(non_colored)
    
if __name__ == '__main__':
    sol()