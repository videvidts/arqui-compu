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

j = 0
memory = 0

print(content)

isArray = False

# Poblar DATA
while content[j] != 'CODE:':
    # Reconocemos datos que son arreglos

        if content[j] != 'DATA:':
            label, value = content[j].split(' ')

            ## Evaluamos los values x dataType y los guardamos como binarios
            scale = 0
            if 'b' in value:
                value = value.split('b')[0]
                value = value.zfill(16)
            elif 'd' in value:
                scale = 10
                value = value.split('d')[0]
                value = bin(int(value, scale)).zfill(16)
            elif 'h' in value:
                scale = 16
                value = value.split('h')[0]
                value = bin(int(value, scale)).zfill(16)
            else:
                value = bin(int(value)).zfill(16)
            data[memory] = [label, value]
            memory += 1
        j += 1
    
# Poblar CODE

print(data)

sys.exit()