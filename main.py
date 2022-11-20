import sys

# Helper function for reading file input
def get_input(filename_in):
    # Read the lines from the file
    in_file = open(filename_in, 'r')
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


# Helper function for writing all solutions to output
def write_output(data_out, filename_out):
    # Create storage for output
    all_data = []
    # Process all problems
    for prob in data_out:
        # Get number of leaves and edges
        leaves = 0
        edges = 0
        for vert in prob:
            if len(prob[vert]) == 1:
                leaves += 1
            edges += len(prob[vert])
        edges //= 2 # We count each edge twice, so divide by 2

        # Remove duplicate edges
        for vert in prob:
            for item in prob[vert]:
                prob[item].remove(vert)
        
        # Put everything in the list for output
        all_data.append((leaves, edges))
        for vert in prob:
            for item in prob[vert]:
                all_data.append((vert, item))

    # Format output as strings
    all_lines = []
    for line in all_data:
        all_lines.append("{} {}\n".format(line[0], line[1]))
    all_lines[-1] = all_lines[-1].strip()
    
    # Write output
    out_file = open(filename_out, 'w')
    out_file.writelines(all_lines)
    out_file.close


# Main function here
if __name__ == "__main__":
    # Debug flags
    print_input = False
    print_output = False
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
    if print_input:
        counter = 1
        for problem in data_in:
            print("Problem {}: {}".format(counter, problem))
            counter += 1

    # Here is where we would actually run our algorithm
    # For now, just hardcode the given results
    data_out = data_in
    # First problem removes edge (0, 2)
    data_out[0][0].remove(2)
    data_out[0][2].remove(0)
    # Second problem removes edge (0, 1)
    data_out[1][0].remove(1)
    data_out[1][1].remove(0)
    # Print solved problems for sanity
    if print_output:
        counter = 1
        for problem in data_out:
            print("Problem {}: {}".format(counter, problem))
            counter += 1


    # Write our algorithm's output to a file
    write_output(data_out, file_out)