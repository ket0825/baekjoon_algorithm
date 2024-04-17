
## 1. 계산해본 결과, 브루트 포스로 1000만까지 하면 모든 케이스 만족가능.
import sys
input = sys.stdin.readline


def main():
    N = int(input().rstrip())
    count = 0
    num_666 = 0 
 
    for i in range(10**7):
        str_num = str(i)    
        if str_num.find('666') > -1: # in 연산이 더 빠르더라..
            count+=1
        
        if count == N:
            num_666 = i
            break
    
    print(num_666)


if __name__ == '__main__':
    main()

## 2. 공식 이용. 출처: tobey2j0
# n=[]
# for m in range(3):
#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 n.append(1000000*m+100000*i+10000*j+1000*k+666)
#                 n.append(1000000*m+100000*i+10000*j+6660+k)
#                 n.append(1000000*m+100000*i+66600+10*j+k)
#                 n.append(1000000*m+666000+100*i+10*j+k)
# for m in range(3):
#     for i in range(10):
#         for j in range(10):
#             n.remove(1000000*m+100000*i+10000*j+6666)
#             n.remove(1000000*m+100000*i+66660+j)
#             n.remove(1000000*m+666600+10*i+j)
# n.sort()
# print(n[int(input())-1])

# 자릿수 로직.
# for i in range(10**7):        
#     num = i
#     consecutive_six_count = 0

#     digit = len(str(i))

#     while consecutive_six_count < 3 and digit != 0:
#         denominator = 10**(digit-1)
#         quotient, remainder = num // denominator, num % denominator

#         if quotient == 6:
#             consecutive_six_count +=1
#         else:
#             consecutive_six_count = 0
        
#         num = remainder
#         digit-=1   
    
#     if consecutive_six_count == 3:
#         count+=1
    
#     if count == N:
#         num_666 = i
#         break
# print(count)
# print(num_666)  