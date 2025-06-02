"""
교환
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	21071	4998	3732	23.828%
문제
0으로 시작하지 않는 정수 N이 주어진다. 이때, M을 정수 N의 자릿수라고 했을 때, 다음과 같은 연산을 K번 수행한다.

1 ≤ i < j ≤ M인 i와 j를 고른다. 그 다음, i번 위치의 숫자와 j번 위치의 숫자를 바꾼다. 이때, 바꾼 수가 0으로 시작하면 안 된다.

위의 연산을 K번 했을 때, 나올 수 있는 수의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N과 K가 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, K는 10보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제에 주어진 연산을 K번 했을 때, 만들 수 있는 가장 큰 수를 출력한다. 만약 연산을 K번 할 수 없으면 -1을 출력한다.

예제 입력 1 
16375 1
예제 출력 1 
76315
예제 입력 2 
132 3
예제 출력 2 
312
예제 입력 3 
432 1
예제 출력 3 
423
예제 입력 4 
90 4
예제 출력 4 
-1
예제 입력 5 
5 2
예제 출력 5 
-1
예제 입력 6 
436659 2
예제 출력 6 
966354

900 2
900

421888 3
888421

821488 < 821884 이게 더 큼... 그래서 오른쪽으로 안됨.
881428
888421


827912 9

987221

"""

import sys
from itertools import combinations
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

def solution(num_str, K):
    N = len(num_str)
    num_str = [num_str[i] for i in range(N)]
    if N == 1:
        print(-1)
        return
    
    if N == 2 and num_str[1] == "0": # 0이 존재하고 2자리
        print(-1)
        return
    
    visited = defaultdict(set)    
    q = deque([(num_str, 0)])
    # visited[int(''.join(num_str))].add(0)
    
    while q:
        num_item, count = q.pop()
        # print(num_item, count)
        if count == K+1:
            break
        
        for combi in combinations(range(N), 2):            
            a, b = combi
            if a > b: # a가 더 작게
                a, b = b, a
                
            if a == 0 and num_item[b] == "0":
                continue
                        
            # swap            
            num_item[b], num_item[a] = num_item[a], num_item[b]
            num = int(''.join(num_item))
            
            # print(f"num: {num} count: {count}")
            if visited[num]:                
                if count+1 not in visited[num]: # 없으면
                    q_flag = True           
                    for i in visited[num]:
                        if (count+1 - i) % 2 == 0: # 뺀 게 짝수라면
                            visited[num].add(count+1) # 방문 기록하고 다시 넣지 않음.
                            q_flag = False
                            break
                    
                    visited[num].add(count+1)
                    if q_flag:   
                        # print(f"넣기: {num_item}, count: {count+1}")                 
                        q.appendleft((num_item.copy(), count+1))
                        
            else:
                visited[num].add(count+1)
                # print(f"넣기: {num_item}, count: {count+1}")                 
                q.appendleft((num_item.copy(), count+1))
            
            # 원상복구
            num_item[b], num_item[a] = num_item[a], num_item[b]
        
    max_val = -1    
    for num, s in visited.items():    
        for s_item in s:
            # print(f"s_item: {s_item}, i: {num}")
            
            if (K - s_item) % 2 == 0: # 뺀 게 짝수라면
                # print(f"{i} 가능")
                max_val = max(num, max_val)
                break    
                          
    print(max_val)
    
    

            
if __name__ == "__main__":
    num_str, K = input().strip().split()    
    solution(num_str, int(K))
    
    
"""
간단한 풀이. 출처: hope123
def dfs(num,cnt):
    global max_val
    num_str=''.join(num)
    #이전에도 한 swap이라면
    if (num_str,cnt) in visited:
        return
    visited.add((num_str,cnt))
    #교환 끝
    if cnt==K:
        max_val=max(max_val,int(num_str))
        return
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            num[i],num[j]=num[j],num[i]
            if num[0]!='0': #교환 결과가 0으로 시작하면 안 됌
                dfs(num,cnt+1)
            num[i],num[j]=num[j],num[i] #백트레킹
N,K=input().split()
K=int(K)
num_list=list(N)
max_val=-1
visited=set() #중복 방지
dfs(num_list,0)
print(max_val)
"""