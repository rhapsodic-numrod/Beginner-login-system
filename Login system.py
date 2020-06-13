import csv
from csv import DictReader

# ask user if they have an existing account account
existing_account = input("Do you have an existing account? (yes/ no): ")

while True:
    # if user has an account user should enter email/username and password. user must receive a greetin
    if existing_account.lower() == "yes":
        print("--LOGIN--")
        existing_user_id = input("Enter your username: ")

        while True:
            existing_password = input("Enter your password: ")

            if len(existing_password) < 8:
                print("Password too short")
                continue

            elif len(existing_password) > 35:
                print("Password too long")
                continue

            elif not existing_password.isalnum():
                print("Password must be alphanumerical")
                continue
            # check if password/account exist in the system

            else:
                with open("user_data.csv", "r") as read_obj:
                    csv_reader = DictReader(read_obj)
                    for row in csv_reader:
                        if row["Username"] == existing_user_id and row["Password"] == existing_password:
                            print("Valid password")
                            print("Welcome back %s, it's been a while" % existing_user_id)
                            break
                        else:
                            print("Password or username is incorrect try again")
                continue

        break

    # if user does not have an account they should create an account by giving their name, email, username and password.  user must receive a greeting

    elif existing_account.lower() == "no":
        print("--CREATE NEW ACCOUNT--")
        name = input("Enter your name: ")
        # check email if it has a @ to see if it is a real email
        while True:
            email = input("Enter your email adress:  ")
            if "@" not in email:
                print("Invalid, email must contain '@' ")
                continue
            else:
                print("Valid email")
                break

        new_user_id = input("Enter your username: ")

        # check if password meets all criteria of length, simialarity and if it is alphanumerical
        while True:
            new_password = input(
                "Enter a password between 8 to 35(must be alphanumerical): ")
            new_password2 = input("Enter your password again: ")

            if new_password != new_password2:
                print("Passwords do not match")
                continue

            elif len(new_password) < 8:
                print("Password too short")
                continue

            elif len(new_password) > 35:
                print("Password too long")
                continue

            elif not new_password.isalnum():
                print("Password must be alphanumerical")
                continue

            else:
                # add username and password to user_data file
                with open("user_data.csv", "a", newline="\n") as csv_file:
                    fieldnames = ["username", "password"]
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writerow(
                        {'username': new_user_id, 'password': new_password})

                    csv_file.close()

                print("Valid password")
                print("Welcome %s, its good to meet you" % new_user_id)
                break
        break
