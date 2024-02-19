import re

def assess_password_strength(password):
    pass
    min_length = 8
    must_contain_lowercase = re.search(r'[a-z]', password)
    must_contain_uppercase = re.search(r'[A-Z]', password)
    must_contain_digit = re.search(r'\d', password)
    must_contain_special_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    if len(password) <8:
        print("Password must be at least 8 characters long.\n")
    elif not re.search("[A-Z]",password):
        print("Password must contain at least one uppercase letter.\n")
    elif not re.search("[a-z]",password):
        print("Password must contain at least one lowercase letter.\n")
    elif not re.search("[0-9]",password):
        print("Password must contain at least one numeric character.\n")
    elif not re.search("[!@#$%^&*?]",password):
        print("Pasword must contain at least 1 special character\n")

    
    strength_score = 0    
    if len(password)>= min_length:
        strength_score += 1
    if must_contain_lowercase:
        strength_score += 1
    if must_contain_uppercase:
        strength_score += 1
    if must_contain_digit:
        strength_score += 1
    if must_contain_special_char:
        strength_score += 1

    
    if min_length and must_contain_lowercase and must_contain_uppercase and must_contain_digit and must_contain_special_char:
        print("Strong password")
    else:
        print("Weak password")

password = input("Enter your password: ")
result = assess_password_strength(password)

