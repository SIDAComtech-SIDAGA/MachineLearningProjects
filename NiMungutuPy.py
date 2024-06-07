def print_pattern(num_rows, char="*"):
    for i in range(num_rows):
        for num_cols in range(num_rows-i):
            print(char, end="")
        print()
 
print_pattern(5)
print_pattern(5,"&")