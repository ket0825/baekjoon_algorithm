# def main():          
#     # 채널 N: 0~500000
#     # 고장난 버튼 개수 M: 0~10, 존재하면 3번째 줄에는 고장난 버튼 숫자 존재.
#     # 초기채널 100
#     # +버튼, -버튼 존재.

#     input1 = input() # channel number
#     input2 = input() # broken button num
#     if input2 != '0':
#         input3 = input() # broken buttons
#         available_button = [str(i) for i in range(10) if str(i) not in input3]

#     button_pressed = 0
#     cur_channel = 100
#     goal_channel = int(input1) # input

#     # Edge cases.
#     if goal_channel == 100:
#         print(button_pressed)
#         return None
    
#     elif input2 == "0":
#         button_pressed = min(len(str(goal_channel)), abs(goal_channel - cur_channel)) # +1, -1만으로 더 빨리 끝낼 수 있는지.
#         print(button_pressed)
#         return None
    
#     elif input2 == "10":
#         button_pressed = abs(goal_channel - cur_channel)
#         print(button_pressed)
#         return None

#     digits = [i for i in input1]
#     digit_num = len(digits)

#     # min이면 다음 자리는 max가 되는 걸로.
#     # max면 다음 자리는 min이 되는 걸로.
#     # same이면 다음 자리는 가장 차이가 작은 걸로.
#     # 5212

#     # 5 1 안돼.
#     # 4 or 6 (두 가지 분기) => 차이가 2가지로 나뉨.
#     # 만약 4면, 앞으로는 계속 max로.  # recursive 안되나...
#     # 4면, 다음 자리는 max인 9로.
#     # 만약 6이면, 앞으로는 계속 min으로
    

#     # 0. 있는지 없는지 확인.
#     # 0.1 있으면 다음 거 확인.

#     # 0.2 없으면 절댓값 제일 작은 수 확인.
#     # 0.2.1 만약 1개면 그게 min인지 max인지 확인.
#     # 0.2.2 만약 2개면 후보군 2개가 나오고, 각자 그것에 따라 min일지 max일지 확인하면 됨.

#     # 단, flag는 단 한번이기에 크게 어렵진 않을듯.
#     min_max_same_flag = 'same'   # min, max, same.
#     first_nearest_channel = ''
#     second_nearest_channel = ''

#     for digit in digits:
#         if (digit in available_button 
#             and min_max_same_flag == 'same'
#             ):
#             first_nearest_channel += digit
#             continue
        
#         if min_max_same_flag == 'same':
#             prev_abs = 10 # 충분히 큼.
#             prev_val = ''
#             for button in available_button:
#                 cur_abs = abs(int(button) - int(digit))
#                 if prev_abs == cur_abs:
#                     # 2가지 경우, prev_val라면 max로 쭉 달림.
#                     min_max_same_flag = 'max'
#                     second_nearest_channel = first_nearest_channel + button
#                     first_nearest_channel += prev_val
#                     break
#                 elif prev_abs < cur_abs:
#                     if int(button) > int(digit):
#                         min_max_same_flag = 'min'
#                     elif int(button) < int(digit):
#                         min_max_same_flag = 'max'
#                     break
#                 else:                    
#                     prev_abs = cur_abs
#                     prev_val = button
#             # 단조 감소 케이스 필요.
#             if min_max_same_flag == 'same':
#                 min_max_same_flag = 'max'

#         if min_max_same_flag == 'max':
#              first_nearest_channel += max(available_button)
#         elif min_max_same_flag == 'min':
#              first_nearest_channel += min(available_button)

#     if (second_nearest_channel 
#         and len(second_nearest_channel) < len(digits)
#         ):
#         second_nearest_channel_digits = digits[len(second_nearest_channel):]
#         for digit in second_nearest_channel_digits:
#             second_nearest_channel += min(available_button)
    
#     nearest_value = 0
#     if second_nearest_channel:
#         nearest_value = min(abs(goal_channel - int(first_nearest_channel)), abs(goal_channel - int(second_nearest_channel)))
#     else:
#         nearest_value = abs(goal_channel - int(first_nearest_channel))

#     button_pressed = min(len(digits) + nearest_value, abs(goal_channel - cur_channel))
#     print(button_pressed)

# if __name__ == '__main__':
#     main()

# benchmark:
# 메모리 시간 언어 코드 길이 제출한 시간
# 목표:
# 31120	360	Python 3 510	
# 내 기록:
# 110668 1288 PyPy3 7560	

def main():          
    input1 = input()
    input2 = input()
    if input2 != '0':
        input3 = input()
        available_button = [str(i) for i in range(10) if str(i) not in input3]
    
    button_pressed = 0
    cur_channel = 100
    goal_channel = int(input1)

    if goal_channel == 100:
        print(button_pressed)
        return None   
    elif input2 == "0":
        button_pressed = min(len(str(goal_channel)), abs(goal_channel - cur_channel))
        print(button_pressed)
        return None   
    elif input2 == "10":
        button_pressed = abs(goal_channel - cur_channel)
        print(button_pressed)
        return None
    
    digits = [i for i in input1]

    min_max_same_flag = 'same'
    first_nearest_channel = ''
    second_nearest_channel = ''
    non_zero_available_button = [button for button in available_button if button != '0']

    for idx, digit in enumerate(digits):
        if (digit in available_button 
            and min_max_same_flag == 'same'
            ):
            first_nearest_channel += digit
            continue

        elif min_max_same_flag == 'same':
            prev_abs = 10
            prev_val = ''
            for button in available_button:
                cur_abs = abs(int(button) - int(digit))
                if prev_abs == cur_abs:
                    min_max_same_flag = 'max'
                    second_nearest_channel = first_nearest_channel + button
                    first_nearest_channel += prev_val
                    break
                elif prev_abs < cur_abs:
                    if int(prev_val) > int(digit):
                        first_nearest_channel += prev_val
                        min_max_same_flag = 'min'
                    elif int(prev_val) < int(digit):
                        first_nearest_channel += prev_val
                        min_max_same_flag = 'max'
                    break
                else:                    
                    prev_abs = cur_abs
                    prev_val = button
            
            # available_button len이 1인 경우.
            if min_max_same_flag == 'same':
                min_max_same_flag = 'max'
                first_nearest_channel += max(available_button)

        elif min_max_same_flag == 'max':
             first_nearest_channel += max(available_button)
        elif min_max_same_flag == 'min':
             first_nearest_channel += min(available_button)

    if (second_nearest_channel 
        and len(second_nearest_channel) < len(digits)   # 5455 # 54578
        ):
        second_nearest_channel_digits = digits[len(second_nearest_channel):]
        for digit in second_nearest_channel_digits:
            second_nearest_channel += min(available_button)

    if not second_nearest_channel:
        second_nearest_channel = '1000000'

    non_zero_available_button = [button for button in available_button if button != '0'] 
    next_digit_channel = ''
    prev_digit_channel = ''
    if non_zero_available_button:
        for i in range(len(digits)+1):
            if i == 0:
                nonzero_min_value = min(non_zero_available_button)
                next_digit_channel += nonzero_min_value
            else:
                min_value = min(available_button)
                next_digit_channel += min_value

        if len(digits) - 1 > 0:
            for i in range(len(digits)-1):
                if i == 0:
                    nonzero_min_value = max(non_zero_available_button)
                    prev_digit_channel += nonzero_min_value
                else:
                    max_value = max(available_button)
                    prev_digit_channel += max_value
        else:
            prev_digit_channel = max(available_button)
    else:
        next_digit_channel = '1000000'
        prev_digit_channel = '1000000'

    if first_nearest_channel:
        first_nearest_channel = str(int(first_nearest_channel)) # 0 제거...
    else:
        first_nearest_channel = "1000000"

    candidates = [first_nearest_channel, second_nearest_channel, prev_digit_channel, next_digit_channel]
    abs_candidates = [len(i) + abs(int(i) - goal_channel) for i in candidates]
    abs_candidates.append(abs(goal_channel - cur_channel))
    button_pressed = min(abs_candidates)
    print(button_pressed)

if __name__ == '__main__':
    main()

# 테스트 케이스
# 다음 자릿수 최솟값
# 이전 자릿수 최댓값

"""
80000
2
8 9
--------
2228

1
9
1 2 3 4 5 6 7 8 9
---------
2

500000
8
0 2 3 4 6 7 8 9
---------
11117

5457
3
6 7 8
---------
6

8000 
5
0 6 7 8 9
--------
2449

8000
6
0 5 6 7 8 9
--------
3116

1555
8
0 1 3 4 5 6 7 9
-------
670
    
101
3
4 5 6
-------
1
    
162
9
0 1 3 4 5 6 7 8 9
-------
62
    
10
9
1 2 3 4 5 6 7 8 9
---------------
11
    
1
10
0 1 2 3 4 5 6 7 8 9
---------------
99
    
1
1
1
----------
2
    
0
9
1 2 3 4 5 6 7 8 9
----------
1
    
101
0
----------
1
    
100000
9
0 1 2 3 4 5 6 7 8
---------------
6
    
1
10
0 1 2 3 4 5 6 7 8 9
-----------------
99
    
1111
9
1 2 3 4 5 6 7 8 9
-------------
1011

얘 안됨.
****
2229
6
4 5 6 7 8 9
5
****
    
10
1
0
2
    
0
10
0 1 2 3 4 5 6 7 8 9
100
    
9
8
0 3 4 5 6 7 8 9
4
    
0
3
0 1 2
4

"""