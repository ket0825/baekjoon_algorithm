"""
포도주 시식
시간 제한	메모리 제한	
2 초	128 MB	140223
문제
효주는 포도주 시식회에 갔다. 
그 곳에 갔더니, 
테이블 위에 다양한 포도주가 들어있는 포도주 잔이 일렬로 놓여 있었다. 
효주는 포도주 시식을 하려고 하는데, 
여기에는 다음과 같은 두 가지 규칙이 있다.

1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 
마신 후에는 원래 위치에 다시 놓아야 한다.
2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
효주는 될 수 있는 대로 많은 양의 포도주를 맛보기 위해서 
어떤 포도주 잔을 선택해야 할지 고민하고 있다. 
1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블 위에 놓여 있고, 
각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때, 
효주를 도와 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오. 

예를 들어 6개의 포도주 잔이 있고, 
각각의 잔에 순서대로 6, 10, 13, 9, 8, 1 만큼의 포도주가 들어 있을 때, 
첫 번째, 두 번째, 네 번째, 다섯 번째 포도주 잔을 선택하면 
총 포도주 양이 33으로 최대로 마실 수 있다.

입력
첫째 줄에 포도주 잔의 개수 n이 주어진다. (1 ≤ n ≤ 10,000) 
둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 
포도주의 양은 1,000 이하의 음이 아닌 정수이다.

출력
첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.

예제 입력 1 
6
6
10
13
9
8
1
예제 출력 1 
33

내 예제 2
5
10
1
10
1
10
예제 출력 2
30

내 예제 3
7
2
10
10
4
10
5
10
예제 출력
40

내 예제 4
6
100
100
1
1
100
100
예제 출력 4
400

6
1
2
3
4
5
6
내 답: 9
출력: 16

https://raejoonee.tistory.com/15 :반례 케이스 모음집

출처
빠진 조건을 찾은 사람: keith
데이터를 추가한 사람: lhr4884
"""
## 1. 최대가 되는 규칙 찾음.
# 1. 안마시면 반드시 다음에 마실 것 => 틀림. 추가 조건 필요.
# 2. 2번 연속으로 마시면 다음에는 쉴 것.
# 일단 포기. 다음에 품.
# import sys
# input = sys.stdin.readline

# def main():
#     N = int(input().rstrip('\n')) #(1 ≤ n ≤ 10,000) 

#     wine_volume = [0] + [int(input().rstrip('\n')) for _ in range(N)] + [0, 0] # 1,000 이하의 음이 아닌 정수이다.
#     # 마지막 0은 아래 중 안마시고 마시는 부분 때문에 추가함.

#     dp = [[0, 0, 0] for _ in range(N+1)]

#     # 3가지 경우만 최대 가능. 
#     # O X 
#     # O O
#     # X O
#     # 뒤에 보는 범위: 최대 앞에 2개까지

#     dp[1] = [wine_volume[1], wine_volume[1], 0]
#     if N > 1:
#         dp[2] = [wine_volume[1], wine_volume[1] + wine_volume[2], wine_volume[2]]
#         for i in range(3, N+1):
#            for j in range(3):
#                 if dp[i-1][j] == dp[i-2][j]: # 전에 안마셨으면 (마신 양 변화 없음)
#                    # 이번부터 O X O 가 X O O보다 크거나 같으면 마시기.
#                     if wine_volume[i] + wine_volume[i+2] >= wine_volume[i+1] + wine_volume[i+2]:
#                         dp[i][j] = dp[i-1][j] + wine_volume[i]
#                     # X O O가 더 크면 안마시기.
#                     else:
#                         dp[i][j] = dp[i-1][j]
#                 elif dp[i-1][j] != dp[i-2][j] and dp[i-3][j] != dp[i-2][j]: # 연속으로 마셨으면
#                     # 반드시 쉬기.
#                     dp[i][j] = dp[i-1][j]  
#                 else: # X O 이면                  
#                     # 이후 가능한 것: O X, X O
#                     if wine_volume[i] >= wine_volume[i+1]: # 똑같아도 일단 먹는게 나음.
#                         dp[i][j] = dp[i-1][j] + wine_volume[i]
#                     else:
#                         dp[i][j] = dp[i-1][j]

#     print(max(dp[N]))


# if __name__ == '__main__':
#     main()


## 2. 고정된 값들과 dp 모두 잘 활용해야만 한다...
import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip('\n')) #(1 ≤ n ≤ 10,000) 

    wine_volume = [0] + [int(input().rstrip('\n')) for _ in range(N)]+[0]# 1,000 이하의 음이 아닌 정수이다.
    dp = [0 for _ in range(N+1)]
    dp[1] = wine_volume[1]
    if N > 1:
        dp[2] = wine_volume[1] + wine_volume[2]
    if N > 2:
        dp[3] = max(dp[1] + wine_volume[3], dp[2], wine_volume[2] + wine_volume[3])
    if N > 3:
        for i in range(4, N+1):            
            dp[i] = max(dp[i-2] + wine_volume[i], dp[i-1], dp[i-3]+wine_volume[i]+wine_volume[i-1])
            #   . X O
            #       X
            # . X O O
                        
    print(dp[N])


if __name__ == '__main__':
    main()