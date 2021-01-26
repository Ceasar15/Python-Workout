def run_timing():

    number_of_runs = 0
    total_time = 0

    while True:

        num = input('Enter 10km run time: ')
        
        if not num:
            break

        number_of_runs += 1
        total_time += float(num)

        
    average_time = total_time/ number_of_runs
    print(f'Average is {average_time}, over {number_of_runs} runs')

run_timing()

