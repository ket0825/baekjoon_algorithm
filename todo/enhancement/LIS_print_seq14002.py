"""
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
10 20 30 50
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: harinboy, kkw564
문제의 오타를 찾은 사람: jh05013
"""

# import sys
# input = sys.stdin.readline

# def main():
#     N = int(input().rstrip("\n"))
#     seq = [0] + list(map(int, input().rstrip('\n').split(" ")))

#     dp = [[i] for i in seq]
#     dp_num = [0] + [1]*N
    
#     # seq[i]
#     # 시퀀스 자체 출력.
#     for i in range(1, N+1):
#         for j in range(1, i):
#             if seq[i] <= seq[j]:    # 같거나 작으면 넘김 (nested if 로 인한 pattern 개선.)
#                 continue               

#             if dp_num[i] > dp_num[j] + 1:
#                 dp_num[i] = dp_num[i]            
#             else:    
#                 dp_num[i] = dp_num[j] + 1
#                 dp[i] = dp[j] + [dp[i][-1]]

    
#     max_length = 1
#     max_length_index = 1
#     for idx, i in enumerate(dp_num):
#         if max_length < i:
#             max_length_index = idx
#         max_length = max(max_length, i)
        
#     print(max_length)
#     print(*dp[max_length_index])
    


# if __name__ == '__main__':
#     main()


## 2. 미리 다 구하고, dp - 1인 부분을 역순으로 찾아나가는 방식.
# 그리고 bisect(nlogn)으로 구함.
import bisect
n = int(input())


numbers = [*map(int, input().split())]
dp = [] # sorted list 형태로 진행.
record = []

for i in numbers:
    p = bisect.bisect_left(dp, i)
    if p == len(dp):
        dp.append(i)
    else:
        dp[p] = i  # 처음값보다 작은 경우 dp를 수정하지만 어차피 0번째이기에 대체되어도 최장 수열 길이에는 지장이 없음.
    record.append(p)
ans_rev = []
max_p = len(dp)
for i in range(n-1, -1, -1):
    if record[i] == max_p-1:
        ans_rev.append(numbers[i])
        max_p -= 1
print(len(dp))
print(*ans_rev[::-1])