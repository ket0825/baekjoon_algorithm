"""문제
Given a sequence of integers, a1, a2, …, an, 
we define its sign matrix S such that, 
for 1 ≤ i ≤ j ≤ n,
Sij="+" if ai + … + aj > 0; 
Sij="−" if ai + … + aj < 0; 
and Sij="0" otherwise. 

For example, if (a1, a2, a3, a4)=( −1, 5, −4, 2), 
then its sign matrix S is a 4×4 matrix: 

 	1	2	3	4
1	-	+	0	+
2	 	+	+	+
3	 	 	-	-
4	 	 	 	+
We say that the sequence (−1, 5, −4, 2) generates the sign matrix. 
A sign matrix is valid if it can be generated by a sequence of integers. 

Given a sequence of integers, 
it is easy to compute its sign matrix. 

This problem is about the opposite direction: 
Given a valid sign matrix, find a sequence of integers 
that generates the sign matrix. 
Note that two or more different sequences of integers 
can generate the same sign matrix. 
For example, the sequence (−2, 5, −3, 1) generates the same sign matrix 
as the sequence (−1,5, −4,2). 

Write a program that,
given a valid sign matrix, 
can find a sequence of integers that generates the sign matrix. 
You may assume that every integer in a sequence 
is between −10 and 10, both inclusive. 

입력
The first line contains an integer n(1 ≤ n ≤ 10),
where n is the length of a sequence of integers. 
The second line contains a string of n(n+1)/2 characters 
such that the first n characters 
correspond to the first row of the sign matrix, 
the next n−1 characters to the second row, ..., 
and the last character to the n-th row. 

출력
Output exactly one line containing a sequence of n integers 
which generates the sign matrix. 
If more than one sequence generates the sign matrix, 
you may output any one of them. 
Every integer in the sequence must be between −10 and 10, both inclusive.

예제 입력 1 
4
-+0++++--+
예제 출력 1 
-2 5 -3 1
예제 입력 2 
2
+++
예제 출력 2 
3 4
예제 입력 3 
5
++0+-+-+--+-+--
예제 출력 3 
1 2 -3 4 -5
"""

# 중복이 가능한 -10부터 10까지의 정수임.

import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip('\n')) # n(1 ≤ n ≤ 10)
    signs = input().rstrip("\n")
    start = 0

    S = [[-1 for _ in range(N)] for _ in range(N)] # N * N

    for i in range(N):
        for j in range(i,N):
            S[i][j] = signs[start]
            start+=1

    # diagonal들은 각 파트의 부호를 나타냄.
    # elems_signs = [S[i][i] for i in range(N)]

    def dfs(guess:list, depth:int):
        if len(guess) == N:
            print(*guess)
            exit()
   
        # 가능 여부 체크로...
        possible_value_lst = list(range(-10, 11))

        for i in range(0, depth+1):            
            check_range = guess[i:depth+1]
            # check_range가 공백인게 의미가 있나? => 0이라는 의미가 있을 듯.
    
            if S[i][depth] == "0":
                possible_value_lst = [i for i in possible_value_lst if sum(check_range) + i == 0]
            elif S[i][depth] == "+":
                possible_value_lst = [i for i in possible_value_lst if sum(check_range) + i > 0]
            elif S[i][depth] == "-":
                possible_value_lst = [i for i in possible_value_lst if sum(check_range) + i < 0]
        
        # 불가능한 경우
        if not possible_value_lst:
            return

        # 절댓값 기준 0과 가까운 순으로 정렬시킴.
        # possible_value_lst.sort(key=lambda x: abs(x))

        for value in possible_value_lst:
            dfs(guess+[value], depth+1)

    dfs([], 0)


# if __name__ == "__main__":
#     main()


## 2. sum으로 한번에 계산하면서 또 for문을 쓰지않고, 
# 요소 하나하나마다 더하면서 동시에 조건을 만족하는지, 만족하지 않는지를 확인함.
# 그리고, 음수 양수를 저장할 때, 숫자로 해서 for i in range도 줄여버림...
# 숫자로 음수, 양수를 저장하여 0인 경우도 과감히 스킵시킴.
    
# def check(index):
#     s = 0
#     for i in range(index,-1,-1):
#         s += ans[i] 
#         if sign[i][index] == 0:
#             if s != 0:
#                 return False
#         elif sign[i][index] < 0:
#             if s >= 0:
#                 return False
#         elif sign[i][index] > 0:
#             if s <= 0:
#                 return False
#     return True
    
# def go(index):
#     if index == n:
#         return True
    
#     if sign[index][index] == 0: # 여기서 sign으로 저장해놓은 +1, -1, 0 형식이 빛남. 그냥 0으로 박아버림.
#         ans[index] = 0
#         return check(index) and go(index+1)
    
#     for i in range(1, 11):
#         ans[index] = i * sign[index][index] # 여기서 sign으로 저장해놓은 +1, -1, 0 형식이 빛남.
#         if check(index) and go(index+1):    # 그것일 경우, 지난 조건들이 만족하는지 체크함. 그리고, True면 go 다음 index를 진행.
#             return True
        
#     return False

# n = int(input())
# s = input()
# sign = [[0]*n for _ in range(n)]
# ans = [0]*n
# cnt = 0
# for i in range(n):
#     for j in range(i,n):
#         if s[cnt] == '0':
#             sign[i][j] = 0
#         elif s[cnt] == '+':
#             sign[i][j] = 1
#         else:
#             sign[i][j] = -1
#         cnt += 1

# go(0)

# print(' '.join(map(str,ans)))