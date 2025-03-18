"""
문제
    +---+        
    | D |        
+---+---+---+---+
| E | A | B | F |
+---+---+---+---+
    | C |        
    +---+        
주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다. 위의 전개도를 수가 밖으로 나오게 접는다.

A, B, C, D, E, F에 쓰여 있는 수가 주어진다.

지민이는 현재 동일한 주사위를 N3개 가지고 있다. 이 주사위를 적절히 회전시키고 쌓아서, N×N×N크기의 정육면체를 만들려고 한다. 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.

N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 둘째 줄에 주사위에 쓰여 있는 수가 주어진다. 위의 그림에서 A, B, C, D, E, F에 쓰여 있는 수가 차례대로 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, 쓰여 있는 수는 50보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.

예제 입력 1 
2
1 2 3 4 5 6
예제 출력 1 
36
예제 입력 2 
3
1 2 3 4 5 6
예제 출력 2 
69
예제 입력 3 
1000000
50 50 50 50 50 50
예제 출력 3 
250000000000000
예제 입력 4 
10
1 1 1 1 50 1
예제 출력 4 
500
"""
import sys
from itertools import combinations

input = sys.stdin.readline

def sol():
    N = int(input().strip())
    dice = list(map(int, input().strip().split()))
    # 1면: 4*(N-2)*(N-1) + (N-2)*(N-2)
    # 2면: 4*(N-2) + 4*(N-2)
    # 3면: 4
    
    def calculate_threeside(): # 3면 선택 중에서 서로 건너편이 포함되지 않은 것
        # 건너편: index 합이 5.
        min_val = 3*1000000
        for comb in combinations(range(6), 3):
            if (
                comb[0] + comb[1] == 5
                or comb[1] + comb[2] == 5
                or comb[2] + comb[0] == 5
                ):
                continue            
            min_val = min(min_val, sum(map(lambda x: dice[x], comb)))
            
        # print(f"3면 min_val: {min_val}")
        return min_val
    
    def calculate_twoside(): # 2면 선택 중에서 서로 건너편이 포함되지 않은 것
        # 건너편: index 합이 5.
        min_val = 2*1000000
        for comb in combinations(range(6), 2):
            if comb[0] + comb[1] == 5:
                continue
            min_val = min(min_val, sum(map(lambda x: dice[x], comb)))
        
        # print(f"2면 min_val: {min_val}")        
        return min_val 
    
    def calculate_oneside():
        return min(dice)        
    
    answer = 0
    if N > 1:                
        answer = 4*calculate_threeside() \
                + (4*(N-1) + 4*(N-2)) * calculate_twoside() \
                + (4*(N-2)*(N-1) + (N-2)*(N-2)) * calculate_oneside()                        
    else:
        answer = sum(dice) - max(dice)
        
    print(answer)
        

if __name__ == '__main__':
    sol()
