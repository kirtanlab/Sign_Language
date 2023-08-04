def find_lines_with_words(file_path, words):
    matched_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            if any(word in line for word in words):
                matched_lines.append(line.strip())
    return matched_lines

# Example usage
file_path = 'include_test.txt'
words = ['1. loud', '2. quiet', '3. happy']
output_file = 'lstm_include_test.txt'

matched_lines = find_lines_with_words(file_path, words)

if matched_lines:
    with open(output_file, 'w') as output:
        for line in matched_lines:
            output.write(line + '\n')
    print("Output lines were written to", output_file)
else:
    print("No lines containing any of the words were found.")
