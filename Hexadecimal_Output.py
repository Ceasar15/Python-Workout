# def hex_output():
#     dec_num = 0
#     hex_num = input("Enter your number in base 10: ")
#     for power, index in enumerate(reversed(hex_num)):
#         dec_num += int(index, 16) * (16 ** power)
#     print(f'Hex_output : {dec_num}')

# hex_output()


def name_triangle():
    nameee = input("Enter your name: ")
    for first, second in enumerate(reversed(nameee)):
        second += second
        print(str(second))
        # print(f'{first}, {second}') 

name_triangle()
