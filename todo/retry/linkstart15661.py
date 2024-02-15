## nC2 등의 계산에서 itertool.combination을 쓰면 생각보다 매우 느리다.
## 그냥 2중 for문을 쓰는 것이 나을 수 있다.
"""
문제
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 
축구는 평일 오후에 하고 의무 참석도 아니다. 
축구를 하기 위해 모인 사람은 총 N명이다.
이제 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.
두 팀의 인원수는 같지 않아도 되지만, 한 명 이상이어야 한다.
BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고,
아래와 같은 능력치를 조사했다. 
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 
팀에 더해지는 능력치이다. 
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. 
Sij는 Sji와 다를 수도 있으며, 
i번 사람과 j번 사람이 같은 팀에 속했을 때, 
팀에 더해지는 능력치는 Sij와 Sji이다.

N=4이고, S가 아래와 같은 경우를 살펴보자.

i\j	1	2	3	4
1	 	1	2	3
2	4	 	5	6
3	7	1	 	2
4	3	4	5	 
예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에
 두 팀의 능력치는 아래와 같다.

스타트 팀: S12 + S21 = 1 + 4 = 5
링크 팀: S34 + S43 = 2 + 5 = 7
1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 
두 팀의 능력치는 아래와 같다.

스타트 팀: S13 + S31 = 2 + 7 = 9
링크 팀: S24 + S42 = 6 + 4 = 10
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 
최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 
2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 
링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

입력
첫째 줄에 N(4 ≤ N ≤ 20)이 주어진다. 
둘째 줄부터 N개의 줄에 S가 주어진다. 
각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. 
Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 
100보다 작거나 같은 정수이다.

출력
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

예제 입력 1 
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
예제 출력 1 
0
예제 입력 2 
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
예제 출력 2 
2
예제 입력 3 
8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
예제 출력 3 
1
예제 입력 4 
5
0 3 1 1 1
3 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0
예제 출력 4 
0
"""

import sys
from itertools import combinations
input = sys.stdin.readline
# min_value = 1000000
def main():
    N = int(input().rstrip("\n")) # N(4 ≤ N ≤ 20)
    S = [list(map(int, input().rstrip("\n").split(" "))) for _ in range(N)]
    # 핵심: 인원이 2대 5여도 가능하다는 것임.
    min_value = 1000000
    # def dfs_from_middle(): # 중간부터 dfs 시작.
    # team_A_players_cnt = N // 2
    # team_B_players_cnt = N - team_A_players_cnt
    # global min_value

    
    for team_A_players_cnt in range((N//2) + 1, 1, -1): # 절반까지만 진행하면 되고, 점점 멀어지도록 하는게 더 나음.
        for A_combi in combinations(range(N), team_A_players_cnt): # 선수들 뽑힘 (index. 순서대로)
            team_A_score = 0
            team_B_score = 0
            B_combi = [player_idx for player_idx in range(N) if player_idx not in A_combi]
            
            if len(A_combi) != 1:   
                for i,j in combinations(A_combi, 2):
                    team_A_score += S[i][j] + S[j][i]
            
            if len(B_combi) != 1:
                for i,j in combinations(B_combi, 2):
                    team_B_score += S[i][j] + S[j][i]
            
            min_value = min(min_value, abs(team_A_score - team_B_score))
            if min_value == 0:
                print(min_value)
                exit()                
    
    print(min_value)                

    # 가능한 combination 다 해야 함. 1:19, 2:18 등등... 20C1*(19C2*2+ 1C2*2(안됨))+ 20C2*(18C2*2+2C2*2) + ... + 20C(n//2)*((n//2)C2*2+(n -n//2)C2)
    # 근데 처음엔 반띵으로 시작하고, 줄여나가는 식으로 할 수 있을까? 
    # 그게 제일 빨리 찾을 확률이 높음. (20C1+ 20C2 + ... + 20C20 = 2^20..?) == 1048576
    # 가능한 조합 => 19P2....18P2*2P2+2+ ... =>  dot product하면...? 232484760 정도 나와서 절대 안되는데 왜 되는거지?
    # 계산식:
    ## max case 계산
    # import math
    # n = 20
    # total = 0
    # for i in range(1, n//2+1):
    #     try:
    #         pick_a = math.comb(i,2)*2
    #     except:
    #         pick_a = 1
    #     try:
    #         pick_b = math.comb(n-i,2)*2
    #     except:
    #         pick_b = 1
        
    #     total += math.comb(n,i)*(pick_a*2+pick_b*2)
    # print(total)

if __name__ == "__main__": 
    main()


## 2. 비트마스킹.. 많이 봐야 알 듯... 지금은 이해 잘 안됨.
# import sys
# input = sys.stdin.readline

# N = int(input())
# S = [[0]*N for _ in range(N)]
# for i in range(N):
#     arr = list(map(int, input().split()))
#     for j in range(N):
#         S[i][j] += arr[j]
#         S[j][i] += arr[j]

# ans = sys.maxsize
# for i in range(1, 1 << N-1): # 1부터 2^(N-1) - 1까지.
#     flag = True
#     start, sp = [], 0
#     link, lp = [], 0
#     for j in range(N):  # N까지 index인 j.
#         if i & (1 << j): # 1 & 1    # 다음엔 1 & 2. (&가 없음.)
#             if start:   # 처음엔 x.
#                 for k in start: # 0번째 row의 start의 요소의 column....
#                     sp += S[j][k]
#             start.append(j) # start에 j가 append(0)
#         else:   
#             if link:
#                 for k in link:
#                     lp += S[j][k]
#             link.append(j)
#     ans = min(ans, abs(sp-lp))
# print(ans)