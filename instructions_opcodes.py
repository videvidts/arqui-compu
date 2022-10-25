
from collections import defaultdict

def load_assembly_instructions(path):
    instructions_dict = {}

    with open(path) as file:
        lines = file.readlines()
        for i in range(len(lines) - 1):
            this_line_list = lines[i].strip('\n').replace('\t', ' ').split(' ')

            command = this_line_list[0]
            parameters = this_line_list[1]
            if command != 'RET' and command != '':
                opcode = this_line_list[2]
            else:
                opcode = this_line_list[1]


            if command not in instructions_dict.keys():
                instructions_dict[command] = {}
            else:
                instructions_dict[command][parameters] = opcode

    return AvailableAssemblyInstructions(instructions_dict)


class AvailableAssemblyInstructions:

    def __init__(self, instructions_list):
        self.instructions_list = instructions_list

    def get_opcode(self, given_instruction):
        for instruction in self.instructions_list:
            str_instruction = instruction[0] + ' ' + instruction[1]
            if str_instruction.strip() == given_instruction:
                return instruction[-1]

    def __str__(self):
        return repr(self.instructions_list)


# print(load_assembly_instructions("CPU - instructions_opcodes.tsv"))
