def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

def show_phone(args, contacts):
    name = args[0]  # Тільки перший аргумент, ім'я
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact with name '{name}' not found."
def show_all(args, contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts found.")
        
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            if args:  # Перевіряємо, чи є аргумент
                print(show_phone(args, contacts))
            else:
                print("Please provide a name after 'phone'.")
        elif command == "all":
            print(show_all(args, contacts))      
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()
