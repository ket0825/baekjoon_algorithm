"""
수들의 합 4
시간 제한	메모리 제한
2 초	128 MB
문제
A[1], A[2], ..., A[N]의 N개의 정수가 저장되어 있는 배열이 있다. 이 배열 A의 부분합이란 1 ≤ i ≤ j ≤ N인 정수 i와 j에 대해 A[i]부터 A[j]까지의 합을 말한다.

N과 A[1], A[2], ..., A[N]이 주어졌을 때, 이러한 N×(N+1)/2개의 부분합 중 합이 K인 것이 몇 개나 있는지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N과 K가 주어진다. (1 ≤ N ≤ 200,000, |K| ≤ 2,000,000,000) N과 K 사이에는 빈칸이 하나 있다. 둘째 줄에는 배열 A를 이루는 N개의 정수가 빈 칸을 사이에 두고 A[1], A[2], ..., A[N]의 순서로 주어진다. 주어지는 정수의 절댓값은 10,000을 넘지 않는다.

출력
첫째 줄에 합이 K인 부분합의 개수를 출력한다.

예제 입력 1 
4 0
2 -2 2 -2
예제 출력 1 
4
예제 입력 2 
6 5
1 2 3 4 5 0
예제 출력 2 
3

---
5 -1
0 -1 3 -2 -1

4
"""

import sys
input = sys.stdin.readline

def sol(A, K, N):
    prefix_map = {0: 1}
    ps = 0
    answer = 0
    for i in range(N):
        ps+=A[i]
        # 만약 지금까지의 누적합 Hashmap에서 K만큼 뺀 값이 존재한다? -> 그렇다면 그 사이 부분집합 안에 K가 존재!
        # print(f"prefix_map: {prefix_map}")
        if prefix_map.get(ps-K):
            answer+=prefix_map[ps-K]
            # print(f"A[i]: {A[i]}, ps: {ps}")
        
        # 그리고 prefix_map 갱신
        if prefix_map.get(ps):
            prefix_map[ps]+=1
        else:
            prefix_map[ps] = 1
                
    return answer


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    print(sol(A, K, N))
