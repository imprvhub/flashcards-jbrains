#'Flashscards' project for hyperskill - jetbrains, completed by Iván Luna

import random

cards = {}

def add_card():
    input_key = input("The card:\n")
    while input_key in cards:
        input_key = input(f'The card "{input_key}" already exists. Try again:\n')
    input_value = input("The definition of the card:\n")
    while input_value in [value["definition"] for value in cards.values()]:
        input_value = input(f'The definition "{input_value}" already exists. Try again:\n')
    cards[input_key] = {"definition": input_value, "errors": 0}
    print(f'The pair ("{input_key}":"{input_value}") has been added.\n')

def remove_card():
    input_key = input("Which card?\n")
    if input_key in cards:
        del cards[input_key]
        print("The card has been removed.\n")
    else:
        print(f'Can\'t remove "{input_key}": there is no such card.\n')

def import_cards():
    input_file = input("File name:\n")
    try:
        with open(input_file, "r") as file:
            for line in file:
                key, value, errors = line.strip().split(":")
                cards[key] = {"definition": value, "errors": int(errors)}
        print(f"{len(cards)} cards have been loaded.\n")
    except FileNotFoundError:
        print("File not found.\n")

def export_cards():
    input_file = input("File name:\n")
    with open(input_file, "w") as file:
        for key, value in cards.items():
            file.write(f"{key}:{value['definition']}:{value['errors']}\n")
    print(f"{len(cards)} cards have been saved.\n")

def ask_cards():
    input_number = int(input("How many times to ask?\n"))
    for i in range(input_number):
        random_card = random.choice(list(cards.keys()))
        input_value = input(f'Print the definition of "{random_card}":\n')
        if input_value == cards[random_card]["definition"]:
            print("Correct!\n")
        elif input_value in [value["definition"] for value in cards.values()]:
            get_key = [key for key, value in cards.items() if value["definition"] == input_value][0]
            print(f'Wrong. The correct answer is "{cards[random_card]["definition"]}", '
                  f'but your definition is correct for "{get_key}".\n')
            cards[random_card]["errors"] += 1
        else:
            print(f'Wrong. The correct answer is "{cards[random_card]["definition"]}".\n')
            cards[random_card]["errors"] += 1

def main():
    while True:
        user_input = input("Input the action (add, remove, import, export, ask, exit):\n")
        if user_input == "add":
            add_card()
        elif user_input == "remove":
            remove_card()
        elif user_input == "import":
            import_cards()
        elif user_input == "export":
            export_cards()
        elif user_input == "ask":
            ask_cards()
        elif user_input == "exit":
            print("Bye bye!")
            exit()

if __name__ == "__main__":
    main()