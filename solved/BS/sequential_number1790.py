"""
N: 1부터 N까지 숫자. 1...100,000,000
k: 앞에서 k번째 자리 숫자의 자릿수 1...1,000,000,000
만약 수의 길이가 k보다 작으면 -1.
입력: 
N k
출력:
a




"""
import sys
input = sys.stdin.readline

def sol():
    N, K = map(int,input().split())
    
    digit = len(str(N)) # 자릿수 길이.
    total_moved = 0
    ans = 0
    low = 0
    high = digit
    
    def get_prev_length(digit):
        if digit == 0:
            return 0
        return int(10**(digit-1) - 10**(digit-2)) * (digit-1) + get_prev_length(digit - 1)
    
    total_length = get_prev_length(digit) + (N - int(10**(digit-1)) + 1)*digit
    
    if total_length < K:
        print(-1)
        return 
        
    for i in range(1, digit+1):
        this_count = int((10**(i) - 10**(i-1))*i) # 9*1 , 90 * 2, 900 * 3
        if K - total_moved - this_count <= 0:
            low = i - 1
            high = i
            break
        else:
            total_moved += this_count
  
    residual_length = K - total_moved                
    # 10**low <= x < 10**high 범위에 존재.    
    move = (residual_length - 1) // (low+1)  # 이러면 0칸 움직이는 것은 본인이라고 할 수 있음.    
    start_num = int(10**low) + move
    move_in_num = (residual_length - 1) % (low+1)
    ans = str(start_num)[move_in_num]
    print(ans)
    
sol()

# 출처 1: 최대 가능한 자릿수를 구하는 것이 아니라 그냥 K에 따른 필요한 자릿수를 찾음. 깔끔하고 좋은 풀이. 출처: taetaehyeon
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 수 이어 쓰기 2 (1790)
 1. 1부터 N까지의 수를 이어서 씀
 2. 앞에서 k번째 자리 숫자가 어떤 숫자인지 구하기
[입력]
 1. N, k
[출력]
 1. k번째 자리 숫자 출력, 수의 길이가 k보다 작아서 k번째 자리 숫자가 없는 경우는 -1 출력
"""

"""
<풀이>
 1. 
- 1의 자리: 1 ~ 9 [9개]
- 2의 자리: 10 ~ 99 [90개]
- 3의 자리: 100 ~ 999 [900개]
"""

N, k = map(int, input().split())

# 현재 자릿수와 그 수의 개수, 마지막 수
digit = 1
digit_cnt = 9
last = 0

# 남은 자릿수가 현재 자릿수의 개수보다 크다면
while k > digit * digit_cnt:

    # k 값 및 마지막 수 조정
    k -= digit * digit_cnt
    last += digit_cnt

    # 자릿수 이동
    digit += 1
    digit_cnt *= 10

# k번째 자리에 사용되는 숫자 찾기 (자릿수 맞추기) + (현재 수가 몇 번째 인지 조정)
number = (last + 1) + ((k - 1) // digit)

# k번째 자리에 사용되는 숫자가 N보다 작거나 같다면
if number <= N:
    # k번째 자리 숫자 출력
    print(str(number)[(k - 1) % digit])
# k번째 자리 숫자가 없는 경우 -1 출력
else:
    print(-1)