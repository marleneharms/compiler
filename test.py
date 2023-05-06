# input = ['lemon', 'apple', 'banana', 'orange']

# output = []

# for i in range(len(input)):
#     output.append({input[i]: i})

# print(output)

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

if 'void' in tokens:
    print('yes')