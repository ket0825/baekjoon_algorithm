"""
이모티콘
2 초	512 MB
문제
영선이는 매우 기쁘기 때문에, 
효빈이에게 스마일 이모티콘을 S개 보내려고 한다.

영선이는 이미 화면에 이모티콘 1개를 입력했다. 
이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.

화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
화면에 있는 이모티콘 중 하나를 삭제한다.
모든 연산은 1초가 걸린다. 
또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다. 
클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다.
또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다. 
화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.

영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 S (2 ≤ S ≤ 1000) 가 주어진다.

출력
첫째 줄에 이모티콘을 S개 만들기 위해 필요한 시간의 최솟값을 출력한다.

예제 입력 1 
2
예제 출력 1 
2
예제 입력 2 
4
예제 출력 2 
4
예제 입력 3 
6
예제 출력 3 
5
예제 입력 4 
5
예제 출력 4 
8
예제 입력 5 
18
예제 출력 5 
8
출처
문제를 번역한 사람: baekjoon
"""
## 1. BFS. 1d array. 왜 2d array로 사람들이 풀지...?
from collections import deque
import sys
input = sys.stdin.readline


def main():
    S = int(input().rstrip())
    emoji = [1 << 11]* 1025 # 최대 1024까지 갈 듯.
    emoji[1] = 0
    q = deque()
    q.appendleft((1, 0, 0))

    while q: 
        start, copy, count = q.pop()

        if start == S:
            break
        # copy:
        if (0 < start*2 <= 1000 
            and start != copy
            ):
            q.appendleft((start, start, count+1))
        # paste:
        if (start+copy < 1025 
            and emoji[start+copy] >= count+1
            ):
            emoji[start+copy] = count+1    
            q.appendleft((start+copy, copy, count+1))
        # delete:
        if (emoji[start-1] >= count+1
            and start-1 >= 0
            ):
            emoji[start-1] = count+1
            q.appendleft((start-1, copy, count+1))
        
    print(emoji[S])


if __name__ == '__main__':
    main()







    