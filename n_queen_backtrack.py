def solve_n_queens(n):
    # Initialize empty board
    board = [-1] * n  # board[r] = c means queen at position (r,c)
    solutions = []
    
    def is_safe(row, col):
        for i in range(row):
            # Check if queens attack each other (same column or diagonal)
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    
    def backtrack(row):
        if row == n:
            # Found a solution
            solution = []
            for i in range(n):
                # Create a string representation of the board
                line = ' . ' * board[i] + ' Q ' + ' . ' * (n - board[i] - 1)
                solution.append(line)
            solutions.append(solution)
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                # Backtrack
                board[row] = -1
    
    backtrack(0)
    return solutions

# Example usage
n = 4  # 4x4 board
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-queens: {len(solutions)}")
for i, solution in enumerate(solutions[:2]):  # Print first two solutions
    print(f"Solution {i+1}:")
    for line in solution:
        print(line)