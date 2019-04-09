
password_lessthan8 = "Draper1"
password_nonumber = "Draperuniversity"
password_nocapital = "draperuniversity1"
password_withspace = "Draper University1"
password_valid = "Draperuniversity1"

import re

def validate(password):
        if len(password) < 8:
            print("Make sure your password is at least 8 letters.", password)
        elif re.search('[0-9]', password) is None:
            print("Make sure your password has a number in it.", password)
        elif re.search('[A-Z]', password) is None: 
            print("Make sure your password has a capital letter in it.", password)
        else:
            print("Your password seems fine.", password)

password_list = [password_lessthan8, password_nonumber, password_nocapital, password_withspace, password_valid]
for n in password_list:
    validate(n)
