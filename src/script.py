from src.Assignment import create_sudoku_csp, print_sudoku_solution

sudoku = create_sudoku_csp("easy.txt")
solution = sudoku.backtracking_search()
print_sudoku_solution(solution)