menu = """ Please select one of the folowing options:
1) Add new entry for today.
2) View enteries.
3) Exit.

Your selection:"""

Welcome = "Welcome to the programing diary!"

print(Welcome)

user_input = input(menu)
while (user_input := input(menu)) != "3":
    if user_input == "1":
        print("Adding...")
    elif user_input == "2":
        print("Viewing...")
    else:
        print("Invalid option, please try again!")

