from random import randint



def guessing_game():

    name =  input("What is your name? ")
    print (f'Hello, {name}')

    while True:
        number = randint(0,10)

        user_num = int(input('Guess this number: '))
        
        if number == user_num:
            print("Good, you got it! ")
            break
        elif number < user_num:
            print("Too high")
        elif number > user_num:
            print("Too low")
        else:
            print('Enter a vlid number! ')


guessing_game()