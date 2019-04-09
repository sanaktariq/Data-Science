#This code is to make a form for a website.

#input("Welcome to the signup form.")

name_with_space = "Sana T"
name = "Sana"
name_integer = "sana1"

def is_name_valid(name):

    if all(x.isalpha() or x == ' ' for x in name):
        print("is a valid name" , name)
    else:
        print("Invalid Entry", name)

namelist = [name, name_integer, name_with_space] 
for n in namelist: 
    is_name_valid(n)




