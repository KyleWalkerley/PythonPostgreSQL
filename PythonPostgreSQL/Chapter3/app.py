from database import add_entry, get_entries

menu = """ Please select one of the folowing options:
1) Add new entry for today.
2) View enteries.
3) Exit.

Your selection:"""

Welcome = "Welcome to the programing diary!"

def prompt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date:")

    add_entry(entry_content, entry_date) 

def view_entries(entries):
    for entry in entries:
            print(f"{entry['date']}\n{entry['content']}\n\n")

print(Welcome)

user_input = input(menu)
while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_entry()

    elif user_input == "2":
        view_entries(get_entries())

    else:
        print("Invalid option, please try again!")

