



SIZE = 9
matrix = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
     [2, 8, 9, 0, 0, 4, 0, 0, 0],
     [3, 4, 6, 2, 0, 5, 0, 9, 0],
     [6, 0, 2, 0, 0, 0, 0, 1, 0],
     [0, 3, 8, 0, 0, 6, 0, 4, 7],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 9, 0, 0, 0, 0, 0, 7, 8],
     [7, 0, 3, 4, 0, 0, 5, 6, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def print_sudoku():
    for i in matrix:
        print (i)

def number_unassigned(row, col):
    num_unassign = 0
    for i in range(0,SIZE):
        for j in range (0,SIZE):
            if matrix[i][j] == 0:
                row = i
                col = j
                num_unassign = 1
                a = [row, col, num_unassign]
                return a
    a = [-1, -1, num_unassign]
    return a

def is_safe(n, r, c):

    for i in range(0,SIZE):

        if matrix[r][i] == n:
            return False

    for i in range(0,SIZE):

        if matrix[i][c] == n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3;
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if matrix[i][j]==n:
                return False
    return True


def solve_sudoku():
    row = 0
    col = 0

    a = number_unassigned(row, col)
    global backtrack
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]

    for i in range(1,10):

        if is_safe(i, row, col):
            matrix[row][col] = i

            if solve_sudoku():
                return True
            backtrack+=1
            matrix[row][col]=0
    return False


def combinationSum(candidates, target):

    ans = []

    tmp = []

    def helper(idx, total):


        if total > target:
            return

        if total == target:
            ans.append(tmp[::])
            return


        for i in range(idx, len(candidates)):
            total += candidates[i]

            tmp.append(candidates[i])

            helper(i, total)

            tmp.pop()
            total -= candidates[i]
    total=0
    helper(0, total)
    return ans


backtrack=0
if solve_sudoku():
    print_sudoku()
    print("backtrack",backtrack)
else:
    print("No solution")
print("\n")
candidates=[5, 10, 12, 13, 15, 18]
print(candidates)
target=30
c=combinationSum(candidates,target)
print("Combinations are: ",c)
