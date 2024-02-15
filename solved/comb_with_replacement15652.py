import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip("\n").split(" "))

    def comb_with_replacement(arr, depth):
        if len(arr) == M:
            print(' '.join(map(str, arr)))
            return
        
        for i in range(depth, N+1):
            arr.append(i)
            comb_with_replacement(arr, i)
            arr.pop()
    
    comb_with_replacement([],1)

if __name__ == "__main__":
    main()