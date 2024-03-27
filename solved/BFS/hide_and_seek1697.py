"""
숨바꼭질
2 초	128 MB	242347	71149	45072	25.788%
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 

만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
힌트
수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.
"""
## 1. BFS.
from collections import deque
import sys
input = sys.stdin.readline

def BFS(N, K):
    if N > K:
        print(N-K)
        return
    
    L = [-1] * 100001
    q = deque([N])
    L[N] = 0
    start = N
    end = K

    while start != end:
        start = q.pop()

        for i in [start+1, start-1, start*2]:
            if (0 <= i < 100001
                and L[i] == -1
                ):
                q.appendleft(i)
                L[i] = L[start] + 1
                if i == K:
                    end = start
                    break
     
    print(L[K])



def main():
    N, K = map(int, input().rstrip().split(" "))
    BFS(N, K)


if __name__ == '__main__':
    main()

## 2. 좀 더 심플하게 풀기. 출처: ktw9028
from collections import deque
def sol():
	#01
    q=deque([n])
    while q:
        x=q.popleft()
        if x==k:
            return ans[x]
        #02
        for i in (x-1,x+1,2*x):
            if 0<=i<=10**5 and not ans[i]:
                ans[i]=ans[x]+1
                q.append(i)
#03
ans=[0]*(10**5+1)
n,k=map(int,input().split())
print(sol())