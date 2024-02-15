import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().rstrip("\n").split(" "))

    def cartesian_product(arr):
        if len(arr) == M:
            print(*arr)
            return
        
        for i in range(1, N+1):
            arr.append(i)
            cartesian_product(arr)
            arr.pop()
    
    cartesian_product([])

if __name__ == "__main__":
    main()