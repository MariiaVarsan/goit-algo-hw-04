def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Проверка на ввод имени корректно (буквами)
def validate_name(name):
    try:
        if not name.isalpha():
            return "Invalid name: Name must contain only letters."
        if len(name) <= 1:
            return "Invalid name: name must contain more than 2 letters."
    except Exception as e:
        return f"Error: {e}"


# Проверка на ввод номера корректно (цифрами) + кол-во
def validate_phone(phone):
    try:
        if not phone.isdigit():
            return "Invalid phone number: Phone number must contain only digits."
        if len(phone) <= 9:
            return "Invalid phone number: The phone number must contain more than 10 digits."
    except Exception as e:
        return f"Error: {e}"


# Добавление имени и номера
def add_contact(args, contacts):
    try:
        name, phone = args
        error_name = validate_name(name)
        if error_name:
            return error_name
        error_phone = validate_phone(phone)
        if error_phone:
            return error_phone
        contacts[name] = phone
        return "Contact added."
    except Exception as e:
        return f"Error: {e}"


# Смена номера
def change_contact(args, contacts):
    try:
        name, phone = args
        error_name = validate_name(name)
        if error_name:
            return error_name
        error_phone = validate_phone(phone)
        if error_phone:
            return error_phone
        if name in contacts:
            contacts[name] = phone
            return "Contact updated"
        else:
            return "Error: Contact not found"
    except Exception as e:
        return f"Error: {e}"


# Показ номера
def show_phone(args, contacts):
    try:
        name = args[0]
        error_name = validate_name(name)
        if error_name:
            return error_name
        if name in contacts:
            return f"The phone number for {name} is {contacts[name]}"
        else:
            return "Error: Contact not found"
    except Exception as e:
        return f"Error: {e}"


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
            # print(contacts)
        elif command == "change":
            print(change_contact(args, contacts))
            # print(contacts)
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
