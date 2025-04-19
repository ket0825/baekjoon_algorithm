"""
숫자놀이
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	1297	609	474	48.715%
문제
홀순이(holsoon)와 짝순이(jjaksoon) 둘이서 숫자 게임을 한다. 예를 들어, 정수 1과 3이 주어지고, 이 둘을 통틀어 5번까지 마음대로 사용하여 그 합을 구하여 1,2,3,…을 만드는 놀이다. 이 경우 먼저 홀순이가 1 하나만을 사용하여 1을 만든다. 짝순이는 1+1로 1을 두 번 사용하여 2를 만들고, 다시 홀순이는 3을 만들어야하는데 1+1+1로 1을 세 번 사용하거나 3을 한 번 사용하여 3을 만든다. 짝순이는 1+1+1+1, 1+3으로 4를 만든다. 서로 번갈아서 상대방의 수보다 1이 큰 수를 만들어야 한다. 단, 1과 3을 통틀어 최대 5번 사용한다. 이런 식으로 진행하면 13까지는 만들 수 있지만 14를 만들지 못하게 되므로 짝순이가 졌다. 

숫자 게임에서 사용하는 정수 N개와 최대 사용 횟수 K가 주어질 때, 누가 어느 수에서 이기는지를 판별하는 프로그램을 작성해보자. 사용하는 정수에는 반드시 1이 포함된다. 그렇지 않으면 홀순이가 1을 만들지 못하므로 무조건 지게 된다. 1이 꼭 있으니 상대방이 만든 방법에 1만 한 번 더 쓰면 된다고 생각하기 쉽지만, 최대 사용 횟수가 정해져 있으므로, 이 방법이 수가 커지는 경우에는 잘 되지 않는다. 위에서 13을 홀순이가 만들었지만 짝순이는 최대 사용 횟수 때문에 14를 만들지 못하고 진다.

입력
첫째 줄에 숫자 게임에서 사용하는 정수의 수 N이, 둘째 줄에는 사용하는 정수가 크기 순으로 주어진다. 셋째 줄에는 최대 사용 횟수 K가 주어진다.

출력
첫째 줄에 누가 몇 번째 수에서 이겼는지를 출력한다. 예제에서는 짝순이가 14를 못 만들어서, 홀순이가 14에서 이겼다.

제한
1 ≤ N ≤ 1,000
1 ≤ K ≤ 50
숫자 게임에서 사용하는 정수는 1000보다 작거나 같은 자연수이고, 중복되는 수가 주어지지 않는다.
예제 입력 1 
2
1 3
5
예제 출력 1 
holsoon win at 14
"""

import sys
input = sys.stdin.readline


def sol(N, K, numbers):
    # 1 반드시 numbers에 존재.
    # 5만까지 가능.
    
    dp = [K+1] * 50001 # 사용 갯수를 나타냄.
    max_num = numbers[-1]
    
    # 하나만 사용한 것
    for num in numbers:
        dp[num] = 1        
    
    answer = f"jjaksoon win at 50001"
        
    for i in range(2, 50001):
        if i % max_num == 0:
            min_count = i // max_num
        else:
            min_count = i // max_num + 1            
            
        for num in numbers:
            if i-num > 0:
                dp[i] = min(dp[i], dp[i-num] + 1)
                if dp[i] == min_count:
                    break
            else:
                break
            
        # print(f"{i}번째: {dp[i]}")
        if dp[i] == K+1:
            if i % 2 == 0 :
                answer = f"holsoon win at {i}"
            else:
                answer = f"jjaksoon win at {i}"                
            break              
    
    print(answer)    

if __name__ == '__main__':
    N = int(input().strip())
    numbers = list(map(int, input().strip().split()))
    K = int(input().strip())
    # N = 1000
    # numbers = [i for i in range(1, 1001)]
    # K = 50
    numbers.sort()
    sol(N, K, numbers)