from utils import read_input, write_output
from algorithms import SimpleGreedy
import sys

if __name__ == "__main__":
    # Debug flags
    print_input = False
    print_output = False
    file_in = "inputs_outputs/hard.in"
    file_out = "inputs_outputs/hard.out"

    if len(sys.argv) == 5:
        file_in = sys.argv[1]
        file_out = sys.argv[2]
        print_input = sys.argv[3]
        print_output = sys.argv[4]
    elif len(sys.argv) == 3:
        file_in = sys.argv[1]
        file_out = sys.argv[2]

    # Get the input from file
    data_in = read_input(file_in)
    # Print input problems for sanity
    if print_input:
        counter = 1
        for problem in data_in:
            print("Problem {}: {}".format(counter, problem))
            counter += 1

    # Run our algorithm on all problems
    data_out = []
    for prob in data_in:
        data_out.append(SimpleGreedy.solve(prob))
    # Print solved problems for sanity
    if print_output:
        counter = 1
        for prob in data_out:
            print("Problem {}: {}".format(counter, prob))
            counter += 1

    # Write our algorithm's output to a file
    write_output(data_out, file_out)
