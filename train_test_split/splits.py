def find_lines_with_words(file_path, words):
    matched_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            if any(word in line for word in words):
                matched_lines.append(line.strip())
    return matched_lines

# Example usage
file_path = 'include_val.txt'
words = ['1. loud', '2. quiet', '3. happy','4. sad','5. Beautiful', '6. Ugly', '7. Deaf', '8. Blind','9. Nice','10. Mean','11. rich','12. poor','13. thick','14. thin','15. expensive','16. cheap','17. flat','18. curved','19. male','20. female','21. tight','22. loose','23. high','24. low','25. soft','26. hard','27. deep','28. shallow','29. clean','30. dirty','31. strong','32. weak','33. dead','34. alive','35. heavy','36. light','39. famous','78. long','79. short','80. tall','81. wide','82. narrow','83. big large','84. small little','85. slow','86. fast','87. hot','88. cold','89. warm','90. cool','91. new','92. old','93. young','94. good','95. bad','96. wet','97. dry','98. sick','99. healthy']
output_file = 'temp_include_val.txt'

matched_lines = find_lines_with_words(file_path, words)

if matched_lines:
    with open(output_file, 'w') as output:
        for line in matched_lines:
            output.write(line + '\n')
    print("Output lines were written to", output_file)
else:
    print("No lines containing any of the words were found.")
