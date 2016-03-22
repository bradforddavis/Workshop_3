def main():
    valid_input = False
    while not valid_input:
        try:
            age = int(input('Age: '))
            if age < 0:
                print('Invald (must be above 0')
            else:
                valid_input = True
        except ValueError:
            print('Invalid (not an integer)')
    print('Next year you weill be', add_one_to(age))

def add_one_to(value): #function
    return value + 1

if __name__ == '__main__':
    main()

# def celsius_to_fahrenheit(celcius):
#     return celcius * 1.8 + 32
