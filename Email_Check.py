email_with_space = "sana tariq@gmail.com"
email = "sanatariq@gmail.com"
email_missingat = "sanatariqgmail.com"

import re

def is_email_valid(email):
    if re.match(r'[^@]+@[^@]+\.[^@]+', email):
        print("Valid email", email)
    elif ' ' in email == True:
        print("Invalid email", email)
    else:
        print("Invalid email", email)
        
email_list = [email_with_space, email, email_missingat] 
for n in email_list: 
    is_email_valid(n)
