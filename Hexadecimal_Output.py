def hex_output():
    dec_num = 0
    hex_num = input("Enter your number in base 10: ")
    for power, index in enumerate(reversed(hex_num)):
        dec_num += int(index, 16) * (16 ** power)
    print(f'Hex_output : {dec_num}')

hex_output()


def name_triangle():
    sec_num = str(0)
    nameee = input("Enter your name: ")
    for first, secondd in enumerate(nameee):
        for first, second in enumerate(nameee + secondd):
            sec_num += second
            print( sec_num , end="")
        print("")

name_triangle()

