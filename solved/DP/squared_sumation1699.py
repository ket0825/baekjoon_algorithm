"""
제곱수의 합

문제
어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다. 
예를 들어 11=3^2+1^2+1^2(3개 항)이다. 
이런 표현방법은 여러 가지가 될 수 있는데, 
11의 경우 11=2^2+2^2+1^2+1^2+1^2(5개 항)도 가능하다. 
이 경우, 수학자 숌크라테스는 “11은 3개 항의 제곱수 합으로 표현할 수 있다.”라고 말한다. 
(최소 항의 제곱수)
또한 11은 그보다 적은 항의 제곱수 합으로 표현할 수 없으므로, 
11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다.

주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 
그 항의 
최소개수
를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000)

출력
주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력한다.

예제 입력 1 
7
예제 출력 1 
4
예제 입력 2 
1
예제 출력 2 
1
예제 입력 3 
4
예제 출력 3 
1
예제 입력 4 
11
예제 출력 4 
3
예제 입력 5 
13
예제 출력 5 
2
출처
ICPC > Regionals > Asia Pacific > Korea > Nationwide Internet Competition > Seoul Nationalwide Internet Competition 2007 E번

문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: godmoon00
데이터를 추가한 사람: sbukkk, yukariko
"""

## 1. nlogn.
from math import floor, sqrt
import sys

input = sys.stdin.readline
LARGE_NUM = 1 << 20 # bigger than 100000.

def main():
    N = int(input().rstrip('\n'))
    K = floor(sqrt(N))
    candidates = [i**2 for i in range(1, K+1)]

    dp = [LARGE_NUM] * (N+1)    # 시행 횟수.

    for i in candidates:    # logn
        dp[i] = 1 # 1번에 가능하다는 뜻.

    for i in range(1, N+1): # nlogn...
        # if dp[N] != LARGE_NUM: # 더 작은 수가 있을 수 있음. 예) 12 => 3인데, 4로 나옴.
        #     break
        # elif dp[i] == LARGE_NUM: # 굳이 필요없는 조건. 1이 있기 때문.
        #     continue

        for k in candidates:
            if i+k > N:
                continue
            
            # if i+k == N:
            #     print(f'{i}는 {dp[i]}회, N은 {dp[i+k]}회')

            dp[i+k] = min(dp[i+k], dp[i]+1)

    print(dp[N])


if __name__ == '__main__':
    # print(100000* math.log2(100000)) => 166만.
    main()


##2. 수학적으로 for 문 없이 바로 진행. 출처: hen7878
# top-down 방식. 이렇게 하면 index 범위 벗어나는 것도 없음. 
# 이게 더 빠른 이유가 이건가...
N = int(input())

dp = [0] * 100001
for i in range(1, 100000):
    dp[i] = int(1e9)
    for j in range(1, int(i ** 0.5 + 1)): # logn
        dp[i] = min(dp[i], 1 + dp[i-j**2]) # 0으로 1을 통합시켜서 연산 아낌.

print(dp[N])

##3. 마찬가지. 출처: hui. 0을 이용하기도 함.
n = int(input())

lis = [0]*999999

for i in range(1,n+1):
    lis[i] = lis[i-1] + 1

    j=1
    while j*j <= i:
        lis[i] = min(lis[i], lis[i-j*j]+1)
        j+=1

print(lis[n])

## 4. nlogn. int로 내림 가능!
import sys

input = sys.stdin.readline
LARGE_NUM = 1 << 20 # bigger than 100000.

def main():
    N = int(input().rstrip('\n'))
    K = int(N**0.5)
    candidates = [i**2 for i in range(1, K+1)]

    dp = [LARGE_NUM] * (N+1)    # 시행 횟수.

    for i in candidates:    # logn
        dp[i] = 1 # 1번에 가능하다는 뜻.

    for i in range(1, N+1): # nlogn...
        # if dp[N] != LARGE_NUM: # 더 작은 수가 있을 수 있음. 예) 12 => 3인데, 4로 나옴.
        #     break
        # elif dp[i] == LARGE_NUM: # 굳이 필요없는 조건. 1이 있기 때문.
        #     continue

        for k in candidates:
            if i+k > N:
                continue
            
            # if i+k == N:
            #     print(f'{i}는 {dp[i]}회, N은 {dp[i+k]}회')

            dp[i+k] = min(dp[i+k], dp[i]+1)

    print(dp[N])


if __name__ == '__main__':
    # print(100000* math.log2(100000)) => 166만.
    main()
    
    


    




