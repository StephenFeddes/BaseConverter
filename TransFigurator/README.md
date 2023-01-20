# Project: TransFigurator
# Creator: Stephen Feddes
# Contact Info: stephenpfeddes@lewisu.edu or feddessteve@gmail.com
# All code is original, unless you count the string/Decimal libaries
## I originally planned for it to just be a base-converter function with a default precision of 10 places, without any rounding, and no user input. 
## I delivered more than originally planned. In my first plan, during sprint 4, I did not want to add user input or implement rounding. For my final version, I added user input, customizable precision, and rounding.
## If I had more time, I think making a website for my program would have been neat. The most important thing I would have done, however, would have been to increase the level of precision. I had to keep it at 9 places because, based on evidence I found while testing the accuracy of my converter, it can get slightly inaccurate after 9 places because of Python's own rounding. For example, 1/3 * 8 would be like 2.666666666667 in Python. I would've searched hard for a way to make Python's rounding more precise.

## This program takes any number in base 2-36 and converts it to any base 2-36, with a degree of precision between 0 and 9 places.
## To execute the program, make sure base_converter.py and transfigurator.py are stored in the same folder. The program is to be run in transfigurator.py.
