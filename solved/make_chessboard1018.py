"""
문제
지민이는 자신의 저택에서 
MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 
어떤 정사각형은 검은색으로 칠해져 있고, 
나머지는 흰색으로 칠해져 있다. 
지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 
변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 
지민이는 8×8 크기의 체스판으로 잘라낸 후에 
몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
당연히 8*8 크기는 아무데서나 골라도 된다. 

지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. 
N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. 
B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

예제 입력 1 
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
예제 출력 1 
1
예제 입력 2 
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
예제 출력 2 
12
예제 입력 3 
8 8
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
예제 출력 3 
0
예제 입력 4 
9 23
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBW
예제 출력 4 
31
예제 입력 5 
10 10
BBBBBBBBBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBBBBBBBBB
예제 출력 5 
0
예제 입력 6 
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWWWB
BWBWBWBW
예제 출력 6 
2
예제 입력 7 
11 12
BWWBWWBWWBWW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBWWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
예제 출력 7 
15
"""
"""
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
"""

## 1. 8*8 board 하나하나 옮겨가면서 하고, 실제 색칠 횟수 2가지 경우로 체크해보기.
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip().split(" ")) # 8 <= N, M <= 50
    board = [input().rstrip() for _ in range(N)] # W가 1, B가 0.
    count_list = []

    for row in range(N-7):
        for col in range(M-7):
            # coloring count
            white_start_count, black_start_count = 0, 0
            for i in range(row, row+8):
                for j in range(col, col+8):
                    if (i+j) % 2 == 0 and board[i][j] == "B": # 짝수이고 검은색이면
                        white_start_count+=1
                    elif (i+j) % 2 == 1 and board[i][j] == "W": # 홀수이고 하얀색이면
                        white_start_count+=1
            for i in range(row, row+8):
                for j in range(col, col+8):
                    if (i+j) % 2 == 0 and board[i][j] == "W": # 짝수이고 하얀색이면
                        black_start_count+=1
                    elif (i+j) % 2 == 1 and board[i][j] == "B": # 홀수이고 검은색이면
                        black_start_count+=1

            count_list.append(white_start_count if white_start_count < black_start_count else black_start_count)

    print(min(count_list))
    
    
# if __name__ == '__main__':
#     main()

## 2. truncated board 만들 수 있음. 그리고 직렬화. 출처: audrms12
import sys
n, m = map(int, sys.stdin.readline().split())
list1=[sys.stdin.readline().split()[0] for _ in range(n)]

lowst=100
word=['W', 'B']

for i in range(n-7):
    for j in range(m-7):
        d=[k[j:j+8] for k in list1[i:8+i]]
        fw=0
        fb=0
        first=''.join(d[0::2])  # 0부터 시작, 끝은 없음. 2칸씩 뛰어가며... 그리고 직렬화.
        second=''.join(d[1::2])
        c=-1
        for j in first:
            c+=1
            if j == word[c%2]:
                fb+=1
            else:
                fw+=1
        c=0
        for j in second:
            c+=1
            if j == word[c%2]:
                fb+=1
            else:
                fw+=1
        lowst=min(lowst, fb, fw)
print(lowst)
 