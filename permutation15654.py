"""
N개의 list, M개를 고르는 것. N개의 item이 주어짐. 중복 불가능.
"""
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().rstrip("\n").split(" "))
    sorted_lst = sorted(list(map(int, input().rstrip("\n").split(" "))))
 
    def selected_permutation(arr):
        if len(arr) == M:
            print(*arr)
            return
        
        for elem in sorted_lst:
            if elem not in arr:
                arr.append(elem)
                selected_permutation(arr)
                arr.pop()
    
    selected_permutation([])


if __name__ == "__main__":
    main()