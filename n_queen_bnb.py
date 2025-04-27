def solve_n_queens(n):
    def is_safe(row, col):
        # Check if a queen can be placed at (row, col)
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(row, cols, diag1, diag2):
        if row == n:
            # Found a valid solution
            solutions.append([' . ' * col + ' Q ' + ' . ' * (n - col - 1) for col in board])
            return

        for col in range(n):
            d1 = row - col  # Left diagonal index
            d2 = row + col  # Right diagonal index

            # Check if column and diagonals are free
            if not (cols[col] or diag1[d1] or diag2[d2]):
                board[row] = col
                cols[col] = diag1[d1] = diag2[d2] = True  # Mark as occupied
                backtrack(row + 1, cols, diag1, diag2)
                cols[col] = diag1[d1] = diag2[d2] = False  # Backtrack

    solutions = []
    board = [-1] * n  # board[row] = column where queen is placed
    cols = [False] * n  # Track occupied columns
    diag1 = [False] * (2 * n - 1)  # Track left diagonals (row - col)
    diag2 = [False] * (2 * n - 1)  # Track right diagonals (row + col)
    backtrack(0, cols, diag1, diag2)
    return solutions

# Example usage
n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-queens: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()