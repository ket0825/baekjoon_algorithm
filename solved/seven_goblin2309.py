import sys
from itertools import combinations
def main():
    lines_count = 9
    inputs = [sys.stdin.readline().rstrip("\n") for i in range(lines_count)]
    inputs_num = list(map(int, inputs))
    inputs_num.sort()
    for combo in combinations(inputs_num, 7):
        if sum(combo) == 100:
            print(*combo, sep="\n")
            exit()
if __name__ == '__main__':
    main()

"""
20
7
23
19
10
15
25
8
13
"""