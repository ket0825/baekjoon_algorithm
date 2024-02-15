# # 순열 구현하기.
# import sys
# """
# 먼저 사용자가 원하는 arr 과 r 을 받는다. 그리고 arr 을 오름차순 정렬하는데 여기서는 큰 의미가 있지는 않고 단순히 출력을 이쁘게 하기 위해서이다. 그리고 used 변수를 만드는데, 이 변수는 i 번째 값을 썼는지 저장하는 데 쓰인다. 우리는 모든 순열을 하나씩 만들고 출력하는데 당연히 중복값은 저장되어서는 안 된다.
# 실제 순열을 만들 generate 함수를 생성한다. 먼저 chosen 변수는 순열의 원소를 저장되는 변수인데 이 배열에 값을 하나씩 추가하다가 그 개수가 r 이 되는 순간 하나의 순열이 만들어진 것이므로 출력 후 종료한다.
# 이 함수의 핵심이다. 모든 순열은 arr 의 0부터 i-1 번째 값으로 시작하기에 for 문으로 다 만들어야 한다. 그리고 chosen 에 값 추가 후, used 에 해당 변수를 사용했다고 체크한다. 그 다음 다시 generate 를 반복한다. 하나가 만들어진 후에는 그 값을 uncheck해줘야 한다.
# """

# def permutation(arr, r):
#     arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]

#     def generate(chosen, used):
#         if len(chosen) == r:
#             print(' '.join(map(str, chosen)))
#             return
        
#         for i in range(len(arr)):
#             if not used[i]:
#                 chosen.append(arr[i])
#                 used[i] = 1
#                 generate(chosen, used)
#                 used[i] = 0
#                 chosen.pop()

#     generate([], used)


# def main():
#     """
#     1   <=  M   <=  N   <=8
#     """

#     input = sys.stdin.readline
#     N, M = map(int, input().rstrip("\n").split(" "))
#     arr = list(range(1, N+1))

#     permutation(arr, M)
    
#     # """
#     # M == 1:
#     # for n in range(1, N+1):
#     #         print(n) 
#     # """

#     # """
#     # M == 2:
#     # for _ in range(M): # M번 뽑기.
#     #     for a in range(1, N+1): 1, 2, 3
#     #         for b in range(1, N+1) 1, 2, 3
#     #             print(n) 
#     # """
#     # for a in range(1, N+1): #1, 2, 3
#     #     for b in range(1, N+1): #1, 2, 3
#     #         if a != b:
#     #             print(a, b) 

#     # for _ in range(M): # M번 for를 진행하기. 뽑기.
#     #     for a in range(1, N+1):
#     #         for b in range(1, N+1):
#     #             for c in range(1, N+1):
#     #                 print(a) 

        
# if __name__ == "__main__":
#     main()


# import sys

# input = sys.stdin.readline

# def main():
#     N, M = map(int, input().rstrip().split(" "))

#     visited = [0 for _ in range(N)]
#     permutation_set = list(range(1, N+1))

#     permu_item = []

#     def dfs(permu_item, visited):
#         if len(permu_item) == M:
#             print(' '.join(map(str, permu_item)))
#             return
        
#         for idx, i in enumerate(permutation_set):
#             if not visited[idx]:
#                 permu_item.append(i)
#                 visited[idx] = 1
#                 dfs(permu_item, visited)
#                 visited[idx] = 0
#                 permu_item.pop()
    
#     dfs(permu_item,visited)
        

# if __name__ == "__main__":
#     main()


import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip().split(" "))

    def dfs(permu_item):
        if len(permu_item) == M:
            print(' '.join(map(str, permu_item)))
            return
        
        for i in range(1, N+1):
            if i not in permu_item:
                dfs(permu_item + [i])

        return
    
    dfs([])
        

if __name__ == "__main__":
    main()