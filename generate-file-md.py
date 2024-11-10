import sys
import os

def generate_markdown(input_file,):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    output_folder = f'{lines[0].strip()}. {lines[1].strip()}'
    os.makedirs(output_folder, exist_ok=True)
    n_len = len(lines)
    i_file = 1
    for i in range(5, n_len,2):
        
        output_file = f'{i_file}. {lines[i].strip()}.md'
        output_file = f'{output_folder}/{output_file}'
        i_file += 1
        with open(output_file, 'w') as file1:
            file1.write("# " + lines[i].strip() + "\n\n")
        

if len(sys.argv) != 2:
    print("Usage: python generate-file-md.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]
generate_markdown(input_file)