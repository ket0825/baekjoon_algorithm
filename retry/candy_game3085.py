import sys
# import array
# array.array("i")

def make_transposed(mat: list[list[str]]) -> list[list[str]]:
     return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat))]

def count_consecutive_color(mat: list[list[str]]
                            ) -> list[int]:
    consecutive_color_count_list = []
    for row in mat:
        consecutive_color_count = 0
        cur_color = None
        prev_color = None
        for col in row:
            cur_color = col
            if cur_color != prev_color and prev_color != None:
                consecutive_color_count_list.append(consecutive_color_count)
                consecutive_color_count = 1
                prev_color = cur_color
            else:    
                prev_color = cur_color
                consecutive_color_count+=1
        consecutive_color_count_list.append(consecutive_color_count)
    
    return consecutive_color_count_list

def count_consecutive_color_row(mat: list[list[str]],
                                index_checklist: list[int],
                                ) -> list[int]:
    consecutive_color_count_list = []
    for rownum in index_checklist:
        consecutive_color_count = 0
        cur_color = None
        prev_color = None
        for col in mat[rownum]:
            cur_color = col
            if cur_color != prev_color and prev_color != None:
                consecutive_color_count_list.append(consecutive_color_count)
                consecutive_color_count = 1
                prev_color = cur_color
            else:    
                prev_color = cur_color
                consecutive_color_count+=1
        consecutive_color_count_list.append(consecutive_color_count)

    return consecutive_color_count_list


def main():
    n = int(sys.stdin.readline().rstrip('\n'))
    inputs = [sys.stdin.readline().rstrip("\n") for i in range(n)]

    mat = [[char for char in elem] for elem in inputs]
    
    # before swap check.
    if (max(count_consecutive_color(mat)) == n 
        or max(count_consecutive_color(make_transposed(mat))) == n
        ):
        print(n)
        exit()

    # swap.
    max_color_count = 0
    for i in range(n-1):
        for j in range(n-1):
            #swapping horizontal
            temp1 = mat[i][j+1]
            temp2 = mat[i][j]
            mat[i][j+1] = mat[i][j]
            mat[i][j] = temp1
            max_color_count = max(*count_consecutive_color_row(make_transposed(mat), index_checklist=[j, j+1]),
                                  *count_consecutive_color_row(mat, index_checklist=[i]),
                                  max_color_count
                                  )
            mat[i][j] = temp2
            mat[i][j+1] = temp1
            # swapping vertical
            temp1 = mat[i+1][j]
            temp2 = mat[i][j]
            mat[i+1][j] = mat[i][j]
            mat[i][j] = temp1
            max_color_count = max(*count_consecutive_color_row(make_transposed(mat), index_checklist=[j]),
                                  *count_consecutive_color_row(mat, index_checklist=[i, i+1]),
                                  max_color_count
                                  )
            mat[i+1][j] = temp1
            mat[i][j] = temp2

            if max_color_count == n:
                print(max_color_count)
                exit() 

        # swapping vertical (last line)
        temp1 = mat[i+1][n-1]
        temp2 = mat[i][n-1]
        mat[i+1][n-1] = mat[i][n-1]
        mat[i][n-1] = temp1
        max_color_count = max(*count_consecutive_color_row(make_transposed(mat), index_checklist=[n-1]),
                                *count_consecutive_color_row(mat, index_checklist=[i, i+1]),
                                max_color_count
                                )
        mat[i+1][n-1] = temp1
        mat[i][n-1] = temp2
        
        if max_color_count == n:
            print(max_color_count)
            exit() 

    print(max_color_count)
    
if __name__ == "__main__":
    main()


import sys
def make_transposed(mat):
     return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat))]
def count_consecutive_color(mat):
    consecutive_color_count_list = []
    for row in mat:
        consecutive_color_count = 0
        cur_color = None
        prev_color = None
        for col in row:
            cur_color = col
            if cur_color != prev_color and prev_color != None:
                consecutive_color_count_list.append(consecutive_color_count)
                consecutive_color_count = 1
                prev_color = cur_color
            else:    
                prev_color = cur_color
                consecutive_color_count+=1
        consecutive_color_count_list.append(consecutive_color_count)
    
    return consecutive_color_count_list

def count_consecutive_color_row(mat, index_checklist):
    consecutive_color_count_list = []
    for rownum in index_checklist:
        consecutive_color_count = 0
        cur_color = None
        prev_color = None
        for col in mat[rownum]:
            cur_color = col
            if cur_color != prev_color and prev_color != None:
                consecutive_color_count_list.append(consecutive_color_count)
                consecutive_color_count = 1
                prev_color = cur_color
            else:    
                prev_color = cur_color
                consecutive_color_count+=1
        consecutive_color_count_list.append(consecutive_color_count)
    return consecutive_color_count_list

def main():
    n = int(sys.stdin.readline().rstrip('\n'))
    inputs = [sys.stdin.readline().rstrip("\n") for i in range(n)]
    mat = [[char for char in elem] for elem in inputs]
    if max(count_consecutive_color(mat)) == n or max(count_consecutive_color(make_transposed(mat))) == n:
        print(n)
        exit()
    max_color_count = 0
    for i in range(n-1):
        for j in range(n-1):
            temp1 = mat[i][j+1]
            temp2 = mat[i][j]
            mat[i][j+1] = mat[i][j]
            mat[i][j] = temp1
            max_color_count = max(*count_consecutive_color_row(make_transposed(mat), index_checklist=[j, j+1]), *count_consecutive_color_row(mat, index_checklist=[i]), max_color_count)
            mat[i][j] = temp2
            mat[i][j+1] = temp1
            temp1 = mat[i+1][j]
            temp2 = mat[i][j]
            mat[i+1][j] = mat[i][j]
            mat[i][j] = temp1
            max_color_count = max(*count_consecutive_color_row(make_transposed(mat), index_checklist=[j]), *count_consecutive_color_row(mat, index_checklist=[i, i+1]), max_color_count)
            mat[i+1][j] = temp1
            mat[i][j] = temp2
            if max_color_count == n:
                print(max_color_count)
                exit() 
        temp1 = mat[i+1][n-1]
        temp2 = mat[i][n-1]
        mat[i+1][n-1] = mat[i][n-1]
        mat[i][n-1] = temp1
        max_color_count = max(*count_consecutive_color_row(make_transposed(mat), index_checklist=[n-1]), *count_consecutive_color_row(mat, index_checklist=[i, i+1]), max_color_count)
        mat[i+1][n-1] = temp1
        mat[i][n-1] = temp2        
        if max_color_count == n:
            print(max_color_count)
            exit() 
    print(max_color_count)
if __name__ == "__main__":
    main()

"""
5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ

5
PCCPY
CYCZZ
CCPZP
YCYZP
PCPZY

5
PCCPY
CYCZZ
CCPZP
YCYZP
PPPPY

5
PPPPC
PCYYC
PZCYZ
PZZCC
PYYYC

"""