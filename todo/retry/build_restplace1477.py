"""
휴게소 세우기
시간 제한	메모리 제한
2 초	128 MB
문제
다솜이는 유료 고속도로를 가지고 있다. 
다솜이는 현재 고속도로에 휴게소를 N개 가지고 있는데,
휴게소의 위치는 고속도로의 시작으로부터 얼만큼 떨어져 있는지로 주어진다. 
다솜이는 지금 휴게소를 M개 더 세우려고 한다.

다솜이는 이미 휴게소가 있는 곳에 휴게소를 또 세울 수 없고,
고속도로의 끝에도 휴게소를 세울 수 없다. 
휴게소는 정수 위치에만 세울 수 있다.

다솜이는 이 고속도로를 이용할 때, 
모든 휴게소를 방문한다. 

다솜이는 휴게소를 M개 더 지어서 휴게소가 없는 구간의 길이의 최댓값을 최소로 하려고 한다. 
(반드시 M개를 모두 지어야 한다.)

예를 들어, 고속도로의 길이가 1000이고, 
현재 휴게소가 {200, 701, 800}에 있고, 
휴게소를 1개 더 세우려고 한다고 해보자.

일단, 지금 이 고속도로를 타고 달릴 때, 
휴게소가 없는 구간의 최댓값은 200~701구간인 501이다. 
하지만, 새로운 휴게소를 451구간에 짓게 되면, 
최대가 251이 되어서 최소가 된다.

입력
첫째 줄에 현재 휴게소의 개수 N, 
더 지으려고 하는 휴게소의 개수 M, 
고속도로의 길이 L이 주어진다. 
둘째 줄에 현재 휴게소의 위치가 공백을 사이에 두고 주어진다. 
N = 0인 경우 둘째 줄은 빈 줄이다.

출력
첫째 줄에 M개의 휴게소를 짓고 난 후에 
휴게소가 없는 구간의 최댓값의 최솟값을 출력한다.

제한
0 ≤ N ≤ 50
1 ≤ M ≤ 100
100 ≤ L ≤ 1,000
1 ≤ 휴게소의 위치 ≤ L-1
N+M < L
모든 휴게소의 위치는 중복되지 않음
입력으로 주어지는 모든 수는 정수
예제 입력 1 
6 7 800
622 411 201 555 755 82
예제 출력 1 
70
예제 입력 2 
3 1 1000
200 701 800
예제 출력 2 
251
예제 입력 3 
3 1 1000
300 701 800
예제 출력 3 
300

2 4 400
299 399

75
"""

import sys
import heapq
input = sys.stdin.readline

def sol():
    N, M, L = map(int, input().strip().split())
    places = list(map(int, input().strip().split()))
    places = [0] + sorted(places) + [L]
    diff = []
    for i in range(len(places) - 1):
        diff.append((-(places[i+1] - places[i]), i)) # for max heap, counter
    
    heapq.heapify(diff)
    # print(diff)
            
    remain = M
    split_counter = [0]*(N+1) # 횟수 체크. 만약 heap에서 이미 1이면 새로운 heap 제작.    
    while remain != 0:
        max_val, idx = heapq.heappop(diff)
        split_counter[idx]+=1    
        iter = split_counter[idx]
        # print(max_val, idx)        
        # 값은 똑같지만 인덱스가 다른 것이 제거될 수도 있음. 이유: 나머지값... 이걸 방지.
        cnt = iter - 1
        refill = []
        while cnt != 0:
            reset_val, reset_idx = heapq.heappop(diff)
            if idx != reset_idx: # 다른 인덱스 제거 시.                
                refill.append((reset_val, reset_idx))
            else: # 원하는 인덱스가 제거됨.                
                cnt-=1 
        # 다시 잘 채워넣어주기
        # print(refill)
        while refill:
            ref = refill.pop()
            heapq.heappush(diff, ref)
        
        # 새롭게 나눠주기 위함.
        original_dist = places[idx+1] - places[idx]
        splitted_dist = original_dist // (iter+1)
        remainer = original_dist % (iter+1) # 나머지값
        for _ in range(iter+1):
            if remainer: # 나머지값 존재하면 몫에 +1해서 넣어줌.
                heapq.heappush(diff, (-(splitted_dist + 1), idx))
                remainer-=1
            else: # 나머지값 없으면 몫을 넣어줌.
                heapq.heappush(diff, (-splitted_dist, idx))        
        remain-=1
        # print(diff)
    # max heap 값 출력
    print(-diff[0][0])        
            

if __name__ == '__main__':
    sol()

# 이진탐색으로 더 깔끔하게 푸는 법. 출처: corntea
"""N, M, L = map(int, input().split())
pos = sorted(list(map(int, input().split()))) if N != 0 else []

pos.insert(0, 0)
pos.append(L)
diff = []
for i in range(len(pos) - 1):
    diff.append(pos[i + 1] - pos[i])
diff.sort()

l, r = 1, diff[-1]


while l <= r:

    m = (l + r) // 2

    count = 0
    for d in diff:
        count += (d - 1) // m

    if count <= M:
        r = m - 1
    else:
        l = m + 1

print(l)
"""