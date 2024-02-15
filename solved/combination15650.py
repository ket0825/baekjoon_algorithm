"""
조합 구현.
"""
# import sys
# input = sys.stdin.readline

# def main():
#     N, M = map(int, input().rstrip("\n").split(" "))
#     comb_set = set(range(1, N+1))    

#     def comb(subset:list, comb_set: set):
        
#         if len(subset) == M:
#             print(' '.join(map(str, subset)))
#             return
        
#         comb_candidate = comb_set.copy()

#         for i in comb_set:
#             if i not in subset:
#                 subset.append(i)
#                 comb_candidate_copy = comb_candidate.copy()
#                 comb_candidate_copy.remove(i)
#                 comb(subset, comb_candidate_copy)
#                 subset.pop()

#             comb_candidate.remove(i)

#     comb([], comb_set)
    

# if __name__ == "__main__":
#     main()

## 2
# n,m=input().split()
# n=int(n);   m=int(m);   # 최대 자연수와 수열의 길이를 입력받음
# a=[0]*m
# def reselect(x,y): # 기준되는 숫자 이상을 뽑는 행위를 반복하니 재귀함수를 정의
#     a[m-y]=x
#     if(y==1):   # 재귀를 모두 성공적으로  마쳤을때 base case
#         print(*a)    # 수열을 출력,초기화
#     elif(x!=n):    # 더 재귀를 해야하는데, 그이상의 숫자가 없지 않을때(더 재귀가 가능할때)
#         for i in range(x+1,n+1):
#             reselect(i,y-1) # 재귀, 즉 선택을 한번 함을 -1로 표시하고 다시 뽑기

# for i in range(1,n+1):
#     reselect(i,m)   # m번 재귀(뽑기) 하는 수열을 출력. 시작 값은 range(1,n+1)
    
## 3 // len, s 등을 파라메터로 추가해서 구현함.
# def dfs(res, visit, len, s):
#     global N, M
#     # print(res, visit, len)
#     if len==M:
#         print(" ".join(res))
#     else:
#         for i in range(s, N):
#             nr=res[:]
#             nv=visit[:]
#             if not visit[i]:
#                 nr.append(str(i+1))
#                 nv[i]=1
#                 dfs(nr, nv, len+1, i+1)

# N, M = map(int, input().split())
# visit=[0]*N
# dfs([], visit, 0, 0)