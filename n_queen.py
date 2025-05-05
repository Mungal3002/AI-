def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens_backtracking(n):
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)

    board = [-1] * n
    solutions = []
    backtrack(0)
    return solutions


from collections import defaultdict

def solve_nqueens_branch_and_bound(n):
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if not cols[col] and not main_diag[row - col] and not sec_diag[row + col]:
                board[row] = col
                cols[col] = main_diag[row - col] = sec_diag[row + col] = True
                backtrack(row + 1)
                cols[col] = main_diag[row - col] = sec_diag[row + col] = False

    board = [-1] * n
    cols = [False] * n
    main_diag = defaultdict(bool)
    sec_diag = defaultdict(bool)
    solutions = []
    backtrack(0)
    return solutions



n = 4
print("Backtracking Solution:")
backtracking_solutions = solve_nqueens_backtracking(n)
for sol in backtracking_solutions:
    print(sol)

print("\nBranch and Bound Solution:")
branch_solutions = solve_nqueens_branch_and_bound(n)
for sol in branch_solutions:
    print(sol)
