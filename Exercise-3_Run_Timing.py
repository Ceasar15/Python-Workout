def run_timing():

    number_of_runs = 0
    total_time = 0

    while True:
        try:
            num = float(input('Enter a number: '))
            print(f'{num}')
            if not num:
                break
            number_of_runs += 1
            total_time += float(num)
        except ValueError:
            print('That no be good value! ')
        
    average_time = total_time/ number_of_runs
    print