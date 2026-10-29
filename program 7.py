password = input("Enter a password: ")

if len(password) < 8:
    print("Failed: use at least 8 characters.")

if not any(letter.isupper() for letter in password):
    print("Failed: add an uppercase letter.")

if not any(letter.islower() for letter in password):
    print("Failed: add a lowercase letter.")

if not any(letter.isdigit() for letter in password):
    print("Failed: add a number.")

if "password" in password.lower():
    print("Failed: do not include the word 'password'.")

if "aaa" in password.lower():
    print("Failed: do not repeat 'a' three times.")

if (
    len(password) >= 8
    and any(letter.isupper() for letter in password)
    and any(letter.islower() for letter in password)
    and any(letter.isdigit() for letter in password)
    and "password" not in password.lower()
    and "aaa" not in password.lower()
):
    print("Password is valid.")
