"""
카드 섞기
시간 제한	메모리 제한
2 초	128 MB
문제
지민이는 카지노의 딜러이고, 지금 3명의 플레이어(0, 1, 2)가 있다. 이 게임은 N개의 카드를 이용한다. (0 ~ N-1번)

일단 지민이는 카드를 몇 번 섞은 다음에, 그것을 플레이어들에게 나누어 준다. 0번째 위치에 있던 카드가 플레이어 0에게 가고, 1번째 위치에 있던 카드는 플레이어 1에게 가고, 2번째 위치에 있던 카드는 플레이어 2에게 가고, 3번째 위치에 있던 카드는 플레이어 0에게 가고, 이런식으로 카드를 나누어 준다. 하지만, 지민이는 약간 사기를 치려고 한다.

지민이는 처음에 카드를 섞기 전에 카드의 순서를 알고 있고, 이 정보를 이용해 각 카드가 특정한 플레이어에게 보내지게 할 것이다.

카드를 한 번 섞을 때는 주어진 방법을 이용해서만 섞을 수 있고, 이 방법은 길이가 N인 수열 S로 주어진다. 카드를 한 번 섞고 나면 i번째 위치에 있던 카드는 S[i]번째 위치로 이동하게 된다.

각 카드가 어떤 플레이어에게 가야 하는지에 대한 정보는 길이가 N인 수열 P로 주어진다. 맨 처음 i번째 위치에 있던 카드를 최종적으로 플레이어 P[i] 에게 보내야한다.

지민이가 목적을 달성하기 위해 필요한 카드 섞는 횟수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. N은 3보다 크거나 같고, 48보다 작거나 같은 3의 배수이다.

둘째 줄에 길이가 N인 수열 P가 주어진다. 수열 P에 있는 수는 0, 1, 2 중 하나이다.

셋째 줄에 길이가 N인 수열 S가 주어진다. 수열 S에 있는 수는 모두 N-1보다 작거나 같은 자연수 또는 0이고 중복되지 않는다.

출력
첫째 줄에 몇 번 섞어야 하는지 출력한다. 만약, 섞어도 섞어도 카드를 해당하는 플레이어에게 줄 수 없다면, -1을 출력한다.

예제 입력 1 
3
2 0 1
1 2 0
예제 출력 1 
2
예제 입력 2 
6
0 1 2 0 1 2
1 4 0 3 2 5
예제 출력 2 
0
예제 입력 3 
3
1 0 2
0 2 1
예제 출력 3 
-1
예제 입력 4 
12
1 1 2 0 2 0 1 0 2 2 1 0
5 0 9 7 1 8 3 10 4 11 6 2
예제 출력 4 
59
"""

import sys
# sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def sol(N, P, S, cards):
    # 최대: N을 합으로 하는 수 집합 중 만들 수 있는 최대 공배수의 최대까지.
    # 그냥 N 배열을 계속 기록해둘까... 똑같은 것이 나오면 끝내기! 수학적 규칙은 쉽지 않음
    cards_to_player = [i % 3 for i in range(N)]
    cards_to_player_mapper = lambda x: cards_to_player[x] # x를 넣으면 분배되게끔.
    shuffle_cards_mapper = lambda x: S[x]
    answer = 0        
    original = cards[:]    
    
    while True:        
        # 이것도 early return 가능.
        if P == list(map(cards_to_player_mapper, cards)):
            break
        
        cards = list(map(shuffle_cards_mapper, cards))        
        answer+=1 
                        
        if original == cards:            
            answer = -1
            break        
            
    return answer

if __name__ == '__main__':
    N = int(input().strip())
    P = list(map(int, input().strip().split())) # i번째 카드는 P[i]가 가져야 함.
    S = list(map(int, input().strip().split())) # i번째 카드는 S[i] 위치로 가야 함.    
    cards = [i for i in range(N)]
    
    print(sol(N, P, S, cards))    