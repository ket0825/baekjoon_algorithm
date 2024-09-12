"""
경사로 14890
시간 제한	메모리 제한
2 초	512 MB
"""
# My answer
import sys
input = sys.stdin.readline

def main():
    N, L = map(int, input().rstrip().split()) #  N (2 ≤ N ≤ 100), L (1 ≤ L ≤ N)
    mat = [list(map(int, input().rstrip().split())) for _ in range(N)]
    
    number_of_roads = 0
    
    # print("row-wise")
    for nrow in range(N):
        installed_set = set()
        is_road = True
        for ncol in range(1, N):            
            if abs(mat[nrow][ncol] - mat[nrow][ncol-1]) > 1:
                is_road = False
                continue            
            elif mat[nrow][ncol] - mat[nrow][ncol-1] == 0:
                pass                            
            elif mat[nrow][ncol] - mat[nrow][ncol-1] == 1: # ascending.
                if (ncol - L) < 0: # out of index.
                    is_road = False
                    continue
                
                # check can install runway.
                can_install_runway = True
                for runway_idx in range(ncol-L, ncol): # ascending way.
                    
                    if runway_idx in installed_set:
                        can_install_runway = False
                        break
                    
                    installed_set.add(runway_idx)
                
                if not can_install_runway:
                    is_road = False
                    continue
                
            elif mat[nrow][ncol] - mat[nrow][ncol-1] == -1: # descending.
                if (ncol + L) > N: # out of index.
                    is_road = False
                    # print("out of descending index")
                    continue
                                
                # check can install runway.
                can_install_runway = True
                for runway_idx in range(ncol, ncol+L): # descending way.
                    if runway_idx in installed_set:
                        can_install_runway = False
                        break
                    
                    installed_set.add(runway_idx)
                
                if not can_install_runway:
                    is_road = False
                    continue
                
        if is_road:
            # print(f"road: {nrow}")
            number_of_roads+=1
    
    # same, but colwise.            
    # print("col-wise")
    for ncol in range(N):
        installed_set = set()
        is_road = True
        for nrow in range(1, N):      
            if abs(mat[nrow][ncol] - mat[nrow-1][ncol]) > 1:
                is_road = False
                continue            
            elif mat[nrow][ncol] - mat[nrow-1][ncol] == 0:
                pass                            
            elif mat[nrow][ncol] - mat[nrow-1][ncol] == 1: # ascending.
                if (nrow - L) < 0: # out of index.
                    is_road = False
                    continue
                                
                # check can install runway.
                can_install_runway = True
                for runway_idx in range(nrow-L, nrow): # ascending way.
                    
                    if runway_idx in installed_set:
                        can_install_runway = False
                        break
                    
                    installed_set.add(runway_idx)
                
                if not can_install_runway:
                    is_road = False
                    continue
                
            elif mat[nrow][ncol] - mat[nrow-1][ncol] == -1: # descending.
                if (nrow + L) > N: # out of index.
                    is_road = False
                    continue
                                
                # check can install runway.
                can_install_runway = True
                for runway_idx in range(nrow, nrow+L): # descending way.
                    if runway_idx in installed_set:
                        can_install_runway = False
                        break
                    
                    installed_set.add(runway_idx)
                
                if not can_install_runway:
                    is_road = False
                    continue
                
        if is_road:
            # print(f"road: {ncol}")
            number_of_roads+=1
    
    print(number_of_roads)
                        
    
if __name__ =='__main__':
    main()
    

# 	qkrrhksdn011. else 위치가 특이함. 함수 잘 사용한 듯. 물론 보기에는 어려움.
    
"""
n,l=map(int,input().split())

board=[]

for i in range(n):
    board.append(list(map(int,input().split())))

for i in zip(*board):
    board.append(list(i))
def up(y,x):
    if x<l:
        return False
    start=board[y][x-l]
    for i in range(x-l,x):
        if visited[i]==1 and board[i]!=start:
            return False
    else:
        for i in range(x-l,x):
            visited[i]=1
    return True

def down(y,x):
    if x+l>n:
        return False
    start=board[y][x]
    for i in range(x,x+l):
        if visited[i]==1 and board[i]!=start:
            return False
    else:
        for i in range(x,x+l):
            visited[i]=1
    return True

answer=0
for i in range(len(board)):
    visited=[0]*n
    height=board[i][0]
    for j in range(n):
        if board[i][j]>height:
            if board[i][j]-height<2 and up(i,j):
                height=board[i][j]
            else:
                break
        elif board[i][j]<height:
            if height-board[i][j]<2 and down(i,j):
                height=board[i][j]
            else:
                break
    else:
        answer+=1
print(answer)
"""