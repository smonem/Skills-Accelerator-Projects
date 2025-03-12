# Password Strength Checker

psw = input("Enter password: ")
psw_strong = True
fail = "Your password needs at least"


# Constructs input with correct punctuation
def punct(check_str):
    if check_str[-1] == " ":
        check_str = check_str.strip() + ","
    return check_str

# Check validity
if len(psw) < 8:
    fail += " 8 characters "
    psw_strong = False
if not any(c.isdigit() for c in psw):
    fail = punct(fail)
    fail += " one digit "
    psw_strong = False
if not any(c.isupper() for c in psw):
    fail = punct(fail)
    fail += " one uppercase letter "
    psw_strong = False
if not any(c.islower() for c in psw):
    fail = punct(fail)
    fail += " one lowercase letter "
    psw_strong = False
if not any(not c.isalnum() for c in psw):
    fail = punct(fail)
    fail += " one special character "
    psw_strong = False

# Print result
if psw_strong:
    print("Your password is strong! 💪")
else:
    fail = fail.strip()
    fail = ", and".join(fail.rsplit(",", 1))
    fail += "."
    print(fail)
