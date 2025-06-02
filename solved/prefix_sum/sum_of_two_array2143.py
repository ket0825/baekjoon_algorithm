"""
두 배열의 합
 
시간 제한	메모리 제한
2 초	64 MB
문제
한 배열 A[1], A[2], …, A[n]에 대해서, 부 배열은 A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다. 이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다. 각 원소가 정수인 두 배열 A[1], …, A[n]과 B[1], …, B[m]이 주어졌을 때, A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.

예를 들어 A = {1, 3, 1, 2}, B = {1, 3, 2}, T=5인 경우, 부 배열 쌍의 개수는 다음의 7가지 경우가 있다.

T(=5) = A[1] + B[1] + B[2]
      = A[1] + A[2] + B[1]
      = A[2] + B[3]
      = A[2] + A[3] + B[1]
      = A[3] + B[1] + B[2]
      = A[3] + A[4] + B[3]
      = A[4] + B[2] 
입력
첫째 줄에 T(-1,000,000,000 ≤ T ≤ 1,000,000,000)가 주어진다. 다음 줄에는 n(1 ≤ n ≤ 1,000)이 주어지고, 그 다음 줄에 n개의 정수로 A[1], …, A[n]이 주어진다. 다음 줄에는 m(1 ≤ m ≤ 1,000)이 주어지고, 그 다음 줄에 m개의 정수로 B[1], …, B[m]이 주어진다. 각각의 배열 원소는 절댓값이 1,000,000을 넘지 않는 정수이다.

출력
첫째 줄에 답을 출력한다. 가능한 경우가 한 가지도 없을 경우에는 0을 출력한다.

예제 입력 1 
5
4
1 3 1 2
3
1 3 2
예제 출력 1 
7

"""

# 음수 포함임...
# d = {i: i for i in range(500000)} # 최대 20MB
# print(d.__sizeof__() // 1024 // 1024) # 20MB

import sys
input = sys.stdin.readline

def sol(T, N, A, M, B):
    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(1, M):
        B[i] += B[i-1]
        
    def make_subsum(arr, length, subsum):
        for i in range(length):
            if subsum.get(arr[i]):
                subsum[arr[i]]+=1
            else:
                subsum[arr[i]] = 1
            
        for i in range(length-1):
            for j in range(i+1, length):
                val = arr[j] - arr[i]                
                if subsum.get(val):
                    subsum[val]+=1
                else:
                    subsum[val] = 1                
    
    a_subsum = {}
    make_subsum(A, N, a_subsum)
    b_subsum = {}
    make_subsum(B, M, b_subsum)
    
    def calculate_sum(subsum1, subsum2):
        answer = 0
        for k, v in subsum1.items():
            check = T - k
            if subsum2.get(check):
                answer += v*subsum2[check]                            
        return answer
                    
    if N > M:
        print(calculate_sum(b_subsum, a_subsum))
    else:
        print(calculate_sum(a_subsum, b_subsum))

if __name__ == '__main__':    
    T = int(input().strip())
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    M = int(input().strip())
    B = list(map(int, input().strip().split()))    
    sol(T, N, A, M, B)
    """
    10
    3
    1 1 1
    4
    1 1 1 1
    
    0
    ---
    
    10
    3
    10 7 9
    4
    1 2 3 1
    
    4
    
    0
    4
    1 -3 1 2
    3
    1 3 -2
    
    
    """  
    