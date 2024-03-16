"""
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
예제 입력 2
14
3 2 4 3 2 1 5 7 6 7 9 8 6 7
예제 출력 1 
6
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: harinboy

비슷한 문제
11054번. 가장 긴 바이토닉 부분 수열
11055번. 가장 큰 증가하는 부분 수열
11722번. 가장 긴 감소하는 부분 수열
12015번. 가장 긴 증가하는 부분 수열 2
12738번. 가장 긴 증가하는 부분 수열 3
14002번. 가장 긴 증가하는 부분 수열 4
14003번. 가장 긴 증가하는 부분 수열 5
"""

# 요구사항에 따라 적절한 알고리즘 설계하기.
# 문제에서 가장 먼저 확인해야 하는 내용은 시간제한(수행시간 요구사항)임
# 시간제한이 1초인 문제를 만났을 때 일반적인 기준은 다음과 같습니다
# N의 범위가 500인 경우: 시간 복잡도가 O(N³)인 알고리즘을 설계하면 문제를 풀 수 있음
# N의 범위가 2,000인 경우: 시간 복잡도가 O(N²)인 알고리즘을 설계하면 문제를 풀 수 있음
# N의 범위가 100,000인 경우: 시간 복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 풀 수 있음
# N의 범위가 10,000,000인 경우: 시간 복잡도가 O(N)인 알고리즘을 설계하면 문제를 풀 수 있음

# # 1. N^3 algorithm (brute force) => 연산 초과...
# import sys
# input = sys.stdin.readline

# def main():
#     N = int(input().rstrip("\n"))
#     seq = list(map(int, input().rstrip("\n").split(" ")))
#     # dfs로 하기엔 너무 깊음. 최대 1000 depth.
#     max_length = 0
    
#     for i in range(N):
#         temp = [[seq[i], i]]    # value and index.
#         current_pos = i
#         while temp:
#             for j in range(current_pos+1, N):
#                 if seq[j] > temp[-1][0]: 
#                     temp.append([seq[j], j])
#             max_length = max(max_length, len(temp))
            
#             current_pos = temp.pop()[1]
    
#     print(max_length)


# if __name__ == '__main__':
#     main()

"""
14
3 2 4 3 2 1 5 7 6 7 9 8 6 7
6

8
2 5 3 6 4 7 5 8
5

"""
# 2. another solution. 해결 실패..
# import sys
# input = sys.stdin.readline

# def main():
#     N = int(input().rstrip("\n"))
#     seq = list(map(int, input().rstrip("\n").split(" ")))
#     # dfs로 하기엔 너무 깊음. 최대 1000 depth.
    
#     dp = [0] * (N)  # 지금까지중 가장 컸던 것으로 채워나가면 됨.
#     dp = [[0]*(1001) for _ in range(N)] # N번 진행함.

#     dp_max_num = [0] * 1001

#     # dp[0] = seq[0]  
#     # 포함하냐, 안포함하냐의 문제이기도 함. 만약 비트마스킹이면? 2*1000... ㅌㅌ

#     max_length = 0

#     dp[0][seq[0]] = 1
#     dp_max_num[seq[0]] = seq[0]

#     for i in range(1, N):  # 지금 문제임...
#         seq_num = seq[i]
#         dp[i][seq_num] = max(1, dp[i-1][seq_num]) # 1이나 전번째 중에서 더 큰걸로...
#         dp_max_num[seq_num] = max(seq_num, dp_max_num[seq_num])

#         # early pruning 하나.
#         if max_length > N-i + max(dp[i]): # max 연산을 또 해야해서 굳이... 라는 생각...?
#             break
        
#         if i == 8:
#             print('here')

#         for k in range(1, 1001): # 일단 max_num을 순회하자.
#             dp[i][k] = max(dp[i][k], dp[i-1][k])
#             if k >= seq_num or dp[i][k] == 0:
#                 continue
#             if k < seq_num and dp_max_num[k] > seq_num and seq[:i].count(seq_num) == 0: # k번째 max값이 seq_num보다 더 작은데, k가 seq_num보다 더 작은 경우.
#                 # 그리고 그 값이 언제 들어왔는지도 확인해야 함...
#                 # k_idx = seq.index(k)
#                 # for j in seq[k_idx+1:i]: # i까지 나온 것 확인. # 2 4 3 7 8 9 4 6 8 5 
#                 #     if seq_num < j < dp_max_num[k]:
#                 #         dp_max_num[k] = seq_num
#                 #         break

#                 dp_max_num[k] = seq_num
#                 # dp[i][k] = dp[i-1][k]

#             elif k < seq_num and dp_max_num[k] < seq_num and dp[i-1][k] != 0: # k보다 seq_num이 더 크고, max_num보다도 크면 증가 형태임. 단, 나온 적 있어야 함.
#                 dp_max_num[k] = seq_num  # k의 최댓값 갱신.
#                 dp[i][k] = dp[i-1][k] + 1  # i번째는 i-1번째 횟수의 것에서 1을 더해줌.
        
#         # max_length = max(*dp[i], max_length)

#     print(max(dp[N-1]))


# if __name__ == '__main__':
#     main()

import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip("\n"))
    seq = [0] + list(map(int, input().rstrip("\n").split(" ")))

    dp = [1] * (N+1)    # 각 위치에서 하나씩 나옴.

    for i in range(1, N+1):
        for j in range(1, i):
            if seq[i] > seq[j]: # 전번째보다 더 크다면,
                dp[i] = max(dp[i], dp[j]+1) # 이전 것과 현재 것보다 더 큰 것.      
    
    print(max(dp))

if __name__ == '__main__':
    main()

## 2. nlogn algorithm...
"""LIS(Longest Increasing Subsequence, 최장 증가 수열)문제를 
O(nlogn) 시간 복잡도로 해결하는 방법은 
이진 탐색과 동적 프로그래밍을 결합한 방식입니다. 

구체적인 단계는 다음과 같습니다.

1. 길이를 저장할 배열 dp를 생성하고, 
dp[0]을 입력 배열의 첫 번째 원소로 초기화합니다.

2. 입력 배열의 두 번째 원소부터 순회하면서 다음을 수행합니다. 
a. dp 배열에서 현재 원소보다 작은 가장 큰 값의 인덱스를 찾습니다. 
이를 위해 이진 탐색을 사용합니다. 

b. 해당 인덱스에 현재 원소를 대입합니다. 
c. 만약 해당 인덱스가 dp 배열의 마지막 인덱스보다 크다면, 
dp 배열의 길이를 1 증가시킵니다.

최종적으로 dp 배열의 길이가 LIS의 길이가 됩니다.
"""
from bisect import bisect_left

def lis(arr):
    if not arr:
        return 0

    dp = [0] * (len(arr) + 1)
    length = 1  # 제일 길었던 길이.
    dp[1] = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > dp[length]: # 일단 arr[i]가 dp[length]보다 크면 더 길게 할 수 있으니 올리고, 그 새로운 자리에 arr[i]를 한다.
            length += 1
            dp[length] = arr[i]
        else: # 더 크지 않다면, 지금까지 dp 중 왼쪽부터 가장 큰 쪽에 대신하여 넣어준다. (어차피 길이만 중요하니)
            idx = bisect_left(dp, arr[i], 1, length) 
            # 원래 dp 리스트에서 i번쨰 원소가 1부터 length 사이에서 어디에 끼면 되냐.
            dp[idx] = arr[i]

    return length

lis([1,100,2,50,60,3,5,6,7,8])