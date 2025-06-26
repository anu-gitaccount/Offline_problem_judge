
# Goals :
    # Displays the Problem
    # Accepts the User's Code
    # Runs it against TestCases
    # Shows Verdict

# Libraries
    # To Load a JSON File import json
    # To Compile the user's Code import subprocess 
    # For file management import os



import json
import subprocess
import os
import sys



# Create a function to Load the Problem from file scraped_prob
def load_problem(file_path):

    try:
        with open(file_path, "r") as statement:
            # json.load() parse a valid json string in python object
            return json.load(statement)
    except Exception as e:
        print(f"Error Ocurred: {e}")
        sys.exit(1)





# Create a function to compile and run the code
def run_code(code_file, input_data):

    try:
        
        # Run a subprocess to compile the code and produce a output file
        subprocess.run(["g++", code_file, "-o", "a.out"])

        # Run The output file and feeds it input and store the output in a list
        result = subprocess.run(["./a.out"],
                                input = input_data.encode(),
                                capture_output = True,
                                timeout = 2
                                )
        
        # .encode() func convert strings to bytes
        # Return the produced result

        return result.stdout.decode().strip()

        # result.stdout is program's output in bytes
        # .decode converts it from bytes to string 
        # .strip() removes trailing space and newline char
    except subprocess.TimeoutExpired:
        return "TLE (Time Limit Exceeded)"
    except Exception as e:
        return f"Error {e}"
    




def normalize_output(output):
    return ' '.join(output.strip().split())


# Main Func that handles the execution of functions
def main():

    # Locate the Problem Path
    problem_path = "/home/anurag/cp_tester/scraped_prob/two_sum.json"

    # Func call to load the problem
    problem = load_problem(problem_path)

    # Print the Title and Discription of problem
    print(f"Problem : {problem['title']}")
    print(problem["description"])

    code_file = "/home/anurag/cp_tester/testcases/two_sum.cpp"
    #code_file.strip() : if we are taking input from user


    for i, tc in enumerate(problem["test_cases"]):
        actual = normalize_output(run_code(code_file, tc["input"]))

        expected = normalize_output(tc["expected_output"].strip())

        print(f"Test case {i+1}:")
        print(f"Input : {tc['input']}")
        print(f"Your output: {actual}")
        print(f"Expected output: {expected}")
        print("Passed" if actual == expected else "failed\n")



# main function call
if __name__ == "__main__":
    main()






