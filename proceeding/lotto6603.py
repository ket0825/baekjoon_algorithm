"""
독일 로또는 {1, 2, ..., 49}에서 수 6개를 고른다.
로또 번호를 선택하는데 사용되는 가장 유명한 전략은 
49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 
그 수만 가지고 번호를 선택하는 것이다.

예를 들어, k=8, S={1,2,3,5,8,13,21,34}인 경우 
이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지이다. 8C2
([1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], 
[1,2,3,5,13,21], ..., [3,5,8,13,21,34])

집합 S와 k가 주어졌을 때, 
수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 
각 테스트 케이스는 한 줄로 이루어져 있다. 
첫 번째 수는 k (6 < k < 13)이고, 
다음 k개 수는 집합 S에 포함되는 수이다. 

S의 원소는 오름차순으로 주어진다.

입력의 마지막 줄에는 0이 하나 주어진다. 

출력
각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 
이때, 사전 순으로 출력한다.

각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.

예제 입력 1 
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0

예제 출력 1 
1 2 3 4 5 6
1 2 3 4 5 7
1 2 3 4 6 7
1 2 3 5 6 7
1 2 4 5 6 7
1 3 4 5 6 7
2 3 4 5 6 7

1 2 3 5 8 13
1 2 3 5 8 21
1 2 3 5 8 34
1 2 3 5 13 21
1 2 3 5 13 34
1 2 3 5 21 34
1 2 3 8 13 21
1 2 3 8 13 34
1 2 3 8 21 34
1 2 3 13 21 34
1 2 5 8 13 21
1 2 5 8 13 34
1 2 5 8 21 34
1 2 5 13 21 34
1 2 8 13 21 34
1 3 5 8 13 21
1 3 5 8 13 34
1 3 5 8 21 34
1 3 5 13 21 34
1 3 8 13 21 34
1 5 8 13 21 34
2 3 5 8 13 21
2 3 5 8 13 34
2 3 5 8 21 34
2 3 5 13 21 34
2 3 8 13 21 34
2 5 8 13 21 34
3 5 8 13 21 34
출처
Contest > University of Ulm Local Contest > University of Ulm Local Contest 1996 F번

문제의 오타를 찾은 사람: apjw6112, jh05013
문제를 번역한 사람: baekjoon
"""

# 계속 입력받음. 0이 나올 때 까지.
# 그리고 조합 문제임.

# k의 집합 길이, 집합 자체는 S.
# 그 중 6개 뽑아야 함.

# import sys
# input = sys.stdin.readline


# def main():
#     case_lists = []
#     while True:
#         case = input().rstrip("\n").split(" ")
#         if case == ['0']:
#             break
#         else:
#             case_lists.append(list(map(int, case)))

#     def dfs(ans:list, depth:int, start:int, case_length:int):
#         if depth == 6:
#             print(*ans)
#             return
        
#         for i in range(start, case_length): # 0, 7
#             if not visited[i]:
#                 visited[i] = True
#                 dfs(ans + [set[i]], depth=depth+1, start=start+1, case_length=case_length)
#                 visited[i] = False
#             start+=1    # 덜 직관적임. 방법 필요.

#     for case in case_lists:
#         visited = [False]*case[0]
#         set = case[1:]
#         dfs([], 0, 0, case[0])
#         if case_lists[-1] != case:
#             print("")    


# if __name__ == "__main__":
#     main()


## 2. 직관적. 그리고 계속 입력과 출력을 번갈아 받게 해도 된다.
def combination(index,level):
	if level==R:
		print(*choose)		
		return

	for i in range(index,k+1):
		choose.append(n[i])
		combination(i+1,level+1)
		choose.pop()

n=[]
while(True):
	n=list(map(int,input().split()))
	choose=[]
	k=n[0]
	R=6
	if(n[0]==0):
		break
	combination(1,0)
	print()
