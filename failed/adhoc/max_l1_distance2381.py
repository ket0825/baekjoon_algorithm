"""
최대 거리
시간 제한	메모리 제한	
1 초	128 MB
문제
N(1 ≤ N ≤ 50,000)개의 점들이 있을 때, 최대 L1-metric 거리를 찾으시오.

두 점의 좌표가 (a, b), (c, d)일 때, 두 점의 L1-metric 거리는 |a-c|+|b-d|이다.

입력
첫째 줄에 N이 주어진다. 다음 N개의 줄에는 각 점의 x, y좌표가 주어진다. 각 좌표의 범위는 -1,000,000이상 1,000,000이하이다.

출력
첫째 줄에 최대 거리를 출력한다.

예제 입력 1 
5
1 1
3 5
2 7
8 1
4 4
예제 출력 1 
12

8
1 1
3 5
0 -1
2 7
8 1
-4 4
-3 6
8 0
---
17


"""
import sys
input = sys.stdin.readline

def sol():
    N = int(input().strip())
    
    # 초기값 설정
    max_x_plus_y = float('-inf')
    min_x_plus_y = float('inf')
    max_x_minus_y = float('-inf')
    min_x_minus_y = float('inf')
    
    for _ in range(N):
        x, y = map(int, input().strip().split())
        
        # x+y 최대/최소 갱신
        max_x_plus_y = max(max_x_plus_y, x + y)
        min_x_plus_y = min(min_x_plus_y, x + y)
        
        # x-y 최대/최소 갱신
        max_x_minus_y = max(max_x_minus_y, x - y)
        min_x_minus_y = min(min_x_minus_y, x - y)
    
    # 두 경우 중 최댓값이 최대 맨해튼 거리
    max_distance = max(max_x_plus_y - min_x_plus_y, max_x_minus_y - min_x_minus_y)
    
    print(max_distance)

if __name__ == '__main__':
    sol()   