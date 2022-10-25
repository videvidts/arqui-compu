from number_converter import convert_str_to_bin


def get_data_content(file_content):
    data = {}

    j = 0
    memory = 0

    # Poblar DATA
    while file_content[j] != 'CODE:':
        if file_content[j] != 'DATA:':
            # Si el value no es un string
            if "'" not in file_content[j] and '"' not in file_content[j]:
                if ' ' in file_content[j]:
                    label, value = file_content[j].split(' ')
                    value = convert_str_to_bin(value)
                    data[memory] = [label, value]
                    memory += 1
                else:
                    label, value = data[memory - 1]
                    value = convert_str_to_bin(file_content[j])
                    data[memory] = [label, value]
                    memory += 1

            # Si el value es un string
            else:
                label, value = file_content[j].split(' ', 1)
                value = value.replace("'", "")
                value = ''.join(format(ord(i), '08b') for i in value)
                data[memory] = [label, value]
                memory += 1
        j += 1

    return data
