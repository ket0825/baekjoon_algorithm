"""
시간 제한	메모리 제한	제출
1 초	512 MB

문제
어른 상어가 마법사가 되었고, 파이어볼을 배웠다.

마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사했다. 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다. i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미한다.

격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.

파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미하며, 정수로는 다음과 같다.

7	0	1
6	 	2
5	4	3
마법사 상어가 모든 파이어볼에게 이동을 명령하면 다음이 일들이 일어난다.

모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
파이어볼은 4개의 파이어볼로 나누어진다.
나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
질량이 0인 파이어볼은 소멸되어 없어진다.
마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.

입력
첫째 줄에 N, M, K가 주어진다.

둘째 줄부터 M개의 줄에 파이어볼의 정보가 한 줄에 하나씩 주어진다. 파이어볼의 정보는 다섯 정수 ri, ci, mi, si, di로 이루어져 있다.

서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다.

출력
마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 출력한다.

제한
4 ≤ N ≤ 50
0 ≤ M ≤ N2
1 ≤ K ≤ 1,000
1 ≤ ri, ci ≤ N
1 ≤ mi ≤ 1,000
1 ≤ si ≤ 1,000
0 ≤ di ≤ 7
예제 입력 1 
4 2 1
1 1 5 2 2
1 4 7 1 6
예제 출력 1 
8
예제 입력 2 
4 2 2
1 1 5 2 2
1 4 7 1 6
예제 출력 2 
8
예제 입력 3 
4 2 3
1 1 5 2 2
1 4 7 1 6
예제 출력 3 
0
예제 입력 4 
7 5 3
1 3 5 2 4
2 3 5 2 6
5 2 9 1 7
6 2 1 3 5
4 4 2 4 2
예제 출력 4 
9
"""

"""
파이어볼 위치: r_i, c_i
질량 m_i
방향 d_i
속력 s_i

1번행은 N번과 연결? 1번 열은 N번 열과 연결?

방향: 
7 0 1
6   2
5 4 3

방향 d로 s칸만큼 이동.

이동 후에, 2개 이상의 파이어볼이 있는 칸은 일 일어남.
1. 하나로 합쳐지고
2. 4개로 나눠지고
3. 질량: 질량 합 / 5 -> 손실 발생. 이걸로 끝날듯
    속력: 속력 합 / 합쳐진 것 개수
    방향이 모두 홀수이거나 짝수이면 0,2,4,6이고, 아니면 1,3,5,7
    질량 0이면 소멸
    
k번 명령한 후 남아있는 파이어볼 질량 합 구하기.


"""

import sys

input = sys.stdin.readline

def decide_next_pos(pos, speed, d, N):
    pos_r, pos_c = pos
    if d == 0:
        return (pos_r-1*speed) % N, pos_c
    elif d == 1:
        return (pos_r-1*speed) % N, (pos_c+1*speed) % N
    elif d == 2:
        return pos_r, (pos_c+1*speed) % N
    elif d == 3:
        return (pos_r+1*speed) % N, (pos_c+1*speed) % N
    elif d == 4:
        return (pos_r+1*speed) % N, pos_c
    elif d == 5:
        return (pos_r+1*speed) % N, (pos_c-1*speed) % N
    elif d == 6:
        return pos_r, (pos_c-1*speed) % N
    elif d == 7:
        return (pos_r-1*speed) % N, (pos_c-1*speed) % N  

def check_more_than_2(pos, mat):
    i, j = pos
    if len(mat[i][j]) >= 2:
        return True    
    return False

def clear_lists(fireball_pos, fireball_mass, fireball_speed, fireball_direction):
    fireball_pos.clear()
    fireball_mass.clear()
    fireball_speed.clear()
    fireball_direction.clear()
    
def collision(mat, pos, fireball_pos, fireball_mass, fireball_speed, fireball_direction):
    # 충돌 일어난 곳에서 다 계산해서 fireball_list들에 다시 분배
    # 그리고 분배하면 분배한 matrix 요소 clean    
    pos_r, pos_c = pos
    sum_m, sum_s = 0, 0
    d_list = []
    
    for m, s, d in mat[pos_r][pos_c]:
        sum_m += m
        sum_s += s
        d_list.append(d)
        
    # print(f"질량 합:{sum_m}")
    
    is_odd = (d_list[0] % 2 == 1)
    same = True
    for i in d_list[1:]:
        if (i % 2 == 1) != is_odd:
            same = False
            break
    
    fireball_pos.extend([pos]*4)
    fireball_mass.extend([sum_m//5]*4) 
    fireball_speed.extend([sum_s // len(mat[pos_r][pos_c])]*4)
    
    if same: # 0,2,4,6
        fireball_direction.extend([0,2,4,6])
    else:
        fireball_direction.extend([1,3,5,7])
        
    # print(f"fireball_pos: {fireball_pos}")
    # print(f"fireball_mass: {fireball_mass}")
    # print(f"fireball_speed: {fireball_speed}")
    # print(f"fireball_direction: {fireball_direction}")
    
    mat[pos_r][pos_c].clear()
        
        
def solution():    
    
    N, M, K = map(int, input().split())
    fireball_pos = [0] * M
    fireball_mass = [0] * M
    fireball_speed = [0] * M
    fireball_direction = [0] * M
    for i in range(M):
        r, c, m, s, d = map(int, input().split())        
        fireball_pos[i] = ((r-1), (c-1))
        fireball_mass[i] = m
        fireball_speed[i] = s
        fireball_direction[i] = d
    # 최대 = N*3*K = 2500* 50 * 1000 = 125000000...
    mat = [[[] for _ in range(N)]  for _ in range(N)] # N * N
    # K번 iteration
    for k in range(K): # K * 
        pos_checklist = []
        # print(f"{k} fireball_pos: {fireball_pos}")
        for i in range(len(fireball_pos)): # M *
            pos = fireball_pos[i]                          
            new_pos = decide_next_pos(pos, fireball_speed[i], fireball_direction[i], N)
            new_pos_r, new_pos_c = new_pos            
            # print(f"new_pos: {new_pos}")            
            # print(f"기존 위치: {mat[new_pos_r][new_pos_c]}")
            mat[new_pos_r][new_pos_c].append((fireball_mass[i], fireball_speed[i], fireball_direction[i]))
            # print(f"길이: {len(mat[new_pos_r][new_pos_c])}")
            if len(mat[new_pos_r][new_pos_c]) <= 1:
                pos_checklist.append(new_pos)                    
        # print(*mat, sep="\n")        
        # clean lists
        clear_lists(fireball_pos, fireball_mass, fireball_speed, fireball_direction)
                    
        # 충돌 일어난 곳에서 다 계산해서 fireball_list들에 다시 분배
        # 그리고 분배하면 분배한 matrix 요소 clear
        # clear이후 다시 fireball_list에서 matrix로 넣음. 
        # print(f"pos_checklist: {pos_checklist}")       
        for pos in pos_checklist: 
            if check_more_than_2(pos, mat):
                collision(mat, pos, fireball_pos, fireball_mass, fireball_speed, fireball_direction)
            else:
                fireball_pos.append(pos)
                r, c = pos                
                m, s, d = mat[r][c][0]
                fireball_mass.append(m)
                fireball_speed.append(s)
                fireball_direction.append(d)
                mat[r][c].clear()                
        
    print(sum(fireball_mass))

if __name__ == "__main__":        
    solution()


