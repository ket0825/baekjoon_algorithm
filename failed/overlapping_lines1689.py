"""
겹치는 선분
시간 제한	메모리 제한	
2 초	256 MB
문제
1차원 좌표계 위에 선분 N개가 있다. 
선분이 최대로 겹쳐있는 부분의 겹친 선분의 개수를 구해보자. 
선분의 끝 점에서 겹치는 것은 겹치는 것으로 세지 않는다.

입력
첫째 줄에는 선분의 개수(1 ≤ N ≤ 1,000,000)가 입력으로 들어온다. 
그 다음 N개의 줄에 선분의 시작 좌표 s와 끝나는 좌표 e (s < e)가 입력으로 들어온다. 
선분의 좌표는 절댓값이 10억보다 작거나 같은 정수이다.

출력
첫째 줄에는 최대로 많이 겹치는 선분들의 개수를 출력한다.

예제 입력 1 
11
1 2
3 6
7 8
10 11
13 16
0 5
5 6
2 5
6 10
9 14
12 15
예제 출력 1 
3
"""


import sys
input = sys.stdin.readline

# 모르겠음.
def sol():
    N = int(input().strip())
    l = []
    for _ in range(N):
        l.append(tuple(map(int, input().strip().split())))
    
    l.sort(key=lambda x: (x[0], x[1]-x[0])) # 첫째 값 오름차순. 그 다음 길이 오름차순
    
    left, right = 0, 1
    prev = 0
    max_length = 1
    while True:
        ls, le = l[left]
        rs, re = l[right]
        if prev == left: # prev check 안함.
            if le > rs:
                right+=1
            else:                
                right+=1
                left+=1
        return
    ...
        
    
if __name__ == '__main__':
    sol()
    
# Answer (정렬 후, 활성 선분을 찾는 방식. On, Off와 비슷함 (-1과 +1 사용))
def max_overlapping_segments(segments):
    events = []
    
    # 각 선분의 시작점과 끝점을 이벤트로 저장
    for s, e in segments:
        # 시작점은 1, 끝점은 -1로 표시 (동일 좌표에서는 끝점이 먼저 처리되도록)
        events.append((s, 1))  # 시작점
        events.append((e, -1))  # 끝점
    
    # 이벤트를 좌표 기준으로 정렬
    # 같은 좌표의 경우 끝점(-1)이 먼저 오도록 정렬 (겹치는 것으로 세지 않기 위해)
    events.sort()
    
    current_count = 0  # 현재 활성화된 선분 수
    max_count = 0      # 최대 겹침 수
    
    for _, event_type in events:
        current_count += event_type  # 시작점(1)이면 증가, 끝점(-1)이면 감소
        max_count = max(max_count, current_count)
    
    return max_count

# 입력 처리
n = int(input())
segments = []
for _ in range(n):
    s, e = map(int, input().split())
    segments.append((s, e))

# 결과 출력
print(max_overlapping_segments(segments))