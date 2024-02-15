## COMMENT: 내가 너무 어렵게 생각하고, 규칙을 발견하는 것에만 정신이 팔려있음...
## brute force를 그냥 쓰기도 하자.
"""
    답의 조합이 여러 개일 수 있음. 여러 가지가 존재하는 tree 처럼.

    현재 위, 자릿값 => 아랫값, 다음 자리 위

    0, o+d % 10 = n[0], o+d / 10
    
    ((o+d / 10) + 2*l) % 10 = n[1], ((o+d / 10) + 2*l) / 10
    
    ((((o+d / 10) + 2*l) / 10) + l + r) % 10 = n[2], ((((o+d / 10) + 2*l) / 10) + l + r) / 10

"""

import sys
import itertools

def main():
    n = sys.stdin.readline().rstrip('\n')
    answer = int(n)
    hello = 0
    world = 0
    exist_answer = False
    for s in itertools.permutations(range(10), 7):
        h, w, e, o, l, r, d = s
        if h == 0 or w == 0:
            continue

        hello = 10000 * h + 1000 * e + 100 * l + 10 * l + o
        world = 10000 * w + 1000 * o + 100 * r + 10 * l + d

        if hello + world == answer:
            exist_answer = True
            break
    
    if exist_answer:
        print(f"  {hello}")
        print(f"+ {world}")
        print("-------")
        print(f" {answer}".rjust(7, " "))
    else:
        print("No Answer")
    sys.exit()


if __name__ == "__main__":
    main()
