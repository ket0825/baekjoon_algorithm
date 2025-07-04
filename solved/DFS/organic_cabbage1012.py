"""
유기농 배추
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	221584	92382	60995	39.267%
문제
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

1	1	0	0	0	0	0	0	0	0
0	1	0	0	0	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	1	1	0	0	0	1	1	1
0	0	0	0	1	0	0	1	1	1
입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

예제 입력 1 
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
예제 출력 1 
5
1
예제 입력 2 
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def sol(M, N, K, locations):
    mat = [[0 for _ in range(M)] for _ in range(N)]
    for loc in locations:
        col, row = loc
        mat[row][col] = 1    

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    
    def dfs(cur_row, cur_col):        
        for i in range(4):
            nr = cur_row + dr[i]
            nc = cur_col + dc[i]
            if (0 <= nr < N 
                and 0 <= nc < M
                and mat[nr][nc] == 1
                ):
                # print(f"체크: r,c : {nr}, {nc}")
                mat[nr][nc] = 0
                dfs(nr, nc)

    cnt = 0
    for r in range(N):
        for c in range(M):
            if mat[r][c] == 1:
                mat[r][c] = 0
                # print(f"시작: r,c : {r}, {c}")
                cnt+=1
                dfs(r, c)
    
    print(cnt)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        locations = []
        M, N, K = map(int, input().strip().split())
        for _ in range(K):
            loc = tuple(map(int, input().strip().split()))
            locations.append(loc)            
        sol(M, N, K, locations)