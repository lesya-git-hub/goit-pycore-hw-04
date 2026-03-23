# Напишіть консольного бота помічника, який повинен вміти працювати з книгою контактів та календарем.
import os
import re
from colorama import Fore, Style

# 1. Зберігання даних 
def save_data(contacts):
    with open("contact_list.txt", "w", encoding="utf-8") as file:
        for name, phone in contacts.items():
            file.write(f"{name}:{phone}\n")

# 1. Читання даних
def load_data():
    contacts = {}
    if os.path.exists("contact_list.txt"):
        with open("contact_list.txt", "r", encoding="utf-8") as file:
            for line in file:
                if ":" in line:
                    name, phone = line.strip().split(":", 1)
                    contacts[name] = phone
    return contacts

# 2. Парсинг та логіка команд
def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    # якщо немає аргументів повертаємо команду як є
    if len(args) == 0:
        return cmd, []
    # якщо аргументів недостатньо, повертаємо іх
    if len(args) < 2:
        return cmd, args
    # якщо аргументів 2 шукаємо де телефон
    arg1, arg2 = args[0], args[1]
    if len(re.sub(r"\D", "", arg1)) > len(re.sub(r"\D", "", arg2)):
        phone, name = arg1, arg2
    else:
        name, phone = arg1, arg2
    
    # Чистимо телефон
    phone_cleaned = re.sub(r"[^\d]", "", phone)
    
    return cmd, [name, phone_cleaned]

def add_contact(args, contacts):
    if len(args) < 2: return "😒 Error: Give me name and phone please."
    # "add username phone". За цією командою бот зберігає у пам'яті новий контакт.
    name = args[0]
    phone = args[1]
    contacts[name] = phone
    save_data(contacts)
    return f"📞 {name}: {contacts[name]}"

def change_contact(args, contacts):
    # "change username phone". За цією командою бот зберігає в пам'яті новий номер телефону phone
    # для контакту username, що вже існує в записнику.
    if len(args) < 2: return "🤔 Error: Give me name and phone please."
    # "add username phone". За цією командою бот зберігає у пам'яті новий контакт.
    name = args[0]
    phone = args[1]
    contacts[name] = phone
    save_data(contacts)
    return "😊 Contact updated."

def phone(args, contacts):
    if not args: return "😕 Error: Give me name please."
    name = args[0]
    return contacts.get(name, "😕 Contact not found.")

def delete_contact(args, contacts):
    if not args: return "🤔 Error: Give me name please."
    name = args[0]
    if name in contacts:
        contacts.pop(name)
        save_data(contacts)
        return f"Contact {name} deleted."
    return "Not found."

def show_all(contacts):
    # "all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
    if not contacts: return "List is empty."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

# 3. Головний цикл
def main():
    contacts = load_data()
    print("🤖🌸 Welcome to the assistant bot!📱📒")
    while True:
        user_input = input("Enter a command 📒 " + Fore.CYAN + Style.BRIGHT + "Add contacts, Change contacts, All, Delete contact, Exit: " + Style.RESET_ALL).strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("🤖 Good bye! 🌸")
            break
        elif command == "hello":
            print("🤖 How can I help you? ☕")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))    
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(phone(args, contacts))
        elif command == "delete":
            print(delete_contact(args, contacts))
        else:
            print("🤨 Invalid command.")

if __name__ == "__main__":
    main()

