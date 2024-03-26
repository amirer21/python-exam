import tabnanny
import tokenize

# Path to the file you want to check
filename = "tab_error_code.py"

# Set verbose mode to get detailed information
tabnanny.verbose = 1

# Function to process the file
def check_indentation(file_path):
    with tokenize.open(file_path) as file:
        tokens = tokenize.generate_tokens(file.readline)
        try:
            tabnanny.process_tokens(tokens)
        except IndentationError as e:
            # Handle indentation error
            print(f"Indentation Error in {file_path}: {e}")

# Check the file
check_indentation(filename)
