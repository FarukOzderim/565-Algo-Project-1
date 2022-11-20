import sys

# Helper function for reading file input
def get_input(filename):
    # Read the lines from the file
    in_file = open(filename, 'r')
    lines = in_file.readlines()
    in_file.close()

    # Remove all newline characters
    lines = [item.strip() for item in lines]

    # Split input into individual problems
    num_probs = int(lines[0])
    split_problems = []
    current_line = 1
    for i in range(num_probs):
        # Create single problem, empty to start
        temp_problem = []
        # Get and store the problem metadata from the first line
        first_line = lines[current_line].split()
        temp_problem.append((int(first_line[0]), int(first_line[1])))
        num_lines = temp_problem[0][1]
        current_line += 1
        # Read the remainder of the problem and store it
        for j in range(num_lines):
            temp_line = lines[current_line].split()
            temp_problem.append((int(temp_line[0]), int(temp_line[1])))
            current_line += 1
        # Store the problem into the list of all problems
        split_problems.append(temp_problem)

    # Store each problem as a map, create list of problems
    problem_list = []
    for prob in split_problems:
        # Get metadata
        num_verts = prob[0][0]
        num_edges = prob[0][1]
        # Create dict with vertices as keys
        graph = {}
        for i in range(num_verts):
            graph[i] = []
        # Add edges
        for i in range(num_edges):
            edge = prob[i+1]
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        # For sanity, sort each adjacency list
        for i in range(num_verts):
            graph[i].sort()

        # Store graph to list
        problem_list.append(graph)
        
    # Return list of problems
    return problem_list



def write_output(data_out):
    print("File output not implemented")


# Main function here
if __name__ == "__main__":
    # Set filenames for input and output
    file_in = "./hard.in"
    file_out = "./hard.out"
    if len(sys.argv) > 1:
        file_in = sys.argv[1]
    if len(sys.argv) > 2:
        file_out = sys.argv[2]

    # Get the input from file
    data_in = get_input(file_in)
    # Print out problems for sanity
    counter = 1
    for problem in data_in:
        print("Problem {}: {}".format(counter, problem))
        counter += 1

    # Here is where we would actually run our algorithm
    # For now, just hardcode the given results
    data_out = data_in

    # Write our algorithm's output to a file
    #write_output(data_out)