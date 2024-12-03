# Read in the table

table_address = "/home/sky/Documents/A_projects/portfolio/boolean_logic/INPUT_truth_table.txt"
truth_table = []
tt_results = []


#Tables Params = 4 inputs w. 2 outputs
with open(table_address, 'r') as f:
    for line in f.readlines()[1:]:
        # print("Row (raw): ", line.strip())
        row = line.strip().split(' ')
        # print("Row (fin): ", row, '\n')

        row_tmp = []
        for bit in row[:]:
            row_tmp.append(int(bit))
        truth_table.append(row_tmp)

        # for bit in row[5:]:
        #     row_tmp.append(int(bit))
        # tt_results.append(row_tmp)



for row in truth_table:
    print(row)
# print(truth_table)

# class bit():
#     def add(self, bit1, bit2):
#         if bit

def negate_str(var: str):
    tmp = ''
    for e in var:
        tmp += e + "\u0305"
    return tmp

# test = ''('test')
# print(test)
# print("AB" + "\u0305")

def lookup_var(index):
    if index == 0:
        return "X1"
    if index == 1:
        return "X2"
    if index == 2:
        return "X3"
    if index == 3:
        return "X4"
    if index == 4:
        return "Z1"
    if index == 5:
        return "Z2"


#SUM OF PRODUCTS EXPRESSIONS WRITE
sop_expressions = []
r = 0
for row in truth_table:
    i = 0
    expression = ''
    for bit in row:
        if i == 4:
            expression += " = "
        if bit == 0:
            expression += negate_str(lookup_var(i)) + ' '

        elif bit == 1:
            expression += lookup_var(i) + ' '

        # input(expression)
        if i == 5:
            sop_expressions.append(expression)
        i += 1
    # for each in


    r += 1



for each in sop_expressions:
    print(each)
