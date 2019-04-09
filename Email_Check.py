email_with_space = "sana tariq@gmail.com"
email = "sanatariq@gmail.com"
email_missingat = "sanatariqgmail.com"

import re

def is_email_valid(email):
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        print("Invalid email - no @ symbol:", email)
    elif (' ' in email):
        print("Invalid email - has space:", email)
    else:
        print("Valid email:", email)
        
email_list = [email_with_space, email, email_missingat] 
for n in email_list: 
    is_email_valid(n)
