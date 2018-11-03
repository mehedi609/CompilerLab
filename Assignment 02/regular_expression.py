# Regular Expression for integer number
def integer_regex(reg_exp):
    if reg_exp[0] == '0':
        return f"{reg_exp}  -->  Not  Valid"
    else:
        for index, char in enumerate(reg_exp):
            if not reg_exp[index].isnumeric():
                return f"{reg_exp}  -->  Not  Valid"
        return f"{reg_exp}  -->  Valid"


def variable_regex(reg_exp):
    for index in range(len(reg_exp)):
        if reg_exp[0].isdigit():
            return f"{reg_exp} is not valid"
    return f"{reg_exp} is a valid expression"


# Regular Expression for integer number
while True:
    print('Press 1 for Integer Regex')
    print('Press 2 for Integer Regex')
    print('Press 3 for Integer Regex')
    print('Press 4 for Integer Regex')
    print('Press 5 for Integer Regex')
    print('Press 6 for Exit')

    user_choice = input('Enter your choice: ')
    if user_choice == '1':
        user_input = input('Enter a valid Integer-->  ')
        if len(user_input):
            if user_input[0] in ['+', '-']:
                print(user_input[0]+integer_regex(user_input[1:]))
                print('')
            else:
                print(integer_regex(user_input))
                print('')
        else:
            print('You did not enter anything')
            print('')

    elif user_choice == '2':
        pass

    elif user_choice == '3':
        pass

# Regular expression for variables
user_input = input('Enter a valid variable: ')
print(variable_regex(user_input))
