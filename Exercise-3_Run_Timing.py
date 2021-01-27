# def run_timing():

#     number_of_runs = 0
#     total_time = 0

#     while True:

#         num = input('Enter 10km run time: ')
        
#         if not num:
#             break

#         number_of_runs += 1
#         total_time += float(num)

        
#     average_time = total_time/ number_of_runs
#     print(f'Average is {average_time}, over {number_of_runs} runs')

# run_timing()


def float_function():
    fl = float(input("Enter your float: "))
    before = int(input("Enter a before: "))
    #after = int(input("Enter a after"))

    print(f'The number is {fl:.2f} ')
    print(round(fl,before))

    return f'{fl:.2f}'


float_function()