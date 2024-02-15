"""
문제
상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.
오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 
남은 N일 동안 최대한 많은 상담을 하려고 한다.

백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고,
비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.

각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와
상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

N = 7인 경우에 다음과 같은 상담 일정표를 보자.

 	1일	2일	3일	4일	5일	6일	7일
Ti	3	5	1	1	2	4	2
Pi	10	20	10	20	15	40	200
1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 
5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.

상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에,
모든 상담을 할 수는 없다. 예를 들어서 1일에 상담을 하게 되면, 
2일, 3일에 있는 상담은 할 수 없게 된다. 2일에 있는 상담을 하게 되면,
3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.

또한, N+1일째에는 회사에 없기 때문에, 
6, 7일에 있는 상담을 할 수 없다.

퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 
이때의 이익은 10+20+15=45이다.

상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며,
1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.
N (1 ≤ N ≤ 15)

예제 입력 1 
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
예제 출력 1 
45

예제 입력 2 
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
예제 출력 2 
55
예제 입력 3 
10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6
예제 출력 3 
20
예제 입력 4 
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
예제 출력 4 
90

내 예제:
in:
4
5 10
5 10
5 10
5 10
out:
0
in:
5 
5 50
5 50
3 1000
1 10
1 10
out:
1000

"""

# import sys
# input = sys.stdin.readline

# def main():
#     N = int(input().rstrip("\n"))
#     reward_board = {}
#     for day in range(1, N+1):
#         time_reward = input().rstrip("\n").split(" ")
#         reward_board[day] = {"time": int(time_reward[0]), "reward": int(time_reward[1])}

#     reward_solution_set = set()

#     # 쉬고 더 좋은 날에 할 수도 있는 거임. (무조건 1일차부터 할 필요는 없음.)
#     def backtracking(current_day:int, total_reward:int):        
#         if current_day + reward_board[current_day].get("time") > N+1:
#             return
        
#         reward_solution_set.add(total_reward)
#         # print(current_day)

#         # 가능한 날들 집합 만들기.
#         for next_day in range(current_day + reward_board[current_day].get("time"), N+1):
#             # print(next_day)
#             backtracking(next_day, total_reward + reward_board[next_day].get("reward"))

#     reward_board[0] = {'time': 1, 'reward': 0} # 인위적으로 처음을 위해서 만들어둠.
#     backtracking(0, reward_board[0].get('reward'))

#     print(max(reward_solution_set))


# if __name__ == "__main__":
#     main()
    
## 2. 맨 뒤에서부터 가면서 가능하다면 dp에 해당하는 보수를 넣음.
# 가능하지 않으면 그것에서 최대값이라고 하고, 그걸 보수라고 함.
# 가능하다면 뒤의 날부터 받을 수 있는 보수값을 그 전의 날로부터 얻어 더함.
n=int(input())
t=[0]*(20)
p=[0]*(20)
dp=[0]*(20)
for i in range(n):
    a,b=map(int,input().split())
    t[i+1]=a
    p[i+1]=b
max_value=0
for i in range(n,0,-1):
    if i+t[i]<=n+1:
        dp[i]=max(dp[i+t[i]]+p[i],max_value) # 여기서 최댓값을 계속 dp에 저장함.
        max_value=dp[i]
    else:
        dp[i]=max_value # 만약 dp가 불가능한 날짜라면 그전까지가 max value임.

# print(dp)
print(dp[1])