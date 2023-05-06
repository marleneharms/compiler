# dictionary of the tokens and their values
tokens = {
    'int': 1,
    'float': 2,
    'string': 3,
    'for':4,
    'if':5,
    'else':6,
    'while':7,
    'return':8,
    'read':9,
    'write':10,
    'void':11,
    '+':12,
    '-':13,
    '*':14,
    '/':15,
    '<':16,
    '<=':17,
    '>':18,
    '>=':19,
    '==':20,
    '!=':21,
    '=':22,
    ';':23,
    ',':24,
    '(':25,
    ')':26,
    '{':27,
    '}':28,
    '[':29,
    ']':30,
    'id':31,
    'num':32,
    'floatnum':33,
    'stringval':34
}

# dictionary of keywords
keywords = {'int', 'float', 'string', 'for', 'if', 'else', 'while', 'return', 'read', 'write', 'void'}

# dictionary of delimiters
delimiters = {'+', '-', '*', '/', '<', '<=', '>', '>=', '==', '!=', '=', ';', ',', '(', ')', '{', '}', '[', ']', '\n', '\t'}

# dictionary of the whitespace characters
whitespace = {' ', '\t', '\n', '\r'}

# transition table headers
header = {'LETTER':0, 'DIGIT':1, '+':2, '-':3, '*':4, '/':5, '<':6, '>':7, '=':8, '!':9, ';':10, ',':11,'"':12,'.':13, '(':14, ')':15, '{':16, '}':17, '[':18, ']':19, 'BLANK':20, 'RARE':21, 'EOF':22}

# transition table
transition_table = [
    [5, 2, 20, 21, 22, 6, 9, 10, 11, 12, 23, 24, 1, 40, 25, 26, 27, 28, 29, 30, 0, 39, 13],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 38],
    [40, 2, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 39, 3, 15, 15, 15, 15, 15, 15, 15, 39, 38],
    [40, 4, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 39, 38],
    [40, 4, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 39, 39, 16, 16, 16, 16, 16, 16, 16, 39, 38],
    [5, 5, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 39, 39, 17, 17, 17, 17, 17, 17, 17, 39, 38],
    [18, 18, 18, 18, 7, 18, 18, 18, 18, 18, 18, 18, 39, 39, 18, 18, 18, 18, 18, 18, 8, 39, 38],
    [7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 38],
    [7, 7, 7, 7, 7, 19, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 38],
    [31, 31, 31, 31, 31, 31, 31, 31, 32, 31, 31, 31, 39, 39, 31, 31, 31, 31, 31, 31, 31, 39, 38],
    [33, 33, 33, 33, 33, 33, 33, 33, 34, 33, 33, 33, 39, 39, 33, 33, 33, 33, 33, 33, 33, 39, 38],
    [35, 35, 35, 35, 35, 35, 35, 35, 36, 35, 35, 35, 39, 39, 35, 35, 35, 35, 35, 35, 35, 39, 38],
    [41, 41, 41, 41, 41, 41, 41, 41, 37, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 39, 38]
]

# set of the error states
error_states = set(range(38,42))

# set of the final states
final_states = set(range(13,37))

# dictionaries of tables for identifiers, numbers, and strings
identifiers = {}
numbers = {}
floatnumbers = {}
strings = {}

# array of tokens for the output
tokens_recognition = []
scanner_output = []

# open file and read it
def open_file(file_name):
    file = open(file_name, 'r') # open the file
    data = file.read() # read the file
    file.close() # close the file
    return data 

# find next state in the transition table given the actual state and the next character
def nextState(state, character):
    if character.isalpha():
        return transition_table[state][0]
    elif character.isdigit():
        return transition_table[state][1]
    elif character in header:
        return transition_table[state][header[character]]
    elif character in whitespace:
        return transition_table[state][20]
    elif character == '':
        return transition_table[state][22]
    else:
        return transition_table[state][21]

# print the tables
def printTables():
    print("SCANNER OUTPUT: ")
    print(scanner_output)
    print("\n\n")

    # invert tokens keys and values
    token_recognition_inverted = {v: k for k, v in tokens.items()}
    identifiers_inverted = {v: k for k, v in identifiers.items()}
    numbers_inverted = {v: k for k, v in numbers.items()}
    floatnumbers_inverted = {v: k for k, v in floatnumbers.items()}
    strings_inverted = {v: k for k, v in strings.items()}

    print("TOKEN RECOGNITION: ")
    for i in scanner_output:
        if isinstance(i, tuple):
            if i[0] == 31:
                print(identifiers_inverted[i[1]], end=' ')
            elif i[0] == 32:
                print(numbers_inverted[i[1]], end=' ')
            elif i[0] == 33:
                print(floatnumbers_inverted[i[1]], end=' ') 
            elif i[0] == 34:
                print(strings_inverted[i[1]], end=' ')
        else:
            print(token_recognition_inverted[i], end=' ')
    print("\n\n")


    print("Identifiers: ", identifiers_inverted)
    print("Numbers: ", numbers_inverted)
    print("Float Numbers: ", floatnumbers_inverted)
    print("Strings: ", strings_inverted)

# scanner function
def scanner():
    # open the file and read it
    code = open_file('input2.txt')
    # initialize the state to 0
    state = 0
    # initialize the lexeme to the empty string
    lexeme = ''
    # initialize the next character to the first character of the code
    next_char = code[0]
    # index the next character
    index = 0

    # loop through the code until EOF is reached
    while next_char != '':

        # if the next character is a whitespace, skip it
        if next_char not in whitespace: 
            lexeme = ''
            state = 0
            # loop until a final or error state is reached
            while state not in final_states or state in error_states:
                # get the next state
                state = nextState(state, next_char)
                # if the state is an error state or a final state, break the loop
                if(state in final_states or state in error_states):
                    break
                lexeme += next_char.lower()
                # increment the index and get the next character
                index += 1
                if(index >= len(code)):
                    break
                next_char = code[index]
                # print('state: ' + str(state))
                # print('lexeme: ' + lexeme)``

            # if the state is a final state, add the token to the output
            if state in final_states:
                if lexeme == '':
                    if next_char in tokens:
                        scanner_output.append(tokens[next_char])
                if state == 17:
                    if lexeme in keywords:
                        scanner_output.append(tokens[lexeme])
                        if next_char in tokens:
                            scanner_output.append(tokens[next_char])
                    else:
                        if lexeme not in identifiers:
                            identifiers[lexeme] = len(identifiers) + 1
                        scanner_output.append(tuple([tokens["id"], identifiers[lexeme]]))
                        if next_char in tokens:
                            scanner_output.append(tokens[next_char])
                elif state == 13:
                    return "End of File"
                elif state == 14:
                    lexeme += next_char
                    if lexeme not in strings:
                        strings[lexeme] = len(strings) + 1
                    scanner_output.append(tuple([tokens["stringval"], strings[lexeme]]))
                    if(next_char in tokens):
                        scanner_output.append(tokens[next_char])
                elif state == 15:
                    if lexeme not in numbers:
                        numbers[lexeme] = len(numbers) + 1
                    scanner_output.append(tuple([tokens["num"], numbers[lexeme]]))
                    if(next_char in tokens):
                        scanner_output.append(tokens[next_char])
                elif state == 16:
                    if lexeme not in floatnumbers:
                        floatnumbers[lexeme] = len(floatnumbers) + 1
                    scanner_output.append(tuple([tokens["floatnum"], floatnumbers[lexeme]]))
                    if(next_char in tokens):
                        scanner_output.append(tokens[next_char])
                elif state == 33:
                    scanner_output.append(tokens[lexeme])
                elif lexeme in tokens:
                    scanner_output.append(tokens[lexeme])

            
            # if state is error state return error message
            elif state in error_states:
                if state == 38:
                    print("Error EOF")
                    return "Error EOF" 
                elif state == 39:
                    print("Error Identifier")
                    return "Error Symbol"
                elif state == 40:
                    print("Error Invalid Float Number")
                    return "Invalid Float Number"
                elif state == 41:
                    print("Error Invalid Token")
                    return "Error Token"
                
        # increment the index
        index += 1 
        if index < len(code):
            next_char = code[index]
        else:
            next_char = ''
    return 'EOF'
    
                
scanner = scanner()
if scanner == 'EOF':
    printTables()
 