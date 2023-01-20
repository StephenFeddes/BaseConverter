# Author: Stephen Feddes

from base_converter import num_validate
from base_converter import base_converter
from base_converter import answer_validate

print("**********************************")
print("         TransFigurator           ")
print("**********************************")
print("")
print("This program will take any number in")
print("base 2-36 and convert it to any base")
print("2-36, with a customizable degree of \nprecision")
print("")
print("Begin.")

while True:
    current_base = num_validate("Enter your current base, 2-36: ", 2, 36)
    new_base  = num_validate("Now, enter the base you want to convert to, 2-36: ", 2, 36)
    precision = num_validate("Enter the desired digits of precision, 0-9: ", 0, 9)
    while True:
        num = input("Enter a number in the current base: ").upper()
        if num.count(".") > 1:
            print("A number can only have one radix point.")
            continue
        try:
            check = base_converter(num, current_base, new_base, precision)
        except:
            print("Invalid input, try again")
            continue
        if check == None:
            continue
        else:
            break
    answer = answer_validate("Do you want to run this program again? Enter 'y' or 'n': ")

    if answer == 'y':
        print("")
        print("----------------------------------")
        print("")
        continue
    else:
        break
    