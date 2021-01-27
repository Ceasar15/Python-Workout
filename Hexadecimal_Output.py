def hex_output():
    dec_num = 0
    hex_num = input("Enter your hex number: ")
    for power, index in enumerate(reversed(hex_num)):
        dec_num += int(index, 16) * (16 ** power)
    print(f'Hex_output : {hex_num}')

hex_output()