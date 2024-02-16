"""
문제
비어있는 공집합 S가 주어졌을 때, 
아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) 
S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. 
(1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 
없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 
없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.

예제 입력 1 
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
예제 출력 1 
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
출처
문제를 만든 사람: baekjoon
빠진 조건을 찾은 사람: djm03178
데이터를 추가한 사람: guswhd903, houma757, leeingyun96
문제의 오타를 찾은 사람: pichulia
"""

## 1. set 연산 없이 구현해보자. 테스트 코드 추가함.
import sys
input = sys.stdin.readline

def main():
    answer = """1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0"""
    ans = list(map(int, answer.split("\n")))
    print(ans)
    N = int(input().rstrip("\n")) # 1 <= N <= 1000000
    S = 0b00000000000000000000  # 1 <= x <= 20
    ans_cnt = 0

    for _ in range(N):
        prompt = input().rstrip("\n").split(" ")
        try:
            num = int(prompt[1])
        except:
            pass
        command = prompt[0]

        if command == "add":
            S |= (1 << (num-1))
            # print(format(S, 'b'))
        elif command == "check": # 있으면 print(1), 없으면 print(0)            
            print(1 if S & (1 << (num-1)) > 0 else 0)
            assert (1 if S & (1 << (num-1)) > 0 else 0) == ans[ans_cnt], "틀렸습니다."
            ans_cnt +=1
            # print(format(S, 'b'))
        elif command == "remove": # 있으면 제거. 없으면 무시.
            S &= ~(1 << (num - 1))
            print(format(S, 'b'))
        elif command == "toggle": # 있으면 제거, 없으면 추가.
            S ^= (1 << (num-1))
            # print(format(S, 'b'))
        elif command == "all":
            S = (1 << 20) - 1
            # print(format(S, 'b'))
        elif command == "empty":
            S = 0
            # print(format(S, 'b'))

        

if __name__ == "__main__":
    main()
    # S = 0b00000000000000000000
    # S = (1 << 20) - 1 
    # print(len(format(S, 'b')))


## 2. 아이디: younghch42. mask 변수 두고 한 풀이. 가독성이 더 좋음. 
    # try except 같은 잔재주 없음.
    # 그리고 기준이 21자리로 하고 0을 체크하지 않음.
import sys

def main():
    input_ = sys.stdin.readline
    n = int(input_())
    current = 0
    for _ in range(n):
        commands = input_().split()
        operation = commands[0]
        if len(commands) ==1:
            match operation:
                    case 'all':
                        current = (1<<21)-1
                    case 'empty':
                        current = 0
        else:
            mask = 1<<int(commands[1])
            match operation:
                case 'add':
                    current |= mask
                case 'remove':
                    current &= ~mask
                case 'check':
                    if current & mask == 0:
                        print(0)
                    else:
                        print(1)
                case 'toggle':
                    current ^= mask
                        
if __name__ == '__main__':
    main()

## 3. 아이디: maengjh. 의외로 in 연산자와 list를 사용해도 생각보다 성능이 좋음.
import sys

def function():
    N = int(input())

    S = []

    for _ in range(N):
        command = sys.stdin.readline().split()

        if command[0] == "all":
            S = [i for i in range(1, 21)]
        elif command[0] == "empty":
            S = []
        else:
            num = int(command[1])

            if command[0] == "add" and num not in S:
                S.append(num)
            elif command[0] == "remove" and num in S:
                S.remove(num)
            elif command[0] == "toggle":
                if num in S:
                    S.remove(num)
                else:
                    S.append(num)
            elif command[0] == "check":
                sys.stdout.write('1\n' if num in S else '0\n')


if __name__ == "__main__":
    function()


## 비트 연산 정리.
A = 0b0000
B = 0b0110
C = 0b1110
mask = 1 << 2 # 1을 왼쪽으로 2만큼 shift
mask = 1 >> 2 # 1을 오른쪽으로 2만큼 shift
A & B # and 연산자
A | B # or 연산자
~B # not 연산자.
A ^ B # XOR 연산자.

A & mask # mask에 해당하는 자릿수 찾기.
B & ~mask # mask에 해당하는 자릿수 제거하기.
C | mask # mask에 해당하는 자릿수 더하기
C ^ ~mask # mask에 해당하는 자릿수 0과 1 전환하기.
