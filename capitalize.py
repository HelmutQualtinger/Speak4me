def capitalize_and_punctuate(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Capitalize the first character
                capitalized_line = line[0].upper() + line[1:]
                
                # Add full stop if line doesn't end with punctuation
                if not capitalized_line[-1] in ['.', '!', '?', ',', ':', ';']:
                    capitalized_line += '.'
                print(capitalized_line, "\n")
                
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    capitalize_and_punctuate("sentences.txt")