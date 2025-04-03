"""
강의실
시간 제한	메모리 제한
2 초	128 MB
문제
N개의 강의가 있다. 우리는 모든 강의의 시작하는 시간과 끝나는 시간을 알고 있다. 이때, 우리는 최대한 적은 수의 강의실을 사용하여 모든 강의가 이루어지게 하고 싶다.

물론, 한 강의실에서는 동시에 2개 이상의 강의를 진행할 수 없고, 한 강의의 종료시간과 다른 강의의 시작시간이 겹치는 것은 상관없다. 필요한 최소 강의실의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 강의의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 줄마다 세 개의 정수가 주어지는데, 순서대로 강의 번호, 강의 시작 시간, 강의 종료 시간을 의미한다. 강의 번호는 1부터 N까지 붙어 있으며, 입력에서 꼭 순서대로 주어지지 않을 수 있으나 한 번씩만 주어진다. 강의 시작 시간과 강의 종료 시간은 0 이상 10억 이하의 정수이고, 시작 시간은 종료 시간보다 작다.

출력
첫째 줄에 필요한 최소 강의실 개수를 출력한다.

예제 입력 1 
8
6 15 21
7 20 25
1 3 8
3 2 14
8 6 27
2 7 13
4 12 18
5 6 20
예제 출력 1 
5
"""

import sys
import heapq
input = sys.stdin.readline


def sol():
    N = int(input().strip()) # 1...10만.
    lectures = [
        list(map(int, input().strip().split())) for _ in range(N)
    ]
    
    lectures.sort(key=lambda x: x[1]) # 1. 시작 시간 빠를수록.        
    # 2 - 14
    # 3 - 8
    # 6 - 20
    # 6 - 27
    # 7 - 13
    # 12 - 18
    # 15 - 21
    # 20 - 25    
    rooms = [] # 종료 시간만 저장. minheap
    
    for lecture in lectures:
        if rooms and lecture[1] >= rooms[0]: # room의 minheap의 강의시간이 제일 작으면 거기에 추가.
            heapq.heappop(rooms) # 추가하기 위해 끝나는 시간 pop.
        heapq.heappush(rooms, lecture[2]) # 끝나는 시간 추가.
    
    # 강의실 최소 개수
    print(len(rooms))

if __name__ == '__main__':
    sol()
    
# 시작 시간 기준 정렬.
# 1 - 2
# 2 - 15
# 2 - 14
# 2 - 7
# 3 - 5
...
# 강의실 추가? 어떻게..? 힙에 노드 추가?
# 15
# 14
#
# 그리디 알고리즘. N**2 풀이...
# def sol():
#     N = int(input().strip()) # 1...10만.
#     lectures = [
#         list(map(int, input().strip().split())) for _ in range(N)
#     ] # 시작과 종료는 0이상 10억이하 정수...
#     # list에 기록하면서는 불가능.
#     # 1. 강의실을 만들어나가면서 기입하기.
#     # 15-21, 2-14, 
#     # 20-25, 6-20
#     # 6-27,
#     # 7-13, 
#     # 12-18, 3-8
#     # 그런데 이게, 어떤 강의실에 배치하는지에 따라 달라질 것 같은데?
    
#     # 일단 sorting 가능. 긴 소요시간 순.
#     # 6-27
#     # 6-20 
#     # 2 14  
#     # 7-13 15-21
#     # 12-18 20-25
#     lectures.sort(key=lambda x: (x[2]-x[1], x[1]), reverse=True) # 1. 길이, 2. 시작 시간 늦을수록.        
#     rooms = [
#                 [ # 방
#                     (0,0) # 시간표
#                 ] 
#         ]
#     # 6 - 27
#     # 6 - 20
#     # 2 - 14  15 - 21
#     # 7 - 13  20 - 25
#     # 12 - 18
#     # 이렇게 하면 높이가 강의실 최소 수임.    
#     for lecture in lectures:
#         # print(f"강의: {lecture}")
#         need_room = True
#         for room in rooms:
#             append_time = True
#             for time in room:                
#                 # time의 마지막이 강의의 처음보다 작거나 같아야 함,
#                 # time의 처음이 강의의 마지막보다 크거나 같아야 함.
#                 # 이것이 모두 충족하면 그 room에 배치
#                 # 아니면 room 추가
#                 if ( 
#                     time[1] <= lecture[1] # time의 마지막이 강의의 처음보다 작거나 같아야 함,
#                     or time[0] >= lecture[2] # time의 처음이 강의의 마지막보다 크거나 같아야 함.
#                     ):
#                     continue
#                 else:
#                     append_time = False
#                     break
                            
#             if append_time:
#                 room.append((lecture[1], lecture[2]))
#                 need_room = False
#                 break
                                
#         if need_room:
#             rooms.append([(lecture[1], lecture[2])])        
#         # print(rooms)
            
    
#     # print(rooms)
#     print(len(rooms))