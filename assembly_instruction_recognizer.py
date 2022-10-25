
def get_instruction_type(full_instruction):
    # full_instruction es una instrucción en assembly limpia (e.g. "MOV A,(variable2)")
    # por lo tanto no se deben introducir labels (e.g. fin:) a la función
    # OJO: este código NO detecta código assembly inválido, hay muchos casos no comprobados.
    # Solo clasifica código válido (osea que existe esa instrucción en el assembly del compu. básico)

    full_instruction_list = full_instruction.split(' ')
    if len(full_instruction_list) == 1:
        full_instruction_list.insert(1, "")

    # ["MOV", "A,(variable2)"]
    instruction = full_instruction_list[0]
    parameters = full_instruction_list[1]

    # reconocimiento
    if instruction == "MOV":
        return _get_mov_type(instruction, parameters)

    elif instruction == "ADD" or instruction == "SUB" or instruction == "AND" \
            or instruction == "OR" or instruction == "XOR":
        return _get_add_sub_and_or_xor_type(instruction, parameters)

    elif instruction == "NOT" or instruction == "SHL" or instruction == "SHR":
        return _get_not_shl_shr_type(instruction, parameters)

    elif instruction == "INC":
        return _get_inc_type(instruction, parameters)

    elif instruction == "DEC":
        return _get_dec_type(instruction, parameters)

    elif instruction == "CMP":
        return _get_cmp_type(instruction, parameters)

    elif instruction == "JMP" or instruction == "JEQ" or instruction == "JNE" or \
            instruction == "JGT" or instruction == "JLT" or instruction == "JGE" or \
            instruction == "JLE" or instruction == "JCR" or instruction == "CALL":
        return _get_jxx_call_type(instruction, parameters)

    elif instruction == "RET":
        return _get_ret_type(instruction, parameters)

    elif instruction == "PUSH" or instruction == "POP":
        return _get_push_pop_type(instruction, parameters)

    elif instruction == "NOP":
        return "NOP"

    else:
        print("1 --error para instruccion" + instruction)


def _has_parenthesis(text):
    if '(' in text or ')' in text:
        return True
    else:
        return False


def _has_comma(text):
    if ',' in text:
        return True
    else:
        return False


def _get_add_sub_and_or_xor_type(instruction, parameters):
    if _has_comma(parameters):
        first_param = parameters.split(',')[0]
        second_param = parameters.split(',')[1]
        if first_param == 'A':
            if second_param == 'B':
                return f"{instruction} A,B"
            elif second_param == '(B)':
                return f"{instruction} A,(B)"
            elif _has_parenthesis(second_param):
                return f"{instruction} A,(Dir)"
            else:
                return f"{instruction} A,Lit"
        elif first_param == 'B':
            if second_param == 'A':
                return f"{instruction} B,A"
            elif second_param == '(B)':
                return f"{instruction} B,(B)"
            elif _has_parenthesis(second_param):
                return f"{instruction} B,(Dir)"
            else:
                return f"{instruction} B,Lit"
        else:
            print("2 --error para instruccion" + instruction)
    elif _has_parenthesis(parameters):
        return f"{instruction} (Dir)"
    else:
        print("3 --error para instruccion" + instruction)


def _get_mov_type(instruction, parameters):
    first_param = parameters.split(',')[0]
    second_param = parameters.split(',')[1]
    if first_param == 'A':
        if second_param == 'B':
            return "MOV A,B"
        elif second_param == '(B)':
            return 'MOV A,(B)'
        elif _has_parenthesis(second_param):
            return "MOV A,(Dir)"
        else:
            return "MOV A,Lit"
    elif first_param == 'B':
        if second_param == 'A':
            return "MOV B,A"
        elif second_param == '(B)':
            return "MOV B,(B)"
        elif _has_parenthesis(second_param):
            return "MOV B,(Dir)"
        else:
            return "MOV B,Lit"
    elif first_param == '(B)':
        if second_param == 'A':
            return "MOV (B),A"
        else:
            return "MOV (B),Lit"
    elif _has_parenthesis(first_param):
        if second_param == 'A':
            return "MOV (Dir),A"
        elif second_param == 'B':
            return "MOV (Dir),B"
        else:
            print("4 --error para instruccion" + instruction)
    else:
        print("5 --error para instruccion" + instruction)


def _get_not_shl_shr_type(instruction, parameters):
    if _has_comma(parameters):
        first_param = parameters.split(',')[0]
        second_param = parameters.split(',')[1]
        if first_param == 'B' and second_param == 'A':
            return f"{instruction} B,A"
        elif first_param == '(B)' and second_param == 'A':
            return f"{instruction} (B),A"
        elif _has_parenthesis(first_param) and second_param == 'A':
            return f"{instruction} (Dir),A"
        else:
            print("6 --error para instruccion" + instruction)
    elif parameters == 'A':
        return f"{instruction} A"
    else:
        print("7 --error para instruccion" + instruction)


def _get_inc_type(instruction, parameters):
    if parameters == 'A':
        return f"{instruction} A"
    elif parameters == 'B':
        return f"{instruction} B"
    elif parameters == '(B)':
        return f"{instruction} (B)"
    elif _has_parenthesis(parameters):
        return f"{instruction} (Dir)"
    else:
        print("8 --error para instruccion" + instruction)


def _get_dec_type(instruction, parameters):
    if parameters == 'A':
        return f"{instruction} A"
    else:
        print("9 --error para instruccion" + instruction)


def _get_cmp_type(instruction, parameters):
    first_param = parameters.split(',')[0]
    second_param = parameters.split(',')[1]
    if first_param == 'A':
        if second_param == 'B':
            return f"{instruction} A,B"
        elif second_param == '(B)':
            return f"{instruction} A,(B)"
        elif _has_parenthesis(second_param):
            return f"{instruction} A,(Dir)"
        else:
            return f"{instruction} A,Lit"
    else:
        print("10 --error para instruccion" + instruction)


def _get_jxx_call_type(instruction, parameters):
    return f"{instruction} Ins"


def _get_ret_type(instruction, parameters):
    if parameters == '':
        return f"{instruction}"
    else:
        print("12 --error para instruccion" + instruction)


def _get_push_pop_type(instruction, parameters):
    if parameters == 'A':
        return f"{instruction} A"
    elif parameters == 'B':
        return f"{instruction} B"
    else:
        print("13 --error para instruccion" + instruction)
