def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))


def is_valid_move(grid, row, col, num):
    if num in grid[row] or num in [grid[i][col] for i in range(9)]:
        return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None


def solve_sudoku(grid):
    row, col = find_empty_location(grid)
    if row is None:
        return True

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False


def get_user_input():
    print("Enter the Sudoku puzzle row by row. Use 0 for empty cells.")
    sudoku_grid = []
    for i in range(9):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated numbers): ").split()))
        sudoku_grid.append(row)
    return sudoku_grid


if __name__ == "__main__":
    print("Welcome to the Sudoku Solver!")
    sudoku_grid = get_user_input()

    print("\nInput Sudoku Puzzle:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Puzzle:")
        print_grid(sudoku_grid)
    else:
        print("\nNo solution exists.")