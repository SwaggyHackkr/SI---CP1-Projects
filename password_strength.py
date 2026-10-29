#Salesi Ilaoa, Period 1, Password strength checker assignment

while True:
    password = input("Enter a password: ")

    # Check each criterion and keep track of which ones pass
    length_ok = len(password) >= 8
    upper_ok = any(char.isupper() for char in password)
    lower_ok = any(char.islower() for char in password)
    number_ok = any(char.isdigit() for char in password)
    special_ok = any(not char.isalnum() for char in password)

    passed_checks = (length_ok + upper_ok + lower_ok
                     + number_ok + special_ok)

    # Show the user exactly which checks passed or failed
    print("Password strength assessment:")
    print(f"  Length (8+ characters):     {"Yes" if length_ok else "No"}")
    print(f"  Contains uppercase:         {"Yes" if upper_ok else "No"}")
    print(f"  Contains lowercase:         {"Yes" if lower_ok else "No"}")
    print(f"  Contains numbers:           {"Yes" if number_ok else "No"}")
    print(f"  Contains special characters: {"Yes" if special_ok else "No"}")

    # Reject anything below Moderate instead of accepting weak passwords
    if passed_checks < 3:
        print("Password too weak (needs at least 3/5 checks), try again.")
        continue

    # Give feedback based on the score
    if passed_checks == 3:
        strength = "Moderate"
    elif passed_checks == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print(f"Strength score: {passed_checks}/5")
    print(f"Password strength: {strength}")
    break

