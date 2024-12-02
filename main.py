# Read in the table

table_address = "/home/sky/Documents/A_projects/portfolio/boolean_logic/INPUT_truth_table.txt"
truth_table = []

with open(table_address, 'r') as f:
    for line in f.readlines():
        print("Row (raw): ", line.strip())
        row = line.strip().split(' ')
        print("Row (fin): ", row, '\n')

def negate_var(var: str):
    tmp = ''
    for e in var:
        tmp += e + "\u0305"
    return tmp
# results = 4, 5
#4 inputs + 2 results.

# print SOP

# if element is "0":
    # print()

test = negate_var('test')
print(test)
# print("AB" + "\u0305")
