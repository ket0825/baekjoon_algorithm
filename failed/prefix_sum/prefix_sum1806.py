"""
부분합
시간 제한	메모리 제한
0.5 초 (하단 참고)	128 MB
문제
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

예제 입력 1 
10 15
5 1 3 5 10 7 4 9 2 8
예제 출력 1 
2
---
10 15
1 1 1 1 1 1 10 1 1 1

6
---
10 30
7 6 9 8 11 10 13 12 15 14

3
---
15 25
8 7 6 5 4 3 2 1 2 3 4 5 6 7 8

4
---
10 100
40 20 30 10 60 30 70 20 10 1

2
---
10 10
1 1 1 1 1 1 1 1 1 10

1
"""

import sys
input = sys.stdin.readline

# 로직 상 문제는 없는 것 같지만 코드 오류가 있기 쉬운 구조.
# def sol():
#     N, S = map(int, input().strip().split()) # N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)
#     # S를 만드는 것이 불가능하다면 0 출력.
#     sequence = list(map(int, input().strip().split()))
    
#     partial_sum = 0
#     reverse_sum = 0
#     traverse = [0]
#     reverse = [N]
#     min_count = 100001
#     for i in range(N):
#         partial_sum += sequence[i]
#         if partial_sum >= S:
#             min_count = min(min_count, i+1 - traverse[-1])
#             # print(f"min_count 갱신: {min_count}")
#             traverse.append(i+1)
#             partial_sum = 0
#         reverse_sum += sequence[N-1-i]
#         if reverse_sum >= S:
#             min_count = min(min_count, reverse[-1] - (N-1-i))
#             # print(f"min_count 갱신: {min_count}")
#             reverse.append(N-1-i)
#             reverse_sum = 0
#     # print(f"traverse: {traverse}")            
#     # print(f"reverse: {reverse}")
    
#     if min_count == 100001: # S 만들기 불가능
#         print(0)
#         return
#     elif min_count == 1:
#         print(1)
#         return
    
#     # 거꾸로 정렬하여 확인                            
#     for t in range(len(traverse)-1):
#         local_sum = 0         
#         sum_indices = 0               
#         for i in range(traverse[t+1] - 1, traverse[t] -1, -1):
#             sum_indices+=1
#             local_sum += sequence[i]
#             if local_sum >= S:                
#                 min_count = min(min_count, sum_indices)
#                 break
    
#     # 거꾸로 정렬하여 확인
#     for r in range(len(reverse)-1):
#         local_sum = 0
#         sum_indices = 0
#         for i in range(reverse[r+1], reverse[r]):            
#             local_sum += sequence[i]
#             sum_indices += 1            
#             if local_sum >= S:                
#                 min_count = min(min_count, sum_indices)
#                 break
    
#     print(min_count)

# 투포인터 사용! 누적합이니 바로 전까지만 포인터 이동.
def sol():
    N, S = map(int, input().strip().split()) # N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)
    # S를 만드는 것이 불가능하다면 0 출력.
    sequence = list(map(int, input().strip().split()))
    # print(S)
    left = 0
    current_sum = 0
    min_length = 100001
    
    for right in range(N):
        current_sum += sequence[right]
        # print(current_sum)
        
        while current_sum >= S and left <= right:            
            min_length = min(min_length, right - left + 1)            
            current_sum -= sequence[left]
            left+=1
    
    if min_length == 100001:
        print(0)
    else:
        print(min_length)


import sys
input = sys.stdin.readline

def sol2():
    N, S = map(int, input().strip().split())
    seq = list(map(int, input().strip().split()))
    answer = 100001
    
    left = 0
    right = 0
    psum = 0
    while left < N:
        # print(f"left: {left}, right: {right}, psum: {psum}")
        if S <= psum:
            answer = min(answer, right-left)
            # print(f"answer: {answer}")
            psum-=seq[left]
            left+=1
        else:
            if right < N:
                psum+=seq[right]
                right+=1
            else:
                psum-=seq[left]
                left+=1    

    if answer == 100001:
        print(0)
    else:
        print(answer)    
    

if __name__ == '__main__':
    sol2()
