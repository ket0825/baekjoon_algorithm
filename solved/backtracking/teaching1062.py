"""
가르침
시간 제한	메모리 제한
1 초	128 MB
문제
남극에 사는 김지민 선생님은 학생들이 되도록이면 많은 단어를 읽을 수 있도록 하려고 한다. 그러나 지구온난화로 인해 얼음이 녹아서 곧 학교가 무너지기 때문에, 김지민은 K개의 글자를 가르칠 시간 밖에 없다. 김지민이 가르치고 난 후에는, 학생들은 그 K개의 글자로만 이루어진 단어만을 읽을 수 있다. 김지민은 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대가 되는지 고민에 빠졌다.

남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다. 남극언어에 단어는 N개 밖에 없다고 가정한다. 학생들이 읽을 수 있는 단어의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N과 K가 주어진다. N은 50보다 작거나 같은 자연수이고, K는 26보다 작거나 같은 자연수 또는 0이다. 둘째 줄부터 N개의 줄에 남극 언어의 단어가 주어진다. 단어는 영어 소문자로만 이루어져 있고, 길이가 8보다 크거나 같고, 15보다 작거나 같다. 모든 단어는 중복되지 않는다.

출력
첫째 줄에 김지민이 K개의 글자를 가르칠 때, 학생들이 읽을 수 있는 단어 개수의 최댓값을 출력한다.

예제 입력 1 
3 6
antarctica
antahellotica
antacartica
예제 출력 1 
2
예제 입력 2 
2 3
antaxxxxxxxtica
antarctica
예제 출력 2 
0
예제 입력 3 
9 8
antabtica
antaxtica
antadtica
antaetica
antaftica
antagtica
antahtica
antajtica
antaktica
예제 출력 3 
3

"""
# 알파벳 하나씩 넣고, 빼는 식? (K는 최대 26개)
# a, c, i ,n, t는 반드시 필요. 그럼 21C(K-5) -> 352716. 그리고 단어 N개라면 시간 초과 가능성...
# 각 단어별로 부족한 글자를 알면, 그것 중 공통 갯수가 많은 순서 -> 그럼 완성 못할수도 있음.
# 단어 길이는 anta tica 빼면 최대 7개...

import sys
from itertools import combinations

input = sys.stdin.readline

def sol(N, K, words_set):
    if K < 5:
        print(0)
        return

    teach_set = set(['a','i','c','t','n'])
    to_teach = ['b','d','e','f','g','h','j', 'k','l','m','o','p','q','r','s','u','v','w','x','y','z']
    max_know = 0
    for comb in combinations(to_teach, K-5): # 21K10 -> 352716
        know_set = set(comb).union(teach_set)        
        cnt = 0
        for word_set in words_set:
            if know_set.issuperset(word_set):
                cnt+=1
        max_know = max(max_know, cnt)
    
    print(max_know)    
    


def sol2(N, K, words_set):
    if K < 5:
        print(0)
        return
    
    teach_set = set(['a','c','i','n','t'])
    to_teach = [chr(i) for i in range(97, 123) if chr(i) not in teach_set]
    answers = [False] * (N+1)
    def dfs(start, length):
        if length == K:
            cnt = 0
            for word_set in words_set:                
                if not word_set.difference(teach_set):
                    cnt+=1
            answers[cnt] = True
            return          
                    
        for i in range(start, 21):                    
            teach_set.add(to_teach[i])
            dfs(i+1, length+1)                
            teach_set.remove(to_teach[i])                
    
    dfs(0, 5)
    
    for i in range(N, -1, -1):
        if answers[i]:
            print(i)
            break
    
if __name__ == '__main__':
    N, K = map(int, input().strip().split())    
    words_set = [set(input().strip()) for _ in range(N)]
    sol2(N, K, words_set)
    # N, K = 50, 15
    # words_set = []
    # for _ in range(N):
    #     words_set.append(set('anta'+"".join(['b','d','e','f','g','h','j', 'k','l','m','o','p','q','r','s','u','v','w','x','y','z'])+'tica'))    
    # sol(N, K, words_set)

