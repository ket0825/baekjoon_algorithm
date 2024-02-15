import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip("\n").split(" "))
    sorted_list = sorted(list(map(int, input().rstrip("\n").split(" "))))

    answer = []

    def comb_with_replacement(start):
        if len(answer) == M:
            print(*answer)
            return
        
        for elem in sorted_list[start:]:
            answer.append(elem)
            comb_with_replacement(start)
            answer.pop()
            start+=1
            
    comb_with_replacement(0)
      

if __name__ == "__main__":
    main()