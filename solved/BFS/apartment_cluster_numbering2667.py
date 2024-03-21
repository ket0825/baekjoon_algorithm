"""
단지번호붙이기
1 초	128 MB
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 
1은 집이 있는 곳을, 
0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 
단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우,
혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. 
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 
각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
예제 출력 1 
3
7
8
9
출처
Olympiad > 한국정보올림피아드 > KOI 1996 > 초등부 1번

잘못된 데이터를 찾은 사람: djm03178
데이터를 추가한 사람: djm03178, jh05013
문제의 오타를 찾은 사람: metadata
"""

## 1. graph search N^2 by queue and memo.
from collections import deque
import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip()) # 5≤N≤25
    board = ["" for _ in range(N+2)]
    for i in range(N+2):
        if i == 0 or i == N+1:
            board[i] = "2"*(N+2)
        else:
            board[i] = "2" + input().rstrip() + '2'      
    
    visited = [[False for _ in range(N+2)] for _ in range(N+2)]

    cluster_count = 0
    apartment_count_list = []

    def check_NEWS(x, y, count):
        local_count = count
        if board[x+1][y] == '1' and not visited[x+1][y]:
            visited[x+1][y] = True
            local_count += 1
            q.appendleft((x+1, y))
        if board[x-1][y] == '1' and not visited[x-1][y]:
            visited[x-1][y] = True
            local_count += 1
            q.appendleft((x-1, y))
        if board[x][y+1] == '1' and not visited[x][y+1]:
            visited[x][y+1] = True
            local_count += 1
            q.appendleft((x, y+1))
        if board[x][y-1] == '1' and not visited[x][y-1]:
            visited[x][y-1] = True
            local_count += 1
            q.appendleft((x, y-1))
        
        return local_count

    for i in range(1,N+1):
        for j in range(1,N+1):
            if not visited[i][j] and board[i][j] == '1':
                local_count = 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    x, y = q.pop()
                    local_count = check_NEWS(x, y, local_count)

                cluster_count+=1
                apartment_count_list.append(local_count)
                
    print(cluster_count)
    
    if apartment_count_list:
        print(*sorted(apartment_count_list), sep='\n')

    
if __name__ == '__main__':
    main()


## 2. DFS and better marking (mark in graph): 출처: sokhyg9016
def bfs(i, j):
    que = [(i, j)]
    nums_house = 1
    houses[i][j] = 0
    
    while que:
        i, j = que.pop(0)
        
        for dir_x, dir_y in [(0,1),(0,-1),(1,0),(-1,0)]:
            x = i + dir_x
            y = j + dir_y
            
            if x < 0 or x > n-1 or y < 0 or y > n-1:
                continue
            
            if houses[x][y] == 1:
                houses[x][y] = 0
                que.append((x, y))
                nums_house += 1
                
    return nums_house


n = int(input())
houses = [[int(el) for el in input()] for _ in range(n)]
groups = []

for i in range(n):
    for j in range(n):
        if houses[i][j]:
            groups.append(bfs(i, j))

groups.sort()
print(len(groups))
print('\n'.join(map(str, groups)))


## 3. DFS by formulation. 출처: dksrud0907
from collections import deque

n = int(input())

matrix = []
for i in range(n):
    matrix.append([int(x) for x in input()])

visited = [[False] * n for _ in range(n)]
num_city = 0
peoples = []

def dfs(start):
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    stack = deque()
    stack.append((start[0], start[1]))

    size = 0

    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        if matrix[x][y] == 0:
            continue
        size += 1
        visited[x][y] = True

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == 1 and not visited[nx][ny]:
                    stack.append((nx, ny))
    return size


for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        if matrix[i][j] == 0:
            visited[i][j] = True
            continue

        num_city += 1
        peoples.append(dfs((i, j)))

print(num_city)
peoples.sort()
for num in peoples:
    print(num)