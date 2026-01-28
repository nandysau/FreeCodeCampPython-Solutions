#STEP - 1
def pin_extractor(poem):
    pass
#Step - 2
def pin_extractor(poem):
    secret_code = ''
#Step - 3
def pin_extractor(poem):
    secret_code = ''

poem = 'Stars and the moon\nshine in the sky\nwhite and bright\nuntil the end of the night'
pin_extractor(poem)
#Step - 4
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)
#Step - 5
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line in lines:
        print(line)    

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)

#Step - 6
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line in lines:
        print(line)
        words = line.split(' ')   
        print(words)     

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)

#Step - 7
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index,line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        print(words)

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)

#Step - 8
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        print(words[line_index])


poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)

#Step - 9
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        print(len(words[line_index]))


poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)

#Step - 10
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        print(str(len(words[line_index])))


poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)

#Step - 11
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        secret_code +=str(len(words[line_index]))


poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)

#Step - 12
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
      
        words = line.split()
        
        secret_code += str(len(words[line_index]))
    return secret_code


poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)

#Step - 13
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        words = line.split()
        secret_code += str(len(words[line_index]))
    return secret_code


poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

print(pin_extractor(poem))

#Step - 14
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        words = line.split()
        if line_index < len(words):
            secret_code += str(len(words[line_index]))
    return secret_code

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

print(pin_extractor(poem))

#Step - 15
def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        words = line.split()
        if len(words) > line_index:
            secret_code += str(len(words[line_index]))
        else:
            secret_code += '0'
    return secret_code

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

print(pin_extractor(poem))

#Step - 16

def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        words = line.split()
        if len(words) > line_index:
            secret_code += str(len(words[line_index]))
        else:
            secret_code += '0'
    return secret_code

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

# print(pin_extractor(poem))

#Step - 17
def pin_extractor(poems):
 for poem in poems:
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        words = line.split()
        if len(words) > line_index:
            secret_code += str(len(words[line_index]))
        else:
            secret_code += '0'
    return secret_code
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

# print(pin_extractor(poem))

#Step - 18
def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

# print(pin_extractor(poem))

#Step - 19

def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))
