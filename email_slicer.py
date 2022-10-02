

user_input = input("Enter your emain: ").lower()


def email_slicer():
    for i in range(len(user_input)):
        if user_input[i] == '@':
            username  = user_input[:user_input.index('@')]
        else:
            domain = user_input[user_input.index('@') + 1:]

    print(f'Your user Name is {username} and domain is {domain}')


email_slicer()

