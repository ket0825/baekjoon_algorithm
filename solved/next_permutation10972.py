"""
문제
1부터 N까지의 수로 이루어진 순열이 있다. 이때, 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성하시오.

사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다.

N = 3인 경우에 사전순으로 순열을 나열하면 다음과 같다.

1, 2, 3
1, 3, 2
2, 1, 3
2, 3, 1
3, 1, 2
3, 2, 1

입력
첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.

출력
첫째 줄에 입력으로 주어진 순열의 다음에 오는 순열을 출력한다. 만약, 사전순으로 마지막에 오는 순열인 경우에는 -1을 출력한다.

예제 입력 1 
4
1 2 3 4
예제 출력 1 
1 2 4 3
예제 입력 2 
5
5 4 3 2 1
예제 출력 2 
-1

입력:
10
8 9 10 7 6 5 4 3 2 1
출력:
8 10 1 2 3 4 5 6 7 9

"""

import sys
input = sys.stdin.readline

# python에서 일반적인 최대값은 2^63-1임!
# python에서 정렬 알고리즘은 timsort로 최선은 n, 최악은 nlogn이다!

def main():
    # 그냥 찾으면 10000!이 되어 버림.
    N = int(input().rstrip("\n")) # 1 <= N <= 10000
    sequence = list(map(int, input().rstrip("\n").split(" ")))
    # 기준치

    # 스왑했을 때 자기보다 큰 수 중 제일 작은 수. # 10000C2까지 줄음. 근데 비교하는게...
    # 만약 스왑했을 때 자기보다 큰수가 없다? => -1

    # 1 3 2 4 6 5
    # 1 6 5 4 3 2 2 있음. 없음. 없음. 없음. 없음. 없음.
    # 2 1 3 4 5 6
    # 3 2 4 1 5 6 
    # 10 9 8 7 6 5 4 3 1 2 뒤에서부터 swap....? 
    # 10 9 8 7 6 5 4 3 2 1 뒤에서부터 swap....? 
                    
    # 뒤에서부터 swap하고, 그리고 바뀐 것이 커지면 그게 답임.

    # 5 "1" 4 3 "2"  # 한 번 커지고, 작아지면.
    # 5 2 4 3 1  # 작아지고 커지고가 될 때 까지 함.
    # 5 2 4 3 1  
                                
    # 답: 5 2 1 3 4
                    
    # 10 9 "7" "8" 6 5 4 3 2 1
    # 10 9 8 7 6 5 4 3 2 1
    # 7 6 5 4 3 2 1 중에서 가장 작은 것 만들면 됨.
    # 바뀐 index 
    last_sequence = True
    key_idx = 0
    swap_idx = 0
    for i in range(N-1, 0, -1): # 내림차순 아닌 곳 찾기 및 swap_idx init.
            if sequence[i] > sequence[i-1]: # 스왑 가능하면.
                last_sequence = False
                key_idx = i-1
                swap_idx = i
                break

    if last_sequence:
        print(-1)
        return

    # swap_idx 재설정.
    for i in range(N-1, key_idx, -1):   # 내림차순 아닌 곳보다 크고, 그 중에 가장 작은 index 구하기.
         if sequence[i] > sequence[key_idx] and sequence[i] < sequence[swap_idx]:
              swap_idx = i
    
    sequence[key_idx], sequence[swap_idx] = sequence[swap_idx], sequence[key_idx]  # 스왑하기.

    # j 전까지는 다 버림. 바뀐 시퀀스.
    sequence_tail = sequence[key_idx+1:]
    sequence_head = sequence[:key_idx+1]

    print(' '.join(map(str, sequence_head + sorted(sequence_tail))))       
                
# 10 7 8 9 4 "5" "6" 3 2 1
# 5 3 2 1
# 1 2 3 5
if __name__ == "__main__":
    main()

"""
반레:
입력:
4
1 3 4 2

출력:
1 4 2 3


243561
132465

1342와
1432를
다른 것으로 봐야함.
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
2 4 3 1
3 1 2 4
3 1 4 2
3 2 1 4
3 2 4 1
3 4 1 2
3 4 2 1
4 1 2 3
4 1 3 2
4 2 1 3
4 2 3 1
4 3 1 2
4 3 2 1


"""
