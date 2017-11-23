from random import *

def length_of_number(number):
    total = 0 
    while number > 0:
        total = total + 1
        number = number / 10
    return total

#print length_of_number(54456)



def check_credit_card(number):
    if length_of_number(number) != 16:
        return "invalid"
    
    number_length = 1
    total = 0.0
    while number > 0:
        number_length = number_length + 1
        last_number = number % 10
        if number_length % 2 == 0: #even
            total = total + last_number
        elif number_length % 2 == 1: #odd
            total = total + ((last_number * 2) / 10) + ((last_number * 2) % 10)
        number = number / 10
    if total % 10 == 0:
        return "valid"
    if total % 10 != 0:
        return "invalid"
        
#print check_credit_card(5424180123456789)

def create_credit_card():
    number = randint(1000000000000000, 9999999999999999)
    while check_credit_card(number) == "invalid":
        number = randint(1000, 9999)
    return number
print create_credit_card()


    
        




