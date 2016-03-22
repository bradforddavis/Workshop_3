# lower = 10
# upper = 100
#
# print("Enter a number.txt between {}-{}".format(lower, upper))

finished = False
result = 0
while not finished:
    try:
        result = input("Enter number: ")
        finished = True
    except ValueError:
        print("Please enter a valid integer")
print("valid result is", result)

