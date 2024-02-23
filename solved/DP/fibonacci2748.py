import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip("\n")) # n은 90보다 작거나 같은 자연수.
    dp = [0]*91
    dp[0] = 0
    dp[1] = 1
    if n > 2:
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

    print(dp[n])


if __name__ == "__main__":
    main()



    




