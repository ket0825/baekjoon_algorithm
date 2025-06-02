"""
IQ Test
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	17324	3724	3011	22.067%
문제
IQ Test의 문제 중에는 공통된 패턴을 찾는 문제가 있다. 수열이 주어졌을 때, 다음 수를 찾는 문제이다.

예를 들어, 1, 2, 3, 4, 5가 주어졌다. 다음 수는 무엇인가? 당연히 답은 6이다. 약간 더 어려운 문제를 보면, 3, 6, 12, 24, 48이 주어졌을 때, 다음 수는 무엇인가? 역시 답은 96이다.

이제 제일 어려운 문제를 보자.

1, 4, 13, 40이 주어졌을 때, 다음 수는 무엇일까? 답은 121이다. 그 이유는 항상 다음 수는 앞 수*3+1이기 때문이다.

은진이는 위의 3문제를 모두 풀지 못했으므로, 자동으로 풀어주는 프로그램을 작성하기로 했다. 항상 모든 답은 구하는 규칙은 앞 수*a + b이다. 그리고, a와 b는 정수이다.

수 N개가 주어졌을 때, 규칙에 맞는 다음 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 N개의 수가 주어진다. 이 수는 모두 절댓값이 100보다 작거나 같은 정수이다.

출력
다음 수를 출력한다. 만약 다음 수가 여러 개일 경우에는 A를 출력하고, 다음 수를 구할 수 없는 경우에는 B를 출력한다.

예제 입력 1 
4
1 4 13 40
예제 출력 1 
121
예제 입력 2 
5
1 2 3 4 5
예제 출력 2 
6
예제 입력 3 
5
3 6 12 24 48
예제 출력 3 
96
예제 입력 4 
1
0
예제 출력 4 
A
예제 입력 5 
2
-1 2
예제 출력 5 
A
예제 입력 6 
2
57 57
예제 출력 6 
57
예제 입력 7 
4
16 -8 4 -2
예제 출력 7 
B
예제 입력 8 
5
6 5 4 3 1
예제 출력 8 
B
예제 입력 9 
4
-12 12 -36 60
예제 출력 9 
-132

3
-8 -8 -8

-8
"""

# a, b 모두 정수.
# 요소 모두 절댓값이 100보다 작거나 같음.
# 그냥 a, b를 -100~100까지 브루트포스하고, 만족하는 순서쌍만 대입.
# 2
# 57 57
# a = 0, b = 57. a = 1, b = 0 = 57.
# 아무튼 57밖에 안되기에 괜찮음.

import sys
# sys.setrecursionlimit(100000000)
from collections import deque
input = sys.stdin.readline

# def sol(N, arr):
#     if N < 2:
#         print("A")
#         return
    
#     # 순서쌍 채우기
#     ordered_pair = deque([])
#     for a in range(-100, 101): # 곱셈은 -100, 101
#         for b in range(-100, 101): # 덧셈은 -2000
#             ordered_pair.appendleft((a, b, 0))
#     # a*x_n + b = x_n+1 확인하기
#     cur_count = 0
#     for i in range(N-1):
#         while ordered_pair:
#             a, b, count = ordered_pair.pop()
#             if cur_count != count: # 다르면 x
#                 cur_count+=1
#                 ordered_pair.append((a, b, count)) # 우측에 다시 넣음
#                 break
#             if a*arr[i] + b == arr[i+1]:
#                 # print(f"후보군 {count}째: {a}, {b}")
#                 ordered_pair.appendleft((a, b, count+1))
    
#     if not ordered_pair:
#         print("B")
#         return
    
#     # 가장 마지막 만족시키는 것들 확인하기
#     a, b, count = ordered_pair.pop()
#     # print(f"최종 후보군: {a}, {b}")
#     objective = a*arr[N-1] + b
#     answer = objective
#     # 순서쌍 존재함.
#     while ordered_pair:
#         a, b, count = ordered_pair.pop()
#         # print(f"최종 후보군: {a}, {b}")
#         if objective != a*arr[N-1] + b:
#             answer = "A"
#             break
    
#     print(answer)    

import sys
input = sys.stdin.readline

def sol(N, arr):
    if N == 1:
        print("A")
    elif N == 2:
        if arr[0] != arr[1]:
            print("A")
        else: # 같은 수이면 계속 그 수로 이어짐.
            print(arr[1]) 
    else: # N >= 3        
        if arr[0] - arr[1] != 0: # ZeroDivisionError          
            a = (arr[1] - arr[2]) / (arr[0] - arr[1])
            if a != int(a):
                print("B")
                return
            a = int(a)
            b = arr[1] - arr[0] * a
            if N == 3:
                print(a*arr[2] + b)            
            else:
                for i in range(2, N-1):
                    if a*arr[i] + b != arr[i+1]:
                        print("B")
                        return
                    
                print(a*arr[N-1] + b)
        else:            
            for i in range(2, N):
                if arr[0] != arr[i]: # 하나라도 값이 다르면 답이 없음.
                    print("B")
                    return
            # 쭈욱 같은 것이기에 다음 것도 같은 것.
            print(arr[0])
        

if __name__ == '__main__':
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    sol(N, arr)