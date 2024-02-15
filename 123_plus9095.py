"""
1, 2, 3 더하기 문제는 점화식이 성립한다.
f(n) = f(n-1) + f(n-2) + f(n-3)
"""

import sys
input = sys.stdin.readline
case_set = set()

def main():
    T = int(input())
    n_list = [int(input()) for _ in range(T)]   # 각 elem은 11보다 작음.
    
    def supergrouping(num_list:tuple[int]): 
        case_set.add(num_list)
        prev = 0
        for idx, i in enumerate(num_list):
            if idx == 0:
                prev = i
                continue
            
            if prev + i > 3:
                return
            
            next_num_list = list(num_list).copy()
            next_num_list[idx-1] = next_num_list.pop(idx-1) + next_num_list[idx-1]
            next_num_list = tuple(next_num_list)

            supergrouping(next_num_list)
            prev = i

    for elem in n_list:
        supergrouping(tuple(1 for _ in range(elem)))
        print(len(case_set))
        case_set.clear()

if __name__ == "__main__":
    main()


## 2. 점화식 공식을 이용한 풀이.

# import sys
# input = sys.stdin.readline
# case_set = set()

# def main():
#     T = int(input())
#     n_list = [int(input()) for _ in range(T)]   # 각 elem은 11보다 작음.

#     dp = [0] * 11
#     dp[1] = 1
#     dp[2] = 2
#     dp[3] = 4

#     for i in range(4, 11):
#         dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

#     for n in n_list:
#         print(dp[n])

# if __name__ == "__main__":
#     main()