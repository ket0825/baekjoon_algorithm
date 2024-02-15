"""
출력
첫째 줄에 입력으로 주어진 순열의 이전에 오는 순열을 출력한다. 만약, 사전순으로 가장 처음에 오는 순열인 경우에는 -1을 출력한다.

예제 입력 1 
4
1 2 3 4
예제 출력 1 
-1
예제 입력 2 
5
5 4 3 2 1
예제 출력 2 
5 4 3 1 2
"""

import sys
input = sys.stdin.readline

def main():
    N = int(input().rstrip("\n"))
    sequence = list(map(int,input().rstrip("\n").split(" ")))

    # 1 "4" 3 2 5
    key_idx = 0
    swap_idx = 0
    first_sequence = True
    for i in range(N-1, 0, -1):
        if sequence[i] < sequence[i-1]:
            key_idx = i-1
            swap_idx = i
            first_sequence = False
            break

    if first_sequence:
        print(-1)
        return
    
    for i in range(swap_idx, N):
        if sequence[key_idx] > sequence[i] and sequence[i] > sequence[swap_idx]:
            swap_idx = i

    sequence[swap_idx], sequence[key_idx] = sequence[key_idx], sequence[swap_idx]

    print(" ".join(map(str, sequence[:key_idx+1]+sorted(sequence[key_idx+1:], reverse=True))))


def next_permu(sequence):
    N = len(sequence)

    key_idx = 0
    swap_idx = 0
    first_sequence = True
    for i in range(N-1, 0, -1):
        if sequence[i] < sequence[i-1]:
            key_idx = i-1
            swap_idx = i
            first_sequence = False
            break

    if first_sequence:
        
        return -1
    
    for i in range(swap_idx, N):
        if sequence[key_idx] > sequence[i] and sequence[i] > sequence[swap_idx]:
            swap_idx = i

    sequence[swap_idx], sequence[key_idx] = sequence[key_idx], sequence[swap_idx]

    return " ".join(map(str, sequence[:key_idx+1]+sorted(sequence[key_idx+1:], reverse=True)))

if __name__ == "__main__":
    # main()
    import itertools
    N = 100
    cnt = 0
    prev_permu = None
    is_correct = True
    for permu in itertools.permutations(range(1, N+1), N):
        if cnt == 0:
            is_correct = next_permu(list(permu)) == -1
            print(is_correct)
        else:
            is_correct = prev_permu == next_permu(list(permu))
            print(is_correct)
        cnt+=1
        prev_permu = " ".join(map(str, permu))

        if not is_correct:
            print("here!")