#Salesi Ilaoa, Period 1, Password strength checker assignment

# Get password from the user
password = input("Enter a password: ")
passed_checks = 0

# Check each criterion
if len(password) >= 8:
    passed_checks += 1
if any(char.isupper() for char in password):
    passed_checks += 1
if any(char.islower() for char in password):
    passed_checks += 1
if any(char.isdigit() for char in password):
    passed_checks += 1
if any(not char.isalnum() for char in password):
    passed_checks += 1

# Keep asking until the password passes at least one check
while passed_checks == 0:
    print("Password too weak, try again")
    password = input("Enter a password: ")
    passed_checks = 0
    if len(password) >= 8:
        passed_checks += 1
    if any(char.isupper() for char in password):
        passed_checks += 1
    if any(char.islower() for char in password):
        passed_checks += 1
    if any(char.isdigit() for char in password):
        passed_checks += 1
    if any(not char.isalnum() for char in password):
        passed_checks += 1

# Give feedback based on the score
if passed_checks == 1 or passed_checks == 2:
    print("WEAK")
elif passed_checks == 3:
    print("MODERATE")
elif passed_checks == 4:
    print("STRONG")
else:
    print("VERY STRONG")