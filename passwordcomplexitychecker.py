import re

def check_password_complexity(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Your password is strong!"
    else:
        feedback = "Your password is weak. To improve, consider the following:\n"
        if not length_criteria:
            feedback += "- Make sure the password is at least 8 characters long\n"
        if not uppercase_criteria:
            feedback += "- Add at least one uppercase letter\n"
        if not lowercase_criteria:
            feedback += "- Add at least one lowercase letter\n"
        if not digit_criteria:
            feedback += "- Add at least one number\n"
        if not special_char_criteria:
            feedback += "- Add at least one special character (!@#$%^&*(),.?\":{}|<>)\n"

        return feedback

def main():
    print("PASSWORD COMPLEXITY CHECKER")
    password = input("Please enter your password: ")
    result = check_password_complexity(password)
    print(result)

if __name__ == "__main__":
    main()
