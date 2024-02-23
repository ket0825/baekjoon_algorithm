# """
# 문제
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

# 정수 N이 주어졌을 때,
# 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 입력
# 첫째 줄에 1보다 크거나 같고, 
# 1e6보다 작거나 같은 정수 N이 주어진다.

# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

# 예제 입력 1 
# 2
# 예제 출력 1 
# 1
# 예제 입력 2 
# 10
# 예제 출력 2 
# 3

# 힌트
# 10의 경우에 10 → 9 → 3 → 1 로 3번 만에 만들 수 있다.

# 출처
# 문제를 번역한 사람: baekjoon
# """

# import sys
# input = sys.stdin.readline
# ans = 1e6

# # 일단 생각나는 건 tree. => BFS
# def main():     
#     N = int(input()) # 1 <= N <= 1e6
       
#     def dfs(num:int, count:int):        
#         global ans
#         if ans <= count: # early pruning.
#             return
        
#         if num == 1:         
#             ans = count
#             return
#         elif num < 1:
#             return
        
#         if num % 3 == 0:
#             dfs(num/3, count+1)
#         if num % 2 == 0:
#             dfs(num/2, count+1)
#         # -1 연산은 모든 경우에 가능.
#         dfs(num-1, count+1)

#     dfs(N,0)
#     print(int(ans))
    

# if __name__ == "__main__":
#     main()


# ## 2. BFS. 그리고 이미 지나간 값까지 제외시킴(이건 BFS라 가능한 듯. 
# # BFS이기에 다음에 나온 값은 무조건 자신보다 횟수가 더 큰 값임)
# # 출처: wjdghkdduq
# from collections import deque
# import sys

# def BFS(N):
#     visited=set()
#     dq=deque([N])
#     temp_list=deque()
#     count=0
#     while dq:
#         v=dq.popleft()
#         if v%3==0 and v%3 not in visited:
#             visited.add(v/3)
#             temp_list.append(v/3)
#         if v%2==0 and v%2 not in visited:
#             visited.add(v/2)
#             temp_list.append(v/2)
#         if v-1 not in visited and v-1>0:
#             visited.add(v-1)
#             temp_list.append(v-1)
#         if 1 in temp_list: return count+1
#         if not dq:
#             count+=1
#             dq=temp_list
#             temp_list=deque()


# N=int(sys.stdin.readline())
# count=BFS(N)
# if not count : print("0")
# else : print(count)


## 3. 리스트를 아예 만들고, 역연산으로 n까지의 모든 최소를
# count하는 횟수를 계산함.
# dp[i]를 일단 전 것 +1로 계산하고 (-1 연산), 
# 혹시 2나 3으로 나눠떨어지는 것이 있으면 /2, /3 전에 것과 현 dp[i]와 비교하여
# min으로 더 작은 값을 구해준다.

n = int(input())
dp = [0] * (n+1)    # n+1개의 list를 만듦.
for i in range(2,n+1): 
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[n])