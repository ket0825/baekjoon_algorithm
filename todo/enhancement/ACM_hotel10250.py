import sys
input = sys.stdin.readline

def main():
    T = int(input().rstrip())
    for _ in range(T):
        result = map(int, input().rstrip().split(" "))
        H, W, client_num = result

        floor = client_num % H 
        room_order = client_num // H + 1

        if floor == 0:
            floor = H
            room_order -= 1
        
        if room_order < 10:
            room_str = "0"+str(room_order)
        else:
            room_str = str(room_order)
        
        floor_str = str(floor)
        
        print(floor_str+room_str)

if __name__ == '__main__':
    main()