# """
# 이모티콘
# 2 초	512 MB
# 문제
# 영선이는 매우 기쁘기 때문에, 
# 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.

# 영선이는 이미 화면에 이모티콘 1개를 입력했다. 
# 이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.

# 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 화면에 있는 이모티콘 중 하나를 삭제한다.
# 모든 연산은 1초가 걸린다. 
# 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다. 
# 클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다.
# 또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다. 
# 화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.

# 영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 S (2 ≤ S ≤ 1000) 가 주어진다.

# 출력
# 첫째 줄에 이모티콘을 S개 만들기 위해 필요한 시간의 최솟값을 출력한다.

# 예제 입력 1 
# 2
# 예제 출력 1 
# 2
# 예제 입력 2 
# 4
# 예제 출력 2 
# 4
# 예제 입력 3 
# 6
# 예제 출력 3 
# 5
# 예제 입력 4 
# 5
# 예제 출력 4 
# 8
# 예제 입력 5 
# 18
# 예제 출력 5 
# 8
# 출처
# 문제를 번역한 사람: baekjoon
# """
# ## 1. BFS. 1d array. => copy된 것을 고려하기 위하여 2차원 배열로 풀어야 함. 
# from collections import deque
# import sys
# input = sys.stdin.readline

# def main(S):
#     # S = int(input().rstrip())
#     emoji = [1 << 11]* 1025 # 최대 1024까지 갈 듯.
#     emoji[1] = 0
#     q = deque()
#     q.appendleft((1, 0, 0))

#     while q: 
#         start, copy, count = q.pop()

#         if start == S:
#             continue
#         # copy:
#         if (0 < start*2 <= 1000 
#             and start != copy
#             ):
#             q.appendleft((start, start, count+1))
#         # paste:
#         if (start+copy < 1025 
#             and emoji[start+copy] >= count+1
#             ):
#             emoji[start+copy] = count+1    
#             q.appendleft((start+copy, copy, count+1))
#         # delete:
#         if (emoji[start-1] >= count+1
#             and start-1 >= 0
#             ):
#             emoji[start-1] = count+1
#             q.appendleft((start-1, copy, count+1))
        
#     return emoji[S]


# # if __name__ == '__main__':
# #     main()

# ## 2. BFS. 2d array. 현재 값, 클립보드 값.
# from collections import deque
# import sys
# input = sys.stdin.readline

# def main():
#     S = int(input().rstrip())
#     emoji = [[(1 << 11) - 1]* 1025 for _ in range(1025)] # 최대 1024까지 갈 듯.
#     emoji[1][0] = 0 # 현재과 클립보드값.
#     q = deque()
#     q.appendleft((1, 0))

#     while q: 
#         start, copy = q.pop()

#         if start == S: # 이후로 더 연산하지 않음.
#             break

#         # copy:
#         if start*2 <= 1024 and emoji[start][start] == 2047:
#             emoji[start][start] = emoji[start][copy] + 1
#             q.appendleft((start, start))
#         # paste:
#         if start+copy <= 1024 and emoji[start+copy][copy] == 2047:
#             emoji[start+copy][copy] = emoji[start][copy] + 1   
#             q.appendleft((start+copy, copy))
#         # delete:
#         if start-1 > 0 and emoji[start-1][copy] == 2047:
#             emoji[start-1][copy] = emoji[start][copy] + 1
#             q.appendleft((start-1, copy))
        
#     print(min(emoji[S]))


# if __name__ == '__main__':
#     main()


## 3. 1d array. copy 부분을 하나씩 늘려나갔음. 출처:sk14cj
from collections import deque

s = int(input())

INF = int(1e9)

visited = [INF] * (2 *(s+1))

def solution(visited):
    queue = deque([1])
    visited[1] = 0
    while queue:
        vx = queue.popleft()
        nx = vx - 1
        if nx >= 0 and visited[nx] > visited[vx] + 1:
            visited[nx] = visited[vx] + 1
            queue.append(nx)
        for i in range(2,2001):
            nx = vx * i
            if nx > 2*s:
                break
            if visited[nx] > visited[vx] + i:
                visited[nx] = visited[vx] + i
                queue.append(nx)

solution(visited)

answer = visited[s]

print(answer)


    