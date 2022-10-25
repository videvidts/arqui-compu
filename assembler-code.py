# main

import sys
from ast import arg
# sys.argv = argumentos en input, base_prefix = ruta arhcivo, byteorder = endian, excecutable = ruta python

from input_file_processor import get_content
from data_controller import get_data_content
from code_controller import get_code_content, get_labels, get_instructions
import instructions_opcodes


input_file_path = sys.argv[1]

available_assembly_instructions = instructions_opcodes.load_assembly_instructions("CPU - instructions_opcodes.tsv")
print(available_assembly_instructions)

file_content = get_content(input_file_path)
data = get_data_content(file_content)
code = get_code_content(file_content)
labels = get_labels(file_content)

for elem in code:
    instructions = get_instructions(elem, labels)
    if instructions is not None:
        command, params = instructions.split(' ')

sys.exit()
