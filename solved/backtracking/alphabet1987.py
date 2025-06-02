"""
알파벳 다국어
시간 제한	메모리 제한
2 초	256 MB
문제
세로 
$R$칸, 가로 
$C$칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (
$1$행 
$1$열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 
$R$과 
$C$가 빈칸을 사이에 두고 주어진다. (
$1 ≤ R,C ≤ 20$) 둘째 줄부터 
$R$개의 줄에 걸쳐서 보드에 적혀 있는 
$C$개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

예제 입력 1 
2 4
CAAB
ADCB
예제 출력 1 
3
예제 입력 2 
3 6
HFDFFB
AJHGDH
DGAGEH
예제 출력 2 
6
예제 입력 3 
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
예제 출력 3 
10

"""
import sys
sys.setrecursionlimit(1000) # 메모리를 pypy3에서 먼저 잡음.

input = sys.stdin.readline

def sol():
    R, C = map(int, input().strip().split())
    graph = [list(map(lambda x:ord(x)-65, input())) for _ in range(R)]
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    
    visited = [False]*26    
    
    def dfs(r, c, count):        
        # 26개의 count라면 early return 가능!
        # stack으로 dfs 구현 시에 OK.
        result = count
        for i in [0,1,2,3]:
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C: 
                v_idx = graph[nr][nc]
                if not visited[v_idx]:
                    visited[v_idx] = True
                    result = max(result, dfs(nr,nc,count+1))
                    visited[v_idx] = False

        return result
    
    visited[graph[0][0]] = True
    print(dfs(0,0,1))    
    

if __name__ == '__main__':
    sol()


# 20 20
# QWERTYUIOPASDFGHJKLZ
# WERTYUIOPASDFGHJKLZX
# ERTYUIOPASDFGHJKLZXC
# RTYUIOPASDFGHJKLZXCV
# TYUIOPASDFGHJKLZXCVB
# YUIOPASDFGHJKLZXCVBN
# UIOPASDFGHJKLZXCVBNM
# IOPASDFGHJKLZXCVBNMQ
# OPASDFGHJKLZXCVBNMQA
# PASDFGHJKLZXCVBNMQAA
# ASDFGHJKLZXCVBNMQAAA
# SDFGHJKLZXCVBNMQAAAA
# DFGHJKLZXCVBNMQAAAAA
# FGHJKLZXCVBNMQAAAAAA
# GHJKLZXCVBNMQAAAAAAA
# HJKLZXCVBNMQAAAAAAAA
# JKLZXCVBNMQAAAAAAAAA
# KLZXCVBNMQAAAAAAAAAA
# LZXCVBNMQAAAAAAAAAAA
# ZXCVBNMQAAAAAAAAAAAA