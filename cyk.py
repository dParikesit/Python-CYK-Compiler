def cyk_algorithm(grammar, tokenized_input, stat = False):

    cyk_Table = [[[] for j in range(i)] for i in range(len(tokenized_input), 0, -1)]

    #Line checker
    check_Table = [False for _ in range(len(tokenized_input))]
    pos_Table = [[set() for j in range(i)] for i in range(len(tokenized_input), 0, -1)]
    pos_Table[0] = [set([i]) for i in range(len(tokenized_input))]

    #Inisialisasi baris pertama
    for i, token in enumerate(tokenized_input):
        for rule in grammar:
            if rule[1] == token and rule[0] not in cyk_Table[0][i]:
                cyk_Table[0][i].append(rule[0])
    
    if stat:
        print()
        print(cyk_Table[0])
        print(len(cyk_Table[0]))
        print(len(tokenized_input))

    #Mengisi sisa table
    for i in range(1, len(cyk_Table)):
        for j in range(len(cyk_Table[i])):
            for k in range(i):
                left_cell = cyk_Table[k][j]
                right_cell = cyk_Table[i-k-1][k+j+1]

                for left in left_cell:
                    for right in right_cell:
                        target = []
                        target.append(left)
                        target.append(right)
                        
                        for rule in grammar:
                            if rule[1:3] == target and rule[0] not in cyk_Table[i][j]:
                                cyk_Table[i][j].append(rule[0])

                                pos_Table[i][j] = pos_Table[i][j].union(pos_Table[k][j])
                                pos_Table[i][j] = pos_Table[i][j].union(pos_Table[i-k-1][k+j+1])

                                # print(pos_Table[i][j])
                                # print(i, j)
                                # print("pos table^")
                                if ('deriv' not in rule):
                                    for pos in pos_Table[i][j]:
                                        check_Table[pos] = True
       


                # print(f"{i} {j} {k}")
                # print(left_cell)
                # print(right_cell)
                # print(cyk_Table[i][j])
                # print("--------------")
    
    #Check if accepted
    print(check_Table)
    print(len(check_Table))
    print("---------Final-----------")
    if stat:
        for table in cyk_Table:
            print(table)
            print("==========================================")
    for item in cyk_Table[-1][0]:
        if (item == "BLOCK_CODE"):
            print("Accepted")
            break
    else:
        print("Syntax Error")

    return check_Table
    
def line_error_checker(check_table, tokenized_line):
    for i, isCorrect in enumerate(check_table):
        if not isCorrect :
            print("Error line :" , tokenized_line[i])
            break