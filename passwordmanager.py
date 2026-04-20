import random
import string

passwords = {}

# Load existing passwords
try:
    with open("password.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except FileNotFoundError:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "@#$%!&"
    return "".join(random.choice(chars) for _ in range(10))

while True:
    print("\n---- PASSWORD MANAGER ----")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter your website: ")
        pwd = input("Enter your password: ")
        passwords[site] = pwd

        with open("password.txt", "a") as file:
            file.write(site + ":" + pwd + "\n")

        print("Saved")

    elif choice == "2":
        if not passwords:
            print("No Data")
        else:
            for site, pwd in passwords.items():
                print(site + ":" + pwd)

    elif choice == "3":
        print("Generated Password:", generate_password())

    elif choice == "4":
        print("Exit")
        break

    else:
        print("Invalid Choice")