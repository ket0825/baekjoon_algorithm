"""
거짓말
시간 제한	메모리 제한
2 초	128 MB
문제
지민이는 파티에 가서 이야기 하는 것을 좋아한다. 파티에 갈 때마다, 지민이는 지민이가 가장 좋아하는 이야기를 한다. 지민이는 그 이야기를 말할 때, 있는 그대로 진실로 말하거나 엄청나게 과장해서 말한다. 당연히 과장해서 이야기하는 것이 훨씬 더 재미있기 때문에, 되도록이면 과장해서 이야기하려고 한다. 하지만, 지민이는 거짓말쟁이로 알려지기는 싫어한다. 문제는 몇몇 사람들은 그 이야기의 진실을 안다는 것이다. 따라서 이런 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기할 수 밖에 없다. 당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다. 지민이는 이런 일을 모두 피해야 한다.

사람의 수 N이 주어진다. 그리고 그 이야기의 진실을 아는 사람이 주어진다. 그리고 각 파티에 오는 사람들의 번호가 주어진다. 지민이는 모든 파티에 참가해야 한다. 이때, 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.

둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다. 진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다. 사람들의 번호는 1부터 N까지의 수로 주어진다.

셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.

N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수는 0 이상 50 이하의 정수, 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.

출력
첫째 줄에 문제의 정답을 출력한다.

예제 입력 1 
4 3
0
2 1 2
1 3
3 2 3 4
예제 출력 1 
3
예제 입력 2 
4 1
1 1
4 1 2 3 4
예제 출력 2 
0
예제 입력 3 
4 1
0
4 1 2 3 4
예제 출력 3 
1
예제 입력 4 
4 5
1 1
1 1
1 2
1 3
1 4
2 4 1
예제 출력 4 
2
예제 입력 5 
10 9
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9
1 10
2 3 10
1 4
예제 출력 5 
4
예제 입력 6 
8 5
3 1 2 7
2 3 4
1 5
2 5 6
2 6 8
1 8
예제 출력 6 
5
예제 입력 7 
3 4
1 3
1 1
1 2
2 1 2
3 1 2 3
예제 출력 7 
0
"""

# import sys
# sys.setrecursionlimit(10000000)
# input = sys.stdin.readline

# def check_party(party, visited_party, checked_person, can_lie):
#     visited_party[party] = True
#     lie_flag = True
#     print(f"현재 party: {party}")
#     for person in party_list[party]:
#         print(f"현재 person: {person}")
#         if person in know:
#             print(f"아는 사람: {person}")
#             lie_flag = False
            
#         if not checked_person[person]:
#             print(f"person 체크 완료: {person}")
#             checked_person[person] = True
#             lie_flag = check_people(person, visited_party, checked_person, can_lie)
#             # checked_person[person] = False
    
#     return lie_flag

# def check_people(person, visited_party, checked_person, can_lie):
#     result = True
#     for party in people_joined[person]:
#         if not visited_party[party]:
#             result = check_party(party, visited_party, checked_person, can_lie)
#             can_lie[party] = result
    
#     return result
        

# if __name__ == '__main__':
#     N, M = map(int, input().strip().split())
#     input1 = list(map(int, input().strip().split()))
#     if len(input1) == 1:
#         know = set()
#     else:
#         know = set(input1[1:])
#     party_list = [[] for _ in range(M+1)]
#     people_joined = [[] for _ in range(N+1)]
    
#     for p in range(1,M+1):
#         input2 = list(map(int, input().strip().split()))
#         for i in input2[1:]:
#             party_list[p].append(i)
#             people_joined[i].append(p)
    
#     print(f"party_list: {party_list}")
#     print(f"people_joined: {people_joined}")
#     # 파티 가고, 사람 리스트 확인하고, ...
#     visited_party = [False] * (M+1)
#     checked_person = [False] * (N+1)
#     can_lie = [True] * (M+1)
#     can_lie[0] = False
    
#     for i in range(1, M+1):
#         if not visited_party[i]:
#             print(f"현재 확인 파티: {i}")
#             result = check_party(i, visited_party, checked_person, can_lie)
#             can_lie[i] = result
    
#     print(sum(can_lie))


    
# 1.        
# 참고: union path compression 알고리즘
# https://seongonion.tistory.com/131
# import sys
# input = sys.stdin.readline

# def find(parent, x):
#     print("parent:", parent)
#     if x != parent[x]:
#         parent[x] = find(parent, parent[x]) # 같을 때까지 find하면서 compression
    
#     return parent[x]

# # 사실을 아는 사람과 Union시, 해당 사람이 부모노드 되도록
# def union(parent, a, b, know_truth):
#     a = find(parent, a) # 아는 사람이 부모노드인지 확인
#     b = find(parent, b) # 아는 사람이 부모노드인지 확인
    
#     if a in know_truth and b in know_truth:
#         return
    
#     if a in know_truth:
#         parent[b] = a
#     elif b in know_truth:
#         parent[a] = b
#     else: # 모두 없으면 그냥 압축
#         if a < b:
#             parent[b] = a
#         else:
#             parent[a] = b 
            
# if __name__ == '__main__':
#     N, M = map(int, input().split())
#     know_truth = list(map(int, input().split()))[1:]
    
#     parties = []
#     parent = list(range(N+1))
    
#     for _ in range(M):
#         party_info = list(map(int, input().split()))
#         party_len = party_info[0]
#         party = party_info[1:]
        
#         for i in range(party_len-1):
#             union(parent, party[i], party[i+1], know_truth)
        
#         parties.append(party)
    
#     ans = 0
#     for party in parties:
#         can_lie = True
#         for i in range(len(party)):
#             if find(parent, party[i]) in know_truth:
#                 can_lie = False
#                 break
#         if can_lie:
#             ans+=1
    
#     print(ans)

# 2. 집합 연산으로 아는 사람 집합 확장.
import sys
input = sys.stdin.readline

def sol(M, parties, know_truth):
    # 아는 사람 집합 확장.
    change = True
    while change:
        change = False
        for i in range(1,M+1):
            if parties[i] & know_truth: # 교집합
                diff = parties[i] - know_truth # 차집합
                if diff:
                    know_truth |= diff # 합집합을 다시 assign
                    change = True
    
    answer = M
    for i in range(1, M+1):
        if parties[i] & know_truth:
            answer-=1
            
    print(answer)
                            

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    know_truth = set(list(map(int, input().strip().split()))[1:])
    parties = [set() for _ in range(M+1)]
    for i in range(1, M+1):
        party = set(list(map(int, input().strip().split()))[1:])
        parties[i] |= party
    
    sol(M, parties, know_truth)

    
        