import itertools
import math
import bisect
import heapq
import collections

# sum()
# max()
# min()
# eval()
# sorted()

# itertools.permutations()
# itertools.combinations()
# itertools.product()
# itertools.combinations_with_replacement()

# heapq 라이브러리
# 힙(Heap) 기능 제공
# 다익스트라 최단 경로 알고리즘을 비롯한 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용
# PriorityQueue 라이브러리도 사용가능하지만, 코딩 테스트 환경에서 보통 heapq가 더 빠르게 동작
# 파이썬의 힙은 최소 힙으로 구성되어 있어서 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
# (보통 최소 힙 자료구조의 최상단 원소는 '가장 작은' 원소이기 때문)
# 힙에 원소를 삽입할 때는 heap.heappush() 메서드를 사용
# 힙에서 원소를 꺼재고자 할 때는 heap.heappop() 메서드를 사용
# 힙으로 만드려면 heapify(x)

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value) # 내림차순 heapsort => -value로 진행하면 됨.

    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1,5,7,3,3,6,9,2,10,64,4,2,154,73])
print(result)

# bisect lib.
# bisect 라이브러리
# 이진 탐색을 쉽게 구현할 수 있도록 해주는 라이브러리
# '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.
# bisect_left()와 bisect_right() 함수가 가장 중요하게 사용되며, 이 두 함수가 동작하는 시간 복잡도는 O(logN)이다.
# bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# 위 두 함수는 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때,
# 효과적으로 사용될 수 있다. 시간복잡도는 O(logN)이다.

# 특정 범위의 데이터 개수를 알고 싶을 때 매우 유용.

# collection lib.
# 유용한 자료구조를 제공하는 표준 라이브러리
# 코딩 테스트에서 유용하게 사용되는 클래스는 deque와 Counter이다.

# deque

# 파이썬에서는 보통 deque를 통해 큐를 구현한다.
# 리스트의 경우 맨 뒤에 원소 추가 및 제거의 시간복잡도는 O(1)이지만, 맨 앞에 원소 추가 및 제거는 O(N)이 걸린다.
# deque의 경우 맨 앞과 뒤 모두 원소를 추가하거나 제거할 때 시간복잡도가 O(1)이다.
# deque는 리스트와 다르게 인덱싱, 슬라이싱 기능은 없지만, 연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적이다.
# deque는 데이터의 맨 앞과 맨 뒤 모두에서 삽입과 삭제가 가능하기 때문에 스택으로도 쓸 수 있고, 큐로도 쓸 수 있다.

# 큐로 사용할 때: popleft()로 맨 앞 원소 제거, append(x)로 맨 뒤에 원소 x 삽입
# 스택으로 사용할 때: pop()로 맨 뒤 원소 제거, append(x)로 맨 뒤에 원소 x 삽입
# 맨 앞에 원소 x 삽입: appendleft(x)

# deque 활용 예시 소스코드

# from collections import deque

# data = deque([2, 3, 4])
# data.appendleft(1)
# data.append(5)

# print(data)
# print(list(data)) # 리스트 자료형으로 변환

# data.popleft()
# data.pop()
# print(list(data))

# counter
# 등장 횟수를 세는 기능 제공
# 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
# 원소별 등장 횟수를 세는 기능이 필요할 떄 짧은 소스코드로 이를 구현할 수 있다.

# Counter 활용 예시 소스코드
# from collections import Counter

# counter = Counter(['red', 'blue', 'red' ,'green', 'blue', 'blue'])
# print(counter['red']) # 'red'가 등장한 횟수 출력
# print(counter['blue']) # 'blue'가 등장한 횟수 출력
# print(dict(counter)) # 딕셔너리형으로 변환

# math 라이브러리

# 자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리
# factorial(n): n!
# sqrt(x): x의 제곱근
# gcd(a, b): a와 b의 최대 공약수
# pi: 상수 파이(pi)
# e: 자연상수 e