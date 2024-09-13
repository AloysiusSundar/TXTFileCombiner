import os

def combine_txt_files(input_folder, output_file):
    try:
        if not os.path.exists(input_folder):
            raise FileNotFoundError(f"The folder {input_folder} does not exist.")
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for filename in os.listdir(input_folder):
                if filename.endswith('.txt'):
                    file_path = os.path.join(input_folder, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                            outfile.write("\n")
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
        
        print(f"All .txt files have been successfully combined into {output_file}")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError as perm_error:
        print(f"Permission error: {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

input_folder = 'D:\King\King' 
output_file = 'combined_output.txt'   
combine_txt_files(input_folder, output_file)
