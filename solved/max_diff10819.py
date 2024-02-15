"""
문제
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

입력
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

출력
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

예제 입력 1 
6
20 1 15 8 4 10
예제 출력 1 
62
"""

import sys
input = sys.stdin.readline
diff = 0

def main():
    N = int(input().rstrip("\n"))   # # 3 <= N <= 8
    sequence = sorted(map(int, input().rstrip("\n").split(" ")))

    permu = []
    visited = [0]*N

    def permutation(local_diff):
        if len(permu) == N:
            global diff
            diff = max(local_diff, diff)
            print(" ".join(map(str, permu)))
            return
        
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                permu.append(sequence[i])
                if sum(visited) > 1:
                    permutation(local_diff + abs(permu[-2] - sequence[i]))
                else:
                    permutation(0)
                permu.pop()
                visited[i] = 0

    permutation(0)        

    print(diff)


if __name__ == "__main__":
    main()


## 2. 다른 방식
# from collections import deque
# import sys
# input=sys.stdin.readline
# n=int(input())
# m=list(map(int,input().split()))
# m.sort()
# q=deque(m[1:])
# res=deque([m[0]])
# ret=0
# while q:
#     res1=abs(q[0]-res[0])
#     res2=abs(q[0]-res[-1])
#     res3=abs(q[-1]-res[0])
#     res4=abs(q[-1]-res[-1])
#     cur=max(res1,res2,res3,res4)
#     ret+=cur
#     if cur==res1:
#         res.appendleft(q.popleft())
#     elif cur==res2:
#         res.append(q.popleft())
#     elif cur==res3:
#         res.appendleft(q.pop())
#     else:
#         res.append(q.pop())
# print(ret)

## 3. 규칙 찾음.
# n = int(input())
# num_list = list(map(int, input().split()))


# num_list.sort()
# ans = 0
# # 기본적으로 큰 수와 작은 수를 번갈아야 차이가 최대
# if n == 3:
#   ans = max(num_list[2] + num_list[1] - 2 * num_list[0],
#             2 * num_list[2] - num_list[1] - num_list[0])
# elif n % 2 == 0:
#   # 수의 개수가 짝수: 가운데 두 수를 양 끝값으로 지정
#   mid = n // 2
#   ans += 2 * sum(num_list[mid+1:]) # 가운데보다 큰 수들
#   ans -= 2 * sum(num_list[:mid-1]) # 가운데보다 작은 수들
#   ans += num_list[mid] # 큰 가운데값
#   ans -= num_list[mid-1] # 작은 가운데값
# else:
#   # 수의 개수가 홀수: 차이가 더 작은 가운데 두 수를 양 끝값으로 지정
#   mid = n // 2
#   if num_list[mid+1] - num_list[mid] > num_list[mid] - num_list[mid-1]:
#     # mid와 mid-1을 양 끝값으로 지정 (양 끝 수보다 큰 수들이 1개 더 많음)
#     ans += 2 * sum(num_list[:mid-1]) # 가운데보다 큰 수들
#     ans -= 2 * sum(num_list[:mid-1]) # 가운데보다 작은 수들
#     ans -= num_list[mid-1] + num_list[mid] # 가운데 수들
#   else:
#     # mid와 mid+1을 양 끝값으로 지정 (양 끝 수보다 작은 수들이 1개 더 많음)
#     ans += 2 * sum(num_list[mid+2:]) # 가운데보다 큰 수들
#     ans -= 2 * sum(num_list[:mid]) # 가운데보다 작은 수들
#     ans += num_list[mid] + num_list[mid+1] # 가운데 수들
# print(ans)
