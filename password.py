pw = input("What would you like you password to be? ")

valid_password = False

MIN_UPPER = 1
MIN_LOWER = 1
MIN_NUMBER = 1
MIN_SPEC = 1

while not valid_password:
    lowerCase = len([c for c in pw if c.islower()])
    upperCase = len([c for c in pw if c.isupper()])
    number = len([c for c in pw if c.isdigit()])
    special = len([c for c in "!@#$%^&*()_+-={}[];':,./<>?\|"])

    if len(pw) < 5 or len(pw) > 15 or lowerCase < MIN_LOWER or upperCase < MIN_UPPER or number < MIN_NUMBER or special < MIN_SPEC:
        print("Please enter a valid password \n Your password must be between 5 and 15 characters and contain: \n\t 1 or more uppercase characters \n\t 1 or more lowercase characters \n\t 1 or more numbers \n\t and 1 or more special charcaters: !@#$%^&*()_-+=`~,.\/'[]<>?{}|")
        pw = input("What would you like you password to be? ")
    else:
        valid_password = True

print('Your {} character password is valid: {}'.format(len(pw), pw))
