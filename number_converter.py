
def convert_str_to_bin(value):
    # Evaluamos los values x dataType y los guardamos como binarios
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
