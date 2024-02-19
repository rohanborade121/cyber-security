#password strength checker
import re 

#Password must be at least 8 characters
password = input("Enter Your Password:\n")
if len(password) < 8:
    print("Password must be at least 8 characters long.\n")
#Password must contain at least 1 uppercase letter
elif not re.search("[A-Z]",password):
    print("Password must contain at least one uppercase letter.\n")
#Password must contain at least 1 lowercase letter
elif not re.search("[a-z]",password):
    print("Password must contain at least one lowercase letter.\n")
#Password must contain at least 1 number letter
elif not re.search("[0-9]",password):
    print("Password must contain at least one number.\n")
#Pssword must contain at least 1 special character
elif not re.search("[!@#$%^&*?]",password):
    print("Pasword must contain at least 1 special character\n")
else:
    print("Password is strong.\n")