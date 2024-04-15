"""
연속합 2
2 초	512 MB	23753	7250	5396	29.830%
문제
n개의 정수로 이루어진 임의의 수열이 주어진다. 
우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 
가장 큰 합을 구하려고 한다. 

단, 수는 한 개 이상 선택해야 한다. 
또, 수열에서 수를 하나 제거할 수 있다. (제거하지 않아도 된다)

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자.
여기서 수를 제거하지 않았을 때의 정답은 12+21인 33이 정답이 된다.

만약, -35를 제거한다면, 
수열은 10, -4, 3, 1, 5, 6, 12, 21, -1이 되고, 
여기서 정답은 10-4+3+1+5+6+12+21인 54가 된다.

입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 
둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 
수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.

예제 입력 1 
10
10 -4 3 1 5 6 -35 12 21 -1
예제 출력 1 
54

예제 입력 2
5
1 4 5 3 2
예제 출력 2 
15

예제 입력 3
3
-1 -2 -3
예제 출력 3 
-1
예제 입력 4
10
10
1 -2 5 -4 3 -10 9 -8 7 -6
예제 출력 4 
16


출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: dj910401, ha_ram, solarmagic
문제의 오타를 찾은 사람: jh05013
잘못된 데이터를 찾은 사람: tncks0121
"""
## 1. N은 최대 100000이므로, 최소 NlogN. n을 하나하나씩 빼면 N^2이므로 안됨. 
# 동적으로 dp memo 관리.
import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip('\n')) # n(1 ≤ n ≤ 100,000) 
    seq = [0] + list(map(int, input().rstrip('\n').split(" "))) # -1000 <= a_i <= 1000
    # N = 100050
    # seq = [0]
    # for _ in range(50):
    #     for i in range(-1000, 1001):
    #         seq.append(i)

    

    dp = [0]*(N+1)    # 각각 현재 자신의 값을 memoization.
    dp[1] = seq[1]
    local_max_index = 1
    max_values = []
    max_values.append(seq[1]) # 최댓값 따로 관리.
    index_set = set([1])
    
    if N > 1:
        for i in range(2, N+1):
            if dp[1] + seq[i] < seq[i]:
                dp[1] = 0  # 아래에서 seq[i] 더하여 처리 가능.
            print(f"index set 길이: {len(index_set)}")
            local_max = -10000
            for s in index_set:                
                dp[s] += seq[i]
                if dp[s] > local_max:
                    local_max_index = s
                    local_max = dp[s]

            # copy된 것에서 index_set을 정리함. index set은 최대 3개까지임.
            for s in index_set.copy():                
                if dp[s] <= local_max and s != 1 and local_max_index != s: # 1번은 원본이기에 지우면 안됨. 동시에 현 max_index와 달라야 함.
                    index_set.discard(s)            
                                   
            if seq[i] < 0:
                index_set.add(i)
                dp[i] = max(dp[1] - seq[i], seq[i]) # dp[1]에서 현재값 뺀 것과, 그냥 현재 것부터 시작하는 것 둘 중 하나.

            max_values.append(local_max)
    
    print(max(max_values))


if __name__ == '__main__':
    main()

## 2. 원래 정석 dp 방법. 출처: jws314046
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

dp = [[0] * n for _ in range(2)]
dp[0][0] = a[0]
dp[1][0] = -1000

for j in range(1, n):
    dp[0][j] = max(dp[0][j-1] + a[j], a[j])
    dp[1][j] = max(dp[0][j-1], dp[1][j-1] + a[j])



print(max(max(dp[0]),max(dp[1])))
