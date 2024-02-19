"""
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다.
축구는 평일 오후에 하고 의무 참석도 아니다. 
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 
이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 
아래와 같은 능력치를 조사했다. 
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때,
팀에 더해지는 능력치이다.
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다.
Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때,
팀에 더해지는 능력치는 Sij와 Sji이다.
N=4이고, S가 아래와 같은 경우를 살펴보자.

i\j	1	2	3	4
1	 	1	2	3
2	4	 	5	6
3	7	1	 	2
4	3	4	5	 
예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

스타트 팀: S12 + S21 = 1 + 4 = 5
링크 팀: S34 + S43 = 2 + 5 = 7
1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

스타트 팀: S13 + S31 = 2 + 7 = 9
링크 팀: S24 + S42 = 6 + 4 = 10
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 
최소로 하려고 한다. 
위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면
스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 
이 값이 최소이다.

입력
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다.
둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

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

예제 입력 2 (1,3,6 / 2, 4, 5가 최대임.)
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
1,3,6: 1+2+3+5+1+5 = 17
2,4,5: 2+3+4+4+2+4 = 19

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

"""

# import sys
# import itertools
# input = sys.stdin.readline

# def main():
#     N = int(input().rstrip("\n")) # N은 짝수임. N(4 ≤ N ≤ 20, N은 짝수)
#     abilty_board = [list(map(int, input().rstrip("\n").split(" "))) for _ in range(N)]
#     # team_A_abilty = 0 # (1,2,3,4) 한 팀의 조합을 뽑으면, 나머지 팀의 조합이 자동으로 나옴.
#     # team_B_abilty = 0 # (5,6,7,8) 최대 20C10 = 184756

#     global power_diff
#     power_diff = 1000000

#     def score_calculate(team_A): # 점수 계산은 permutation

#         team_A_abilty = sum(abilty_board[i][j] for i, j in itertools.permutations(team_A, 2))
#         team_B = []
#         for i in range(N):
#             if i not in team_A:
#                 team_B.append(i)

#         team_B_abilty = sum(abilty_board[i][j] for i, j in itertools.permutations(team_B, 2))
#         return abs(team_A_abilty-team_B_abilty)

#     # def combination(stack:list, start:int):
#     #     if len(stack) == int(N/2):
#     #         # score_calculate()
#     #         print(stack)
#     #         return
        
#     #     for i in range(start if start <= N else N, N):
#     #         if i not in stack:
#     #             combination(stack+[i], start+1)
#     #             # combination(stack, start)
#     #         start+=1

#     def combination(team_A:list, start:int):
#         if len(team_A) == int(N/2):
#             global power_diff
#             power_diff = min(score_calculate(team_A), power_diff)
#             if power_diff == 0:
#                 print(power_diff)
#                 exit()
#             # print(team_A)
#             return
        
#         if start >= int(N):
#             return
        
#         combination(team_A+[start], start+1)
#         combination(team_A, start+1)
  
#     combination([],0)
    
#     if power_diff != 0:
#         print(power_diff)

# if __name__ == "__main__":
#     main()

## 2. 바로 한번에 계산하는 듯. 이해가기 쉬운 코드는 아님. 그리고 한 함수 내부에 너무 동작이 많음.
# def go(index, first, second):
#     if index == n:
#         if len(first) != n // 2:
#             return -1
#         if len(second) != n // 2:
#             return -1
#         t1 = 0
#         t2 = 0
#         for i in range(n // 2):
#             for j in range(n // 2):
#                 if i == j:
#                     continue
#                 t1 += s[first[i]][first[j]]
#                 t2 += s[second[i]][second[j]]
#         diff = abs(t1 - t2)
#         return diff
#     if len(first) > n // 2:
#         return -1
#     if len(second) > n // 2:
#         return -1
#     ans = -1
#     t1 = go(index + 1, first + [index], second)
#     if ans == -1 or (t1 != -1 and ans > t1):
#         ans = t1
#     t2 = go(index + 1, first, second + [index])
#     if ans == -1 or (t2 != -1 and ans > t2):
#         ans = t2
#     return ans

# n = int(input())
# s = [list(map(int, input().split())) for _ in range(n)]
# print(go(0, [], []))

## 3. 그냥 2개 선택하니 for 문 2번으로 진행하고,
# range의 시작과 끝을 연결하자...
# 어차피 2개 permutation이니깐 그냥 i,j j,i번째 더하는 식으로 하자.

# from itertools import combinations

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# result = 10**6
# number = [i for i in range(n)]

# for comb in combinations(number, n//2):
#     link = [i for i in range(n) if i not in comb]
#     link_score = 0
#     score = 0
#     for i in range(n//2-1):
#         for j in range(i+1, n//2):
#             score += graph[comb[i]][comb[j]] + graph[comb[j]][comb[i]]
#             link_score += graph[link[i]][link[j]] + graph[link[j]][link[i]]
#     ans = abs(score - link_score)
#     result = min(result, ans)
# print(result)

## 3. bitmask로 풀기. 그런데 더 느림...

import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip("\n"))
    board = [list(map(int, input().rstrip("\n").split(" "))) for _ in range(N)]
    mask = int("0"*N, base=2)
    score_diff = 1e8

    # 000111
    # 001011
    # 010011

    for i in range(1 << N): # 범위 설정을 어떻게 하지?
        team = format(i, 'b').rjust(N, '0')
        if team.count('1') == N/2:  #000111이라면.
            start_team = []
            link_team = []
            for idx, ch in enumerate(team):
                if ch == "0":
                    start_team.append(idx)
                else:
                    link_team.append(idx)
            start_score = 0
            link_score = 0
            for i in range(N):
                for j in range(i+1,N):
                    if i in start_team and j in start_team:
                        start_score+=board[i][j]+ board[j][i]
                    elif i in link_team and j in link_team:
                        link_score+=board[i][j]+ board[j][i]

            score_diff = min(score_diff, abs(start_score-link_score))

    print(score_diff)


if __name__ == "__main__":
    # main()
    a = 0b0000
    for i in range(5):
        print(a+i)

# 모든 부분집합 순회하는 것도 가능함.
origin = int('0b1101',2)
subset = origin

while True:
    subset = (subset - 1) & origin 
    # 이러면 하나씩 빼고, 결국 origin과 교집합이기에 모든 부분집합이 나옴.

    if subset == 0:
        break

    print(bin(subset))


## 4. 비트마스킹.
    # 출처: msjang4. 다이아 5
    """input
8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
"""
import sys

read = sys.stdin.readline

n = int(read())


adj = [list(map(int, read().split())) for _ in range(n)]

# 깊이는 11
# 상태전이는 4 
# 4^11 = 2^22 400만 정도?

from itertools import combinations

def solution():
    team_size = n//2
    team_count = 1<<n
    power = [-1] *(team_count)  # power를 아예 array에 저장시킴.
    answer = float('inf')
    for team in combinations(range(n), team_size): 
        status_bit = 0
        team_power = 0
        for i in range(team_size):
            status_bit |= (1<<team[i])
            for j in range(team_size):
                if i!=j:
                    team_power += adj[team[i]][team[j]] 
        
        
        power[status_bit] = team_power
        enemy_status_bit = team_count-1 - status_bit    # 1111111 - 100101 => # 011010
        if power[enemy_status_bit] != -1:
            answer = min(answer,abs(power[enemy_status_bit]-team_power))
    return answer

print(solution())