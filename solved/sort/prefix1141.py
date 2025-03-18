"""
접두사
시간 제한	메모리 제한
2 초	128 MB

문제
접두사 X 집합이란 집합의 어떤 한 단어가, 
다른 단어의 접두어가 되지 않는 집합이다. 

예를 들어, {hello}, {hello, goodbye, giant, hi}, 비어있는 집합은 
모두 접두사X 집합이다.

하지만, {hello, hell}, {giant, gig, g}는 접두사X 집합이 아니다.

단어 N개로 이루어진 집합이 주어질 때, 
접두사X 집합인 부분집합의 최대 크기를 출력하시오.

입력
첫째 줄에 단어의 개수 N이 주어진다. 

N은 50보다 작거나 같은 자연수이다. 

둘째 줄부터 N개의 줄에는 단어가 주어진다. 

단어는 알파벳 소문자로만 이루어져 있고, 길이는 최대 50이다. 

집합에는 같은 단어가 두 번 이상 있을 수 있다.

출력
첫째 줄에 문제의 정답을 출력한다.

예제 입력 1 
6
hello
hi
h
run
rerun
running
예제 출력 1 
4

예제 입력 2 
6
a
b
cba
cbc
cbb
ccc
예제 출력 2 
6

예제 입력 3 
6
a
ab
abc
abcd
abcde
abcdef
예제 출력 3 
1

예제 입력 4 
3
topcoder
topcoder
topcoding
예제 출력 4 
2

"""

test_case = """6
hello
hi
h
run
rerun
running
---
6
a
b
cba
cbc
cbb
ccc
---
6
a
ab
abc
abcd
abcde
abcdef
---
3
topcoder
topcoder
topcoding
---
11
a
apple
ate
b
ball
c
candy
d
e
f
g
"""

answers = """4
---
6
---
1
---
2
---
8
"""

import sys

input = sys.stdin.readline

def sol():
    N = int(input().strip())
    words = []
    for _ in range(N): # 1 <= N <= 50. 자연수
        words.append(input().strip())        # 단어 당 최대 50자.        
    # 일단 단어의 길이별 정렬 필요.
    words = sorted(words, key=lambda x: len(x))
    # 그 다음 , 자기 이후를 보며, 자신이 접두사인지 체크.
    # 아니라면, 답을 더해줌.
    answer = 0
    for prefix_idx in range(N):
        is_prefix = False # 현재가 접두사인가요?
        for check in range(prefix_idx+1, N):            
            if words[check].startswith(words[prefix_idx]): # 접두사인지 체크 로직
                is_prefix = True
                break
        if not is_prefix: # 접두사 아니면 답 하나 더하기.
            # print("prefix 없음.", words[prefix_idx])
            answer+=1
    
    print(answer)    

if __name__ == '__main__':
    sol()
    
