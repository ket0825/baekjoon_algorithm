"""
문제
두 종류의 부등호 기호 ‘<’와 ‘>’가 k개 나열된 순서열 A가 있다. 
우리는 이 부등호 기호 앞뒤에 서로 다른 한 자릿수 숫자를 넣어서 
모든 부등호 관계를 만족시키려고 한다. 
예를 들어, 제시된 부등호 순서열 A가 다음과 같다고 하자. 
A ⇒ < < < > < < > < >

부등호 기호 앞뒤에 넣을 수 있는 숫자는 0부터 9까지의 정수이며 
선택된 숫자는 모두 달라야 한다. 

아래는 부등호 순서열 A를 만족시키는 한 예이다. 

3 < 4 < 5 < 6 > 1 < 2 < 8 > 7 < 9 > 0

이 상황에서 부등호 기호를 제거한 뒤, 
숫자를 모두 붙이면 하나의 수를 만들 수 있는데 
이 수를 주어진 부등호 관계를 만족시키는 정수라고 한다. 
그런데 주어진 부등호 관계를 만족하는 정수는 하나 이상 존재한다. 
예를 들어 3456128790 뿐만 아니라 5689023174도 
아래와 같이 부등호 관계 A를 만족시킨다. 

5 < 6 < 8 < 9 > 0 < 2 < 3 > 1 < 7 > 4

여러분은 제시된 k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서
최댓값과 최솟값을 찾아야 한다. 

앞서 설명한 대로 각 부등호의 앞뒤에 들어가는 숫자는 
{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }중에서 선택해야 하며 
선택된 숫자는 모두 달라야 한다. 

입력
첫 줄에 부등호 문자의 개수를 나타내는 정수 k가 주어진다.
그 다음 줄에는 k개의 부등호 기호가 하나의 공백을 두고 
한 줄에 모두 제시된다. 
k의 범위는 2 ≤ k ≤ 9 이다. 

출력
여러분은 제시된 부등호 관계를 만족하는 k+1 자리의 최대,
최소 정수를 첫째 줄과 둘째 줄에 각각 출력해야 한다. 

단 아래 예(1)과 같이 첫 자리가 0인 경우도 정수에 포함되어야 한다. 

모든 입력에 답은 항상 존재하며 출력 정수는 하나의 문자열이 되도록 해야 한다. 

예제 입력 1 
2
< >
예제 출력 1 
897
021
예제 입력 2 
9
> < < < > > > < <
예제 출력 2 
9567843012
1023765489

내 예시:
=================
in:
9
< < < < < < < < <
out:
123456789
123456789
=================
in:
9
> > > > > > > > > 
out:
9876543210
9876543210
=================
in:
9
> > > > > > > > > 
out:
9876543210
9876543210

"""

# 2 ≤ k ≤ 9. 부등호 가짓수는 2^k개.
# 그 사이에 숫자가 들어가는 경우의 수는 10P(k+1), 최대 10! = 3628800

## 1. 내 풀이: 그냥 for문으로 여러 번 실행시킴.
# import sys
# input = sys.stdin.readline
# max_value = 0
# min_value = 1e11

# def main():
#     K = int(input().rstrip("\n"))
#     inequality_signs = [True if sign == "<" else False for sign in input().rstrip("\n").split(" ")]
#     # 작으면 True, 크면 False.

#     def brute_force(used_list:list[int], count:int):
#         if count == K+1:
#             value = int(''.join(map(str,used_list)))
#             global max_value, min_value
#             max_value = max(max_value, value)
#             min_value = min(min_value, value)
#             return
    
#         if count == 0: # 다 가능.
#             unused_list = [i for i in range(10)]
#         elif inequality_signs[count-1]: #True면 "<" 부호.
#             unused_list = [i for i in range(10) if i > used_list[-1] and i not in used_list]    
#         else: # ">" 부호.
#             unused_list = [i for i in range(10) if i < used_list[-1] and i not in used_list]    

#         # 조건이 안되는 경우가 있음.
#         if not unused_list: # empty면
#             return

#         for i in unused_list:
#             brute_force(used_list+[i], count+1)

#     brute_force([],0)
    
#     print(max_value)
#     if len(str(min_value)) == K: # 맨 앞이 0이면
#         print("0"+str(min_value))
#     else:
#         print(min_value)
    

# if __name__ == "__main__":
#     main()


## 2. str 처리하고 쭉 더하기. 그리고, 낮은 수부터 만족하는 것을 찾아나가면 당연히 처음이 min임!
import sys

k = int(sys.stdin.readline())
li = list(sys.stdin.readline().split())

min_res = ''
max_res = ''

visited = [False] * 10 # memoization.


def check(mark, a, b):
    if mark == "<":
        return a < b
    else:
        return a > b

def dfs(depth, s):  
    global min_res, max_res

    if depth == k+1:
        if len(min_res) == 0: # 0부터 차례로 가면 당연히 맨 처음이 최소구나!
            min_res = s
        else:
            max_res = s
        return
    
    for i in range(10):
        if not visited[i]:  # visited[i]가 false면
            if  depth == 0 or check(li[depth-1], s[-1], str(i)):
                visited[i] = True
                dfs(depth+1, s+str(i))
                visited[i] = False

    
dfs(0, '')
print(max_res)
print(min_res)