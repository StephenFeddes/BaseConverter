# Author: Stephen Feddes


def num_validate(statement, lower, upper):
    while True:
        try:
            reply = int(input(statement))
            if type(reply) == int and reply >= lower and reply <= upper:
                return reply
            else:
                print("Invalid input, try again.")
        except:
            print("Invalid input, try again.")
            continue

def answer_validate(statement):
    while True:
        reply = input(statement)
        answer = reply[0].lower()
        if answer == 'y' or answer == 'n':
            return answer
        else:
            print("Invalid input")

def base_converter(num, current_base, new_base, precision):
    

    if num == "0": # Instant answer for the simple input of 0
        print(f"{num} in base {current_base} is 0 in base {new_base}")
        return "0"

    sign = ""
    
    # Makes sure every number is positive a floating-point number so that the algorithms are consistent
    if num[0] == "-":
        num = num.replace("-","")
        sign = "-" 
    if not "." in num:
        num = num + ".0"
    if num[-1] == ".":
        num = num + "0"
    
    from decimal import Decimal # This function corrects float errors
    # Dictionary for character to number/number to character conversions
    import string
    alphabet = string.ascii_uppercase 
    str_to_int = {"":0, 0:"0", "0":0, "1":1,"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "36":36, "36":36}
    for l in alphabet:
        str_to_int.update({l:10+alphabet.index(l)}) # Fills dictionary with letter:number pairings
    for l in alphabet:
        str_to_int.update({str(10+alphabet.index(l)):l}) # Fills dictionary with number:letter pairings
        
    if (current_base > 36 or current_base < 2) or (new_base > 36 or new_base < 2):
            print("Base values are limited to 2-36")
            return None # Guarantees the bases have a minimum value of 2 and a maximum of 35
    
    # Check for common mistakes
    acceptable_num_characters = alphabet+"0123456789"
    for x in num.replace(".",""):
        if not x in acceptable_num_characters:
            print("numbers can only use alphanumeric characters.")
            return None
        elif str_to_int[x] > current_base-1:
            print(f"This number's digits are larger than the base allows. Digits must between 0 and {current_base-1}")
            return None

   # Now that the numbers have been checked, the next lines of code can do the actual converting

    num_split = num.split(".") # Splits number into it's whole and fractional components
    whole_current_base = num_split[0] # Whole part in current base
    num_frac_current = num_split[1] # Fractional part in current base
    num_frac_ten = 0 # Initial value for algorithm that converts a number's fractional part in the current base to base 10
    whole_base_ten = 0 # Initial value for algorithm that converts a number's whole part in the current base to base 10
    
    
    # Converts a whole number in some base to base ten
    i = 0
    for x in whole_current_base[::-1]:
        whole_base_ten = whole_base_ten + (str_to_int[x]*(current_base**i))
        i += 1
    
    # Prequesite values for next algorithm that converts a number's whole part from base ten to the new base
    quotient = whole_base_ten
    conv_order = []

    # Algorithm for converting a number's whole part in base ten to the new base
    while quotient != 0:
        remainder = quotient%new_base
        quotient = quotient//new_base
        conv_order.append(str(str_to_int[str(remainder)]))
    conv_order = conv_order[::-1]

    if len(conv_order) == 0: # To things consistent, a number like .8 must become 0.8
       conv_order.append("0")

    i =- 1
    for x in num_frac_current: # Converts a fractional part of a number to base 10
        num_frac_ten = num_frac_ten + str_to_int[x]*(current_base**i)
        i -= 1

    # Prequesite values for next algorithm
    product = num_frac_ten*new_base
    frac_conv_order = []
    product_split = str(product).split(".") 
    try:
        product_frac = product_split[1]
    except:
        product_split.insert(0, 0) # if product_split doesn't split, then the whole number part should become 0 so that it can split
        product_frac = product_split[1]
    j = 0

    # Algorithm for converting the fractional part of a base ten number to a new base
    while (product_frac != 0 and product != 1) and precision-(j-1) > 0 and precision != 0:
        product = 10 # This is for the loop to stop checking if product does not equal 1, as we only want it to check once
        conv = product_split[0]
        # Sometimes I get a number like 0E-8, which breaks the code. That's why I have try statements
        try:
            frac_conv_order.append(str((str_to_int[str(conv)])))
        except:
            pass
        try:
            product_frac = Decimal("."+ product_split[1])
        except:
            product_frac = 0
        product_split = str(Decimal(product_frac*new_base)).split(".")
        j+=1
    # Situation where fractional conversion doesn't need looping
    if len(frac_conv_order) == 0:
        frac_conv_order.append(str(str_to_int[str(int((Decimal(num_frac_ten*new_base))))]))

    
    # Next lines of code handle rounding    

    if precision == 0 and int(str_to_int[frac_conv_order[0]]) >= new_base/2:
        conv_order[-1] = str(str_to_int[str(int(str_to_int[conv_order[-1]]) + 1)])
    
    if precision == 0:
        frac_conv_order.clear()
        frac_conv_order.append("0")

    if int(str_to_int[frac_conv_order[-1]]) >= new_base/2 and len(frac_conv_order) > 1 and product_frac != 0:
        frac_conv_order[-2] = str(str_to_int[str(int(str_to_int[frac_conv_order[-2]]) + 1)])
        frac_conv_order.pop() # Removes the digit that went beyond our desired precision level so that we could round
    elif len(frac_conv_order) > 1 and product_frac != 0:
        frac_conv_order.pop()

    # The following lines of code handle the carries caused due to rounding
    i = 1
    while i < len(frac_conv_order):
        if int(str_to_int[frac_conv_order[-i]]) >= new_base:
            frac_conv_order[-i] = "0"
            frac_conv_order[-i-1] = str(str_to_int[str(int(str_to_int[frac_conv_order[-i-1]]) + 1)])
        i+=1
    
    if int(str_to_int[frac_conv_order[0]]) >= new_base:
        frac_conv_order[0] = "0"
        conv_order[-1] = str(str_to_int[str(int(str_to_int[conv_order[-1]]) + 1)])
    i = 1

    if int(str_to_int[conv_order[0]]) >= new_base:
        conv_order[0] = "0"
        conv_order = ["1"] + conv_order  
    
    # This code converts all the zeros that occur before the first number, e.g. 0008 becomes 8
    i = 0
    p = ""
    if len(conv_order) != 0 and not (len(conv_order) == 1 and conv_order[0] == "0"):
        while True:
            if int(str_to_int[conv_order[i]]) != 0:
                conv_order.insert(0, p)
                break
            else:
                p = conv_order.pop(0)
                i+=1
    
    # The rest of the code puts all the results together to print out the new number
    total_conv_order = conv_order + ["."] + frac_conv_order
    new_num = "".join(total_conv_order)

    new_num = sign + new_num
    print(f"{sign+num} in base {current_base} is {new_num} in base {new_base}")
    return new_num
