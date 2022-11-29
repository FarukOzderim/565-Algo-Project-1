from utils import read_input, write_output, plot_graph_from_adjacency_list
from algorithms import SimpleGreedy
from algorithms import Heuristic
import sys

if __name__ == "__main__":
    # Debug flags
    DEBUG = False
    file_in = "../inputs_outputs/hard.in"
    file_out = "../inputs_outputs/hard.out"

    if len(sys.argv) == 4:
        file_in = sys.argv[1]
        file_out = sys.argv[2]
        DEBUG = sys.argv[3]
    elif len(sys.argv) == 3:
        file_in = sys.argv[1]
        file_out = sys.argv[2]

    problem_list = read_input(file_in)

    # Run our algorithm on all problems
    solution_list = []

    for prob in problem_list:
        solution_list.append(SimpleGreedy.solve(prob))

    # Print solved problems for sanity
    if DEBUG:
        counter = 1
        for i in range(len(problem_list)):
            print(f"Problem {counter + 1}: {problem_list[i]}")
            print(f"Solution {counter + 1}: {solution_list[i]}")
            plot_graph_from_adjacency_list(
                problem_list[i], solution_list[i], title=f"Solution {counter}"
            )
            counter += 1

    # Write our algorithm's output to a file
    # write_output(solution_list, file_out)
    #########################################################
    solution_list = []

    for prob in problem_list:
        solution_list.append(Heuristic.solve(prob))

    # Print solved problems for sanity
    if DEBUG:
        counter = 1
        for i in range(len(problem_list)):
            print(f"Problem {counter + 1}: {problem_list[i]}")
            print(f"Solution {counter + 1}: {solution_list[i]}")
            plot_graph_from_adjacency_list(
                problem_list[i], solution_list[i], title=f"Solution {counter}"
            )
            counter += 1

    # Write our algorithm's output to a file
    write_output(solution_list, file_out)
