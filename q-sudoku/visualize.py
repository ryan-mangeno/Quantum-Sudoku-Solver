import numpy as np
import matplotlib.pyplot as plt
import math

def visualize_sudoku_solution(puzzle_file, solution_file):
    """
    Loads a Sudoku puzzle and its solution from files and visualizes the result.
    """
    try:
        puzzle = np.loadtxt(puzzle_file, dtype=int)
        solution = np.loadtxt(solution_file, dtype=int)
    except FileNotFoundError as e:
        print(f"Error: {e}. Please run 'generate_sudoku_board.py' first.")
        return

    grid_size = puzzle.shape[0]
    n = int(math.sqrt(grid_size))

    if grid_size not in [2, 4, 9]:
        print("Error: Visualization only supports 2x2, 4x4, or 9x9 puzzles.")
        return

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.set_title(f"Sudoku Solution ({grid_size}x{grid_size})", fontsize=16)

    # Configure grid and ticks
    ax.set_xticks(np.arange(grid_size + 1))
    ax.set_yticks(np.arange(grid_size + 1))
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
    ax.tick_params(which='both', bottom=False, left=False, labelbottom=False, labelleft=False)

    # Draw the thicker n x n sub-grid lines
    for i in range(n, grid_size, n):
        ax.axvline(i, color='k', linewidth=3)
        ax.axhline(i, color='k', linewidth=3)

    # Fill in the numbers
    for i in range(grid_size):
        for j in range(grid_size):
            # Check if the number was part of the original puzzle
            if puzzle[i, j] != 0:
                ax.text(j + 0.5, grid_size - 1 - i + 0.5, str(puzzle[i, j]),
                        ha='center', va='center', fontsize=24/n, fontweight='bold', color='black')
            # Otherwise, it's a solved number
            else:
                ax.text(j + 0.5, grid_size - 1 - i + 0.5, str(solution[i, j]),
                        ha='center', va='center', fontsize=24/n, color='blue')

    plt.show()

if __name__ == '__main__':
    print("Displaying visualization for the 4x4 puzzle...")
    visualize_sudoku_solution("puzzle_4x4.txt", "solution_4x4.txt")

    print("Displaying visualization for the 9x9 puzzle...")
    visualize_sudoku_solution("puzzle_9x9.txt", "solution_9x9.txt")
