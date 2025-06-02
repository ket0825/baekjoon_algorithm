"""
감소하는 수
시간 제한	메모리 제한
1 초	512 MB

문제
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

입력
첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 N번째 감소하는 수를 출력한다.

예제 입력 1 
18
예제 출력 1 
42
예제 입력 2 
0
예제 출력 2 
0
예제 입력 3 
500000
예제 출력 3 
-1


"""

# 1. 일단 다 넣고, sort

# 2. 부분 sort.

import sys
input = sys.stdin.readline

def sol(N):
    order = 0
    prefix = [[j for j in range(i+1, 10)] for i in range(10)]
    answer = -1
    # 넣고 부분 sort.    
    cur_lst = list(range(10))
    l = []
    cur_len = 10    
    digits = 0
    while cur_lst:                
        cur_lst.sort()        
        # 먼저 숫자 확인
        if order + cur_len > N: # 순서에 현재 스택 길이를 더한 것이 N보다 크다면
            answer = cur_lst[N-order]
            break        
        
        order+=cur_len # 다음 순서는 cur_len 더한 것.
        cur_len = 0
        # 가장 맨 앞자리 확인 후 추가
        for item in cur_lst:            
            idx = item // 10 ** digits # 다음 idx 확인                
            for next_digit in prefix[idx]: # idx에 해당하는 prefix가 다음 자리수
                l.append(item + next_digit * 10 ** (digits+1))
                cur_len+=1
        cur_lst = l.copy()
        l.clear()
                
        digits+=1        
    
    print(answer)
 

if __name__ == '__main__':
    N = int(input().strip())
    sol(N)








