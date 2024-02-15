"""
암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 
최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고
알려져 있다. 
또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 
암호를 이루는 알파벳이 암호에서
즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.
(정렬)
새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 
C가지가 있다고 한다. 이 알파벳을 입수한 민식, 영식 형제는 
조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. 
C개의 문자들이 모두 주어졌을 때, 
가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

입력
첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

출력
각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

예제 입력 1 
4 6
a t c i s w
예제 출력 1 
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw

"""

## 1. comb 모듈 사용
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# def main():
#     L, C = map(int,input().rstrip("\n").split(" "))
#     C_items = sorted(set(input().rstrip("\n").split(" ")))
    
#     vowel_char_tuple = ("a", "e", "i", "o", "u")
    
#     for combo in combinations(C_items, L):
#         one_vowel = False
#         consonant_count = 0
#         for elem in combo:
#             if elem in vowel_char_tuple:
#                 one_vowel = True
#             else:
#                 consonant_count+=1

#             if one_vowel and consonant_count == 2:
#                 print(''.join(combo))
#                 break

# if __name__ == "__main__":
#     main() 

## 2. 자체적으로 recursion으로 걸러내면서 진행.
# import sys
# input = sys.stdin.readline

# def main():
#     L, C = map(int,input().rstrip("\n").split(" "))
#     C_items = sorted(input().rstrip("\n").split(" "))
#     visited = [0]*C
#     vowel_char_tuple = ("a", "e", "i", "o", "u")
    
#     def dfs(stack:list, base:int, vowel_counts:int, consonant_counts: int):
#         if len(stack) == L and vowel_counts >= 1 and consonant_counts >= 2:
#             print(''.join(stack))
#             return
#         elif len(stack) == L:
#             return

#         items = C_items[base:]
        
#         for i in items:
#             # if "".join(stack) == "acs":
#             #     print("here")
#             # print(C_items[base:], "stack:", stack)
#             if i not in stack:
#                 stack.append(i)
#                 if i in vowel_char_tuple:
#                     visited[base] = 1
#                     dfs(stack, base+1, vowel_counts+1, consonant_counts)
#                     visited[base] = 0
#                     stack.pop()
#                     # vowel_counts-=1
#                 else:
#                     visited[base] = 1
#                     dfs(stack, base+1, vowel_counts, consonant_counts+1)
#                     visited[base] = 0
#                     stack.pop()
#                     # consonant_counts-=1
#             base+=1
    

#     dfs([], 0, 0, 0)

# if __name__ == "__main__":
#     main() 

## 3. # 모음 개수에 따라 계속 나오게끔 하는거임. 모음 1개: 자음 l-1개처럼 반복.
# import sys
# input = sys.stdin.readline

# l, c = map(int, input().split())
# words = list(input().split())
# vowel = []
# consonant = []
# for w in words:
#   if w in ['a', 'e', 'i', 'o', 'u']:
#     vowel.append(w)
#   else:
#     consonant.append(w)
# vowel.sort()
# consonant.sort()
# vn = range(1, l-1)
# cn = range(l-1, 1, -1)
# combi = {}

# def findCombi(current, count, n, total, vFlag):
#   if count == n:
#     if vFlag:
#       combi[n]['v'].append(current)
#     else:
#       combi[l - n]['c'].append(current)
#   else:
#     for i in range(total):
#       if not current or current[len(current) - 1] < i:
#         newC = current[:]
#         newC.append(i)
#         findCombi(newC, count + 1, n, total, vFlag)

# for i in vn: # 모음 개수에 따라 계속 나오게끔 하는거임. 모음 1개: 자음 l-1개 등.
#   combi[i] = {}
#   combi[i]['v'] = []
#   combi[i]['c'] = []
#   findCombi([], 0, i, len(vowel), True)
#   findCombi([], 0, l-i, len(consonant), False)
# # 모음 아예 없는 경우는 vn이 0임.
# # 자음 2개 이상 없는 경우는 어떻게 되는지...
# answer = []
# for i in vn:
#   for vcombi in combi[i]['v']:
#     st = []
#     for v in vcombi:
#       st.append(vowel[v])
#     for ccombi in combi[i]['c']:
#       nst = st[:]
#       for c in ccombi:
#         nst.append(consonant[c])
#       nst.sort()
#       answer.append(''.join(nst))
# answer.sort()
# for a in answer:
#   print(a)

## 4. 매우 빠르게 진행됨. parameter 최소화. 
# 그리고 pop 대신 backtracking을 두 번 함.
# L, C = map(int, input().split())  # L: 암호 길이, C: 알파벳 개수

# alphabets = list(input().split())  # 알파벳 리스트
# alphabets.sort()

# vowels = ["a", "e", "i", "o", "u"]

# if L == C:
#     print("".join(alphabets))

# else:

#     def backtracking(idx, password):
#         if len(password) == L:
#             vowel_cnt = 0
#             cons_cnt = 0

#             for elem in password:
#                 if elem in vowels:
#                     vowel_cnt += 1
#                 else:
#                     cons_cnt += 1

#             if vowel_cnt >= 1 and cons_cnt >= 2:
#                 print(password)
#                 return

#         if idx >= len(alphabets):
#             return
#         backtracking(idx + 1, password + alphabets[idx])
#         backtracking(idx + 1, password)

#     backtracking(0, "")