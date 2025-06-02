"""
직사각형으로 나누기
시간 제한	메모리 제한	
2 초	128 MB
문제
세준이는 N*M크기로 직사각형에 수를 N*M개 써놓았다.

세준이는 이 직사각형을 겹치지 않는 3개의 작은 직사각형으로 나누려고 한다. 각각의 칸은 단 하나의 작은 직사각형에 포함되어야 하고, 각각의 작은 직사각형은 적어도 하나의 숫자를 포함해야 한다.

어떤 작은 직사각형의 합은 그 속에 있는 수의 합이다. 입력으로 주어진 직사각형을 3개의 작은 직사각형으로 나누었을 때, 각각의 작은 직사각형의 합의 곱을 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 직사각형의 세로 크기 N과 가로 크기 M이 주어진다. 둘째 줄부터 직사각형에 들어가는 수가 가장 윗 줄부터 한 줄에 하나씩 M개의 수가 주어진다. N과 M은 50보다 작거나 같은 자연수이고, 직사각형엔 적어도 3개의 수가 있다. 또, 직사각형에 들어가는 수는 한 자리의 숫자이다.

출력
세 개의 작은 직사각형의 합의 곱의 최댓값을 출력한다.

예제 입력 1 
# 2 * 9 * 6
1 8
11911103 
예제 출력 1 
108
예제 입력 2 
3 3
123
456
789
예제 출력 2 
3264
예제 입력 3 
3 1
7
9
3
예제 출력 3 
189

3 3
147
238
569
예제 출력 4
3264

1 5
91212

81

1 5
12129

81

2 5
91212
12129

990

3 5
91212
12129
19621

4352

3 3
124
212
213

216

3 3
122
211
423

216

"""
import sys

input = sys.stdin.readline

def divide_and_compute(N, M, mat):
    # 가로로 길게 자름.
    row_max = 0
    row_sum = [0]*N    
    row_acc = 0    
    for i in range(N):
        row_sum[i] = sum(mat[i]) # M        
        # print(f"row_sum: {row_sum}")
    if M > 1:        
        for i in range(N-1): # N-1        
            row_acc+=row_sum[i]
            # print(f"row_acc: {row_acc}")
            # col_sum에서 prefix M * i-N                
            col_sum = [0]*M
            for k in range(i+1, N):
                for j in range(M): # col에서 하나하나 쪼개어 더함.
                    col_sum[j]+=mat[k][j]        
            # print(f"col_sum: {col_sum}")
            for jj in range(1, M):
                # print(f"row로 1개, col로 2분할: {row_acc} * {sum(col_sum[0:jj])} * {sum(col_sum[jj:M])}")
                row_max = max(sum(col_sum[0:jj])*sum(col_sum[jj:M])*row_acc, row_max) # 0 * 1:M, # M-2, M-1:M
                # print(f"row_max: {row_max}")
        
        # print("아래부터 시작!")
        row_acc = 0
        for i in range(N-1, 0, -1): # N-1...1
            row_acc+=row_sum[i]
            # print(f"row_acc: {row_acc}")
            # col_sum에서 prefix M * i-N                
            col_sum = [0]*M
            for k in range(0, i):
                for j in range(M): # col에서 하나하나 쪼개어 더함.
                    col_sum[j]+=mat[k][j]        
            # print(f"col_sum: {col_sum}")
            for jj in range(1, M):
                # print(f"row로 1개, col로 2분할: {row_acc} * {sum(col_sum[0:jj])} * {sum(col_sum[jj:M])}")
                row_max = max(sum(col_sum[0:jj])*sum(col_sum[jj:M])*row_acc, row_max) # 0 * 1:M, # M-2, M-1:M
                # print(f"row_max: {row_max}")
        
        # 3차 시간복잡도 N-1 * (M + M *(i-N) + M-1)
    if N > 2:
        for i in range(1, N-1): # N-2 * N-i  (2차) if N  == 1, 1, 0
            for k in range(i+1, N):
                # print(f"row로 3분할: {sum(row_sum[0:i])} * {sum(row_sum[i:k])} * {sum(row_sum[k:N])}")
                row_max = max(sum(row_sum[0:i]) * sum(row_sum[i:k]) * sum(row_sum[k:N]), row_max) # 0-1 * 1-2* 2-N,
    
    return row_max

def sol(N, M, mat):    
    answer = divide_and_compute(N, M, mat)
    # 빠른 구현을 위하여 mat을 convert
    mat = [[mat[row][col] for row in range(N)] for col in range(M)]    
    N, M = M, N
    answer = max(divide_and_compute(N, M, mat), answer)
    
    return answer        
        

if __name__ == '__main__':    
    N, M = map(int, input().strip().split())
    mat = [list(map(int, input().strip())) for _ in range(N)]
    print(sol(N, M, mat))


"""
출처: tkqmfp26. 2차원 prefix_sum. 중복 더하기만 생각해주면 됌

풀이:
import sys
input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())
    nums = [[*map(int, list(input().rstrip()))] for  in range(N)]
    psum = [[0] * (M + 1) for  in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            psum[i][j] = nums[i - 1][j - 1] + psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1]
    ans = 0
    # 3개 넓이 구하기 - ㅏ, ㅗ, ㅓ, ㅜ
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            lu = psum[i][j]
            lb = psum[N][j] - lu
            ru = psum[i][M] - lu
            rb = psum[N][M] - lu - lb - ru
            ans = max((lu + lb) * ru * rb, lu * ru * (lb + rb), lu * lb * (ru + rb), (lu + ru) * lb * rb, ans)
    # 3개 넓이 구하기 - =
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            one = psum[i][M]
            two = psum[j][M] - one
            third = psum[N][M] - one - two
            ans = max(ans, one * two * third)
    # 3개 넓이 구하기 - ll
    for i in range(1, M - 1):
        for j in range(i + 1, M):
            one = psum[N][i]
            two = psum[N][j] - one
            third = psum[N][M] - one - two
            ans = max(ans, one * two * third)
    print(ans)
solve()"""