# Read in the table

table_address = "/home/sky/Documents/A_projects/portfolio/boolean_logic/INPUT_truth_table.txt"
truth_table = []

with open(table_address, 'r') as f:
    for line in f.readlines():
        print("Row (raw): ", line.strip())
        row = line.strip().split(' ')
        print("Row (fin): ", row, '\n')
