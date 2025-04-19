"""
달팽이
시간 제한	메모리
2 초	128 MB
문제
홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N^2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.

9	2	3
8	1	4
7	6	5

25	10	11	12	13
24	9	2	3	14
23	8	1	4	15
22	7	6	5	16
21	20	19	18	17

N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오. 또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오. 
예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.

입력
첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다. 둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.

출력
N개의 줄에 걸쳐 표를 출력한다. 각 줄에 N개의 자연수를 한 칸씩 띄어서 출력하면 되며, 자릿수를 맞출 필요가 없다. N+1번째 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력한다.

예제 입력 1 
7
35
예제 출력 1 
49 26 27 28 29 30 31
48 25 10 11 12 13 32
47 24 9 2 3 14 33
46 23 8 1 4 15 34
45 22 7 6 5 16 35
44 21 20 19 18 17 36
43 42 41 40 39 38 37
5 7
"""

# import sys

# input = sys.stdin.readline

# def sol(N, target):
#     mat = [[-1 for _ in range(N)] for _ in range(N)]        
#     col = N // 2
#     row = N // 2
#     target_idx = (row+1, col+1)
#     move_lim = 0
#     num = 1
#     mat[col][row] = num
#     num+=1
#     out_of_idx = False
#     dr = [-1, 0, 1, 0]
#     dc = [0, 1, 0, -1]
#     while True:                        
#         move_lim+=1
#         for _ in range(move_lim) : # 움직인 횟수 <= 움직일 수 있는 횟수
#             row = row - 1        
#             if row < 0: # 음수 인덱스. 여기서만 끝나는 가능성 존재.
#                 out_of_idx = True
#                 break                        
#             mat[row][col] = num
#             # print("현재 row:",row, "현재 col:", col, "현재 값:", num, "제한:", move_lim)
#             if num == target:
#                 target_idx = (row+1, col+1)
#             num+=1            
        
#         if out_of_idx:
#             break
                        
#         for _ in range(move_lim) : # 움직인 횟수 <= 움직일 수 있는 횟수
#             col = col + 1
#             mat[row][col] = num
#             # print("현재 row:",row, "현재 col:", col, "현재 값:", num, "제한:", move_lim)
#             if num == target:
#                 target_idx = (row+1, col+1)
#             num+=1            

#         # 이동 가능 +1
#         move_lim+=1
#         for _ in range(move_lim):        
#             row = row + 1                        
#             mat[row][col] = num
#             # print("현재 row:",row, "현재 col:", col, "현재 값:", num, "제한:", move_lim)
#             if num == target:
#                 target_idx = (row+1, col+1)
#             num+=1                
                
#         for _ in range(move_lim):
#             col = col - 1
#             mat[row][col] = num
#             # print("현재 row:",row, "현재 col:", col, "현재 값:", num, "제한:", move_lim)
#             if num == target:
#                 target_idx = (row+1, col+1)
#             num+=1            

#     for row in mat:
#         print(*row)
    
#     print(*target_idx) 
    

# if __name__ == '__main__':
#     N = int(input().strip())
#     target = int(input().strip())
#     sol(N, target)
    
import sys

input = sys.stdin.readline

def sol(N, target):
    mat = [[-1 for _ in range(N)] for _ in range(N)]        
    col = N // 2
    row = N // 2
    target_idx = (row+1, col+1)
    move_lim = 1
    num = 1
    mat[col][row] = num
    num+=1
    out_of_idx = False
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while not out_of_idx:        
        for i in range(4):
            for _ in range(move_lim) : # 움직인 횟수 <= 움직일 수 있는 횟수            
                row+=dr[i]
                col+=dc[i]                
                if col < 0 or col >= N or row < 0 or row >= N:
                    out_of_idx = True
                    break
                
                mat[row][col] = num
                # print("현재 row:",row, "현재 col:", col, "현재 값:", num, "제한:", move_lim)
                if num == target:
                    target_idx = (row+1, col+1)
                num+=1
                
            if out_of_idx:
                break
                                
            if i % 2 == 1:
                move_lim+=1
            
    for row in mat:
        print(*row)
    
    print(*target_idx) 
    

if __name__ == '__main__':
    N = int(input().strip())
    target = int(input().strip())
    sol(N, target)