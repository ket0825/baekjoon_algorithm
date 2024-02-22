"""
문제
영선이는 숫자가 쓰여 있는 직사각형 종이를 가지고 있다. 
종이는 1×1 크기의 정사각형 칸으로 나누어져 있고,
 숫자는 각 칸에 하나씩 쓰여 있다. 
 
 행은 위에서부터 아래까지 번호가 매겨져 있고, 
 열은 왼쪽부터 오른쪽까지 번호가 매겨져 있다.

영선이는 직사각형을 겹치지 않는 조각으로 자르려고 한다. 
각 조각은 크기가 세로나 가로 크기가 1인 직사각형 모양이다. 
길이가 N인 조각은 N자리 수로 나타낼 수 있다. 
가로 조각은 왼쪽부터 오른쪽까지 수를 이어 붙인 것이고, 
세로 조각은 위에서부터 아래까지 수를 이어붙인 것이다.

아래 그림은 4×4 크기의 종이를 자른 한 가지 방법이다.


각 조각의 합은 493 + 7160 + 23 + 58 + 9 + 45 + 91 = 7879 이다.

종이를 적절히 잘라서 조각의 합을 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 종이 조각의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 4)

둘째 줄부터 종이 조각이 주어진다. 
각 칸에 쓰여 있는 숫자는 0부터 9까지 중 하나이다.

출력
영선이가 얻을 수 있는 점수의 최댓값을 출력한다.

예제 입력 1 
2 3
123
312
예제 출력 1 
435
예제 입력 2 
2 2
99
11
예제 출력 2 
182
예제 입력 3 
4 3
001
010
111
100
예제 출력 3 
1131
예제 입력 4 
1 1
8
예제 출력 4 
8
출처
문제를 번역한 사람: baekjoon
"""

# 일단 정사각형이 아니면 긴 방향 결대로 찢는게 맞음.
# => 아님. 반례.
"""
0 0 0 8
0 0 0 8
"""
# 그럼 0이 있는 부분들 (한쪽 열이나, 한쪽 행 단위로)은 없는 셈 치고
# 결대로 찢는게 나음.
"""
0 0 0 0
0 0 0 8
0 0 0 8
"""

"""
3 3
000
012
034

46

2 2
00
00

2 3 => 비트마스킹으로 표현 가능!
123 101  111 000 010
312 010  000 001 000
"""

## 1. 비트마스킹 및 visited (DP) 사용.
import sys
input = sys.stdin.readline

def main(): 
    N, M = map(int, input().rstrip("\n").split()) #(1 ≤ N, M ≤ 4)
    board = [[num for num in input().rstrip("\n")] for _ in range(N) ]
    
    total_lst = []
    
    for bits in range((1 << N*M)-1, -1, -1):    #000 000 001 000
        visited_bits = 0
        total = 0
        format(bits, 'b').rjust(N*M, '0')
        format(visited_bits, 'b').rjust(N*M, '0')

        for row in range(N):            
            for col in range(M):
                index = row*M+col   # 0*N+0 = 0, 1*N+2 = N+2, # 0*N+M-1 = M-1 board
                if visited_bits & (1 << (N*M - index - 1)):
                    continue
                rowwise_piece_str = "0"
                colwise_piece_str = "0"
                if bits & (1 << index) == 0: # 세로로 더하기. 그런데 그 다음 비트 생각.
                    temp_row = row
                    
                    while True:
                        colwise_piece_str += board[temp_row][col]
                        visited_bits |= (1 << (N*M - index - 1))
                        temp_row += 1
                        index = temp_row*M+col
                        if bits & (1 << index) != 0 or temp_row == N:
                            break
                    total += int(colwise_piece_str)
                else:   # 1이면 가로로 더하기. 그런데 그 다음 비트 생각.
                    temp_col = col

                    while True:
                        rowwise_piece_str += board[row][temp_col]
                        visited_bits |= (1 << (N*M - index - 1))
                        temp_col += 1
                        index = row*M+temp_col
                        if bits & (1 << index) == 0 or temp_col == M:
                            break
                    total += int(rowwise_piece_str)
                       
        
        total_lst.append(total)

    print(max(total_lst))


if __name__ =='__main__':
    main()


## 2. 더 깔끔한 풀이. DP 안써서 더 빠른 것일수도.
N, M = map(int, input().split())
# bitmasking
A = [list(map(int, input())) for _ in range(N)]
ans = 0

for i in range(1 << N * M):
    s = 0
    for c in range(N):
        tmps = 0
        for r in range(M):
            if i & 1 << (c * M + r) != 0:
                tmps *= 10
                tmps += A[c][r]
            else:
                s += tmps
                tmps = 0
        s += tmps
    for r in range(M):
        tmps = 0
        for c in range(N):
            if i & 1 << (c * M + r) == 0:
                tmps *= 10
                tmps += A[c][r]
            else:
                s += tmps
                tmps = 0
        s += tmps
    ans = max(ans, s)
print(ans)


# import sys

# input=sys.stdin.readline

# N,M=map(int,input().strip().split())

# graphs=[]

# for _ in range(N):
#     graphs.append(list(map(int,input().strip())))

# ans=[]

# def bitmask():
#     for i in range(1<<N*M):
#         total=0
#         for row in range(N):
#             rowsum=0
#             for col in range(M):
#                 idx=row*M+col
#                 if i&(1<<idx) != 0:
#                     rowsum=rowsum*10+graphs[row][col]
#                 else:
#                     total+=rowsum
#                     rowsum=0
#             total+=rowsum


#     for col in range(M):
#         colsum=0
#         for row in range(N):
#             idx=row*M+col
#             if i&(1<<idx)==0:
#                 colsum=colsum*10+graphs[row][col]
#             else:
#                 total+=colsum
#                 colsum=0
#         total+=colsum
#     ans.append(total)

# bitmask()

# print(max(ans))        







# 틀렸습니다 나옴.
# import sys
# input = sys.stdin.readline

# def main():
#     N, M = map(int, input().rstrip("\n").split()) #(1 ≤ N, M ≤ 4)
#     board = [[num for num in input().rstrip("\n")] for _ in range(N) ]

#     # trimming all row-wise elem is 0.
#     for i in range(N):
#         zero_row_count = 0
#         for j in range(M):
#             if board[i][j] == "0":
#                 zero_row_count +=1
#             else:
#                 break
#         if zero_row_count == M:
#             for j in range(M):
#                 board[i][j] = "-1"

#     # trimming all col-wise elem is 0.
#     for j in range(M):
#         zero_col_count = 0
#         for i in range(N):
#             if board[i][j] == "0" or board[i][j] == "-1":   # -1로 변경해준 것도 기존에 0이었음.
#                 zero_col_count +=1
#             else:
#                 break
#         if zero_col_count == N:
#             for i in range(N):
#                 board[i][j] = "-1"

#     trimmed_board = [[col for col in row if col != "-1"] for row in board]
#     # empty list removing.
#     remove_indices = []

#     is_empty = True
#     for i in trimmed_board:
#         for j in i:
#             if j:
#                 is_empty = False   

#     if is_empty:
#         print(0)    
#         return
    
#     for idx, row in enumerate(trimmed_board):
#         if not row:
#             remove_indices.append(idx)

#     for i in remove_indices[::-1]:
#         trimmed_board.pop(i)

#     # print(trimmed_board)
    
#     trimmed_N = len(trimmed_board)
#     trimmed_M = len(trimmed_board[0])

#     row_wise_sum = 0
#     col_wise_sum = 0

#     if trimmed_N < trimmed_M:
#         for row in trimmed_board:
#             row_wise_sum+=int(''.join(row))
        
#         print(row_wise_sum)
#     elif trimmed_N > trimmed_M:


#         for col_idx in range(trimmed_M):    
#             chars = ""
#             for row_idx in range(trimmed_N):
#                 chars+=trimmed_board[row_idx][col_idx]
#             col_wise_sum += int(chars)
        
#         print(col_wise_sum)
#     else:
#         for row in trimmed_board:
#             row_wise_sum+=int(''.join(row))

#         for col_idx in range(trimmed_M):   
#             chars = ""
#             for row_idx in range(trimmed_N):
#                 chars+=trimmed_board[row_idx][col_idx]
#             col_wise_sum += int(chars)

#         print(max(col_wise_sum,row_wise_sum))       


# if __name__ == "__main__":
#     main()