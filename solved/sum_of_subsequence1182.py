"""
부분수열의 합

문제
N개의 정수로 이루어진 수열이 있을 때, 
크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 
S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. 
(1 ≤ N ≤ 20, |S| ≤ 1,000,000) 
둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 
주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

예제 입력 1 
5 0
-7 -3 -2 5 8
예제 출력 1 
1
출처
문제를 만든 사람: author5
문제의 오타를 찾은 사람: eric00513, jh05013
데이터를 추가한 사람: rdd6584
잘못된 데이터를 찾은 사람: tncks0121
"""
## 1. 일반적인 풀이.
# import sys
# import itertools
# input = sys.stdin.readline

# def main():
#     N, S = map(int, input().rstrip("\n").split(" ")) # (1 ≤ N ≤ 20, |S| ≤ 1,000,000)
#     sequence = list(map(int, input().rstrip("\n").split(" ")))
#     """
#     5 0
#     -7 -3 -2 5 8
#     """
#     ## 1. brute force. 5C1 + 5C2 + 5C3 + ... + 5C5 = 2^5 - 1. 일종의 부분집합의 합.
#     # 최대 2^20 => 524288 안전. 가능.
#     subseq_count = 0
#     for i in range(1, N+1):
#         for subseq in itertools.combinations(sequence, i):
#             if sum(subseq) == S:
#                 subseq_count +=1

#     print(subseq_count)


# if __name__ == "__main__":
#     main()

# 메모리: 31120, 시간: 252


## 2. 비트 연산을 이용한 부분집합 표현.
import sys
input = sys.stdin.readline

def main():
    N, S = map(int, input().rstrip("\n").split(" ")) # (1 ≤ N ≤ 20, |S| ≤ 1,000,000)
    sequence = list(map(int, input().rstrip("\n").split(" ")))

    ## 2. N개의 bit를 가진 것을 작성. 각 비트를 수열 elem에 대응.
    # 10010 => 첫번째, 4번째 대응.
    # 00101 => 3번째, 5번째 대응.
    # 이 또한 최대 2^20 => 524288. 안전. 가능.
    subseq_count = 0

    for i in range (1, 1 << N):
        subseq_sum = 0
        for idx, j in enumerate(format(i, 'b').rjust(N, "0")):  # 이걸로 우측에 0을 삽입시켜줌.
            if j == '1':
                subseq_sum+= sequence[idx]
        
        if subseq_sum == S:            
            subseq_count +=1

    print(subseq_count)


if __name__ == "__main__":
    main()
    # print("a".rjust(5, "*"))


## 3. 0과 1로 표현 가능하니 binary tree 구조로도 생각 가능.
'''
부분수열: 연속하지 않아도 됨...
'''
import sys
input = sys.stdin.readline

n, s = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
def recur(cur,sum_):
  global cnt
  if cur == n:
    return
  sum_ += arr[cur]
  if sum_ == s:
    cnt += 1
  # 해당 index의 값을 더해준 거 => 왼쪽
  recur(cur+1, sum_)
  # 해당 index의 값을 스킵한 거 => 오른쪽.
  recur(cur+1, sum_ - arr[cur])

recur(0,0)
print(cnt)
# 출처: yongjae116

## 4. 트리 끝까지 내려가서 확인하는 것임. 맞으면 1, 아니면 0임.
n, s = map(int, input().split())
l = [int(x) for x in input().split()]
def f(i, x):
    if i == n:
        return +(x==0)
    return f(i+1, x) + f(i+1, x-l[i])
print(f(0,s) - (s==0))
# 출처: eunsoo0607


## 5. 하나하나 더해줌.
n, s = map(int, input().split()) # 리스트 정수의 개수, 부분 수열의 합
arr = list(map(int, input().split())) # 리스트

cnt = 0 # 조건에 맞는 경우 카운트
for i in range(1 << n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])
    if sum(subset) == s:
        cnt += 1
if s == 0: # s가 0일경우 공집합을 포함하기때문에, 이 경우를 제외한다.
    cnt -= 1
print(cnt)

# 출처: https://sunshower99.tistory.com/10