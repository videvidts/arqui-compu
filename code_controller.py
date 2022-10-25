from number_converter import convert_str_to_bin
from assembly_instruction_recognizer import get_instruction_type


def _get_code_position(content_list):
    for i in range(len(content_list)):
        if content_list[i] == "CODE:":
            return i

def isComment(element):
    if '///' in element:
        return 1


def get_code_content(content_list):
    cleanCode = []
    code_position = _get_code_position(content_list)
    commands = content_list[code_position + 1: len(content_list)]
    for elem in commands:
        if isComment(elem):
            pass
        else:
            cleanCode.append(elem)
    return cleanCode


def get_labels(code_content):
    labels = {}

    for i in range(len(code_content)):
        instruction = code_content[i]
        if ":" in instruction:
            label = instruction.replace(':', '')
            opcode = "00000000000000000000"  # nop
            direction = convert_str_to_bin(f"{i}")
            labels[label] = [direction, opcode]

    return labels


def get_instructions(code_line, labels):

    if not is_label(code_line):
        instruction_type = get_instruction_type(code_line)
        return instruction_type

           

        #else:  # no hay valor asociado, o sea se hace referencia a registros
        #    opcode = available_assembly_instructions.get_opcode(instruction_type)
        #   value = "0000000000000000"  # da igual que valor poner, solo hay que rellenar
        #    if '\n' in opcode:
        #        # significa que es una instrucción que se ejecuta en 2 ciclos (e.g. RET)
        #        opcode = opcode.split('\n')
        #        return opcode[0]+value+'\n'+opcode[1]+value  # 36 bits
        #    else:
        #        return opcode + value  # 36 bits
        return 'hola'


def has_an_associated_value(instruction_type):
    # Chequea si hay un valor asociado en la instrucción que ingresó el programador
    # o sea, si se hace referencia variables en RAM o a labels
    if '(Dir)' in instruction_type or 'Lit' in instruction_type:
        return True
    else:
        return False


def is_label(code_line):
    if code_line[-1] == ':':
        return True
    else:
        return False


def get_associated_value(code_line):
    pass
