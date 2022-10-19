# Retornar instruccion completa -- 20 bits opcode + 16 bit literal/ direccion
# ¿que se le va a entregar a mi programa?

import sys
# sys.argv = argumentos en input, base_prefix = ruta arhcivo, byteorder = endian, excecutable = ruta python

inputFile = sys.argv[1]
print(inputFile)

data = {}
code = {}
content = []
memory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def remove_first_end_spaces(string):
    return "".join(string.rstrip().lstrip())

# Poblar content
with open(inputFile) as f:
    while True:
        line = f.readline()
        element = line.strip('\n').replace('\t',' ')
        print(element)
        element = element.split('// ')[0]
        element = remove_first_end_spaces(element)
        if element != '':
            content.append(element)

        if not line:
            break
print(data)

j = 0

print(content)

# Poblar DATA
while content[j] != 'CODE:':
    if content[j] != 'DATA:':
        label, value = content[j].split(' ')
        data[j] = [label, value]
    j += 1

# Poblar CODE

print(data)

sys.exit()