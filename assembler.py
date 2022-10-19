# Retornar instruccion completa -- 20 bits opcode + 16 bit literal/ direccion
# ¿que se le va a entregar a mi programa?

import re
import sys
# sys.argv = argumentos en input, base_prefix = ruta arhcivo, byteorder = endian, excecutable = ruta python

inputFile = sys.argv[1]

data = {}
code = {}
content = []

def remove_first_end_spaces(string):
    return "".join(string.rstrip().lstrip())

def getValue(value):
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
    return value

# Poblar content
with open(inputFile) as f:
    while True:
        line = f.readline()
        # Remove tabs
        element = line.strip('\n').replace('\t',' ')
        # Remove //
        element = element.split('// ')[0]
        # Remove extra space between strings
        element = re.sub(' +', ' ', element)
        # Remove first and end spaces
        element = remove_first_end_spaces(element)
        if element != '':
            content.append(element)

        if not line:
            break

print(content)

j = 0
memory = 0

isArray = False

# Poblar DATA
while content[j] != 'CODE:':
    if content[j] != 'DATA:':
        # Reconocemos datos que son arreglos
        if ' ' in content[j]:
            print('tiene')
            print(content[j].split(' '))
            label, value = content[j].split(' ')
            value = getValue(value)
            data[memory] = [label, value]
            memory += 1
        else:
            isArray = True
            array = []
            k = j
            while isArray and content[k] != 'CODE:':
                print(k, content[k])
                if ' ' in content[k + 1]:
                    isArray = False
                # Sacar primer elemento del arreglo de data y convertirlo en arreglo
                elif ' ' in content[k-1]:
                    label, value = data[memory - 1]
                    array.append(label)
                    array.append([value])

                elif len(array) > 0:
                    value = getValue(content[k])
                    array[1].append(value)

                k += 1
    j += 1
    
# Poblar CODE

print(data)

sys.exit()