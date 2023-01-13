import random


def main():
    computer_guess_number = random.randint(1, 10)
    guess_number_count = 0
    wrong_data_entry = 0
    while guess_number_count < 3 and wrong_data_entry < 3:
        print(f'''
--------------------------------------------
You Enter Wrong Ans {wrong_data_entry} this many times!!!
--------------------------------------------
        you have {3-guess_number_count} chance
--------------------------------------------
''')

        user_guess_number = input('enter number to guess(between 1-10): ')
        if user_guess_number.isdigit():
            guess_number_count += 1
            user_guess_number = int(user_guess_number)
            if user_guess_number == computer_guess_number:
                print(f"You win!! the number is {computer_guess_number}")
                break
            elif user_guess_number < 3 and user_guess_number != computer_guess_number:
                print(
                    f"\nEnter number {user_guess_number} is not a computer guess number.\nenter again")
                wrong_data_entry += 1
                pass

        elif wrong_data_entry < 2:
            print('''
****************************
Wrong input data try again..
****************************
''')
            wrong_data_entry += 1
        else:
            print("Too many Wrong input!!")
            break
    else:
        print(f'You FAILD.The Right answer is {computer_guess_number}')


main()
