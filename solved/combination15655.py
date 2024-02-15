import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().rstrip("\n").split(" "))
    sorted_lst = sorted(list(map(int, input().rstrip("\n").split(" "))))

    def selected_combination(lst: list, start):
        # print("=============", "\nsorted_lst logging:",*sorted_lst[start:], "\nexisting_lst:", *lst, "\nstart:", start)
        if len(lst) == M:
            print(*lst)
            return
        
        for elem in sorted_lst[start:]:
            if elem not in lst:
                lst.append(elem)
                selected_combination(lst, start+1)
                lst.pop()
            start+=1

    selected_combination([], 0)

if __name__ == "__main__":
    main()



## 2. list 자체를 넘겨주는 게 아니라 그냥 start만 가지고 진행함. list는 바깥에 있음.
## i 조차도 그냥 global로 넘겨줘도 됨.
# import sys
# input = sys.stdin.readline


# def back(i,idx):
#     if len(res) == i:
#         print(*res)
#     for j in range(idx, len(numl)):
#             res.append(numl[j])
#             back(i,j+1)
#             res.pop()

# res = []
# n,s = map(int,input().split())
# numl = list(map(int,input().split()))
# #visit = [False for i in range(n)]
# numl.sort()
# back(s,0)