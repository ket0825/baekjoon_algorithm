import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip().split(" "))
    sorted_list = sorted(list(map(int, input().rstrip().split(" "))))

    answer = []

    def cartesian_product():
        if len(answer) == M:
            print(*answer)
            return
        
        for i in sorted_list:
            answer.append(i)
            cartesian_product()
            answer.pop()
    
    cartesian_product()


if __name__ == '__main__':
    main()