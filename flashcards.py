# Flashcards
# Project Completed By Iván Luna, August 3, 2023
# For Hyperskill (Jet Brains Academy).
import random
import argparse
from io import StringIO


log = StringIO()
cards = {}
for key, value in cards.items():
    cards[key] = {"definition": value, "errors": 0}


def add_card():
    print("The card:")
    while True:
        input_key = input()
        log.write(f"{input_key}\n")
        if input_key in cards.keys():
            print(f"The card \"{input_key}\" already exists. Try again:")
            log.write(f"The card \"{input_key}\" already exists. Try again:\n")
        else:
            break
    print("The definition of the card:")
    log.write("The definition of the card:\n")
    while True:
        input_value = input()
        log.write(f"{input_value}\n")
        if input_value in [value["definition"] for value in cards.values()]:
            print(f"The definition \"{input_value}\" already exists. Try again:")
            log.write(f"The definition \"{input_value}\" already exists. Try again:\n")
        else:
            break
    cards[input_key] = {"definition": input_value, "errors": 0}
    print(f"The pair (\"{input_key}\":\"{input_value}\") has been added.\n")
    log.write(f"The pair (\"{input_key}\":\"{input_value}\") has been added.\n")


def remove_card():
    print("Which card?")
    log.write("Which card?\n")
    input_key = input()
    log.write(f"{input_key}\n")
    if input_key in cards.keys():
        del cards[input_key]
        print("The card has been removed.\n")
        log.write("The card has been removed.\n")
    else:
        print(f"Can't remove \"{input_key}\": there is no such card.\n")
        log.write(f"Can't remove \"{input_key}\": there is no such card.\n")


def import_cards():
    print("File name:")
    log.write("File name:\n")
    input_file = input()
    log.write(f"{input_file}\n")
    try:
        with open(input_file, "r") as file:
            for line in file:
                key, value, errors = line.strip().split(":")
                cards[key] = {"definition": value, "errors": int(errors)}
        print(f"{len(cards)} cards have been loaded.\n")
        log.write(f"{len(cards)} cards have been loaded.\n")
    except FileNotFoundError:
        print("File not found.\n")
        log.write("File not found.\n")


def export_cards():
    print("File name:")
    log.write("File name:\n")
    input_file = input()
    log.write(f"{input_file}\n")
    with open(input_file, "w") as file:
        for key, value in cards.items():
            file.write(f"{key}:{value['definition']}:{value['errors']}\n")
    print(f"{len(cards)} cards have been saved.\n")
    log.write(f"{len(cards)} cards have been saved.\n")


def ask_cards():
    print("How many times to ask?")
    log.write("How many times to ask?\n")
    input_number = int(input())
    log.write(f"{input_number}\n")
    for i in range(input_number):
        random_card = random.choice(list(cards.keys()))
        print(f"Print the definition of \"{random_card}\":")
        log.write(f"Print the definition of \"{random_card}\":\n")
        input_value = input()
        log.write(f"{input_value}\n")
        if input_value == cards[random_card]["definition"]:
            print("Correct!\n")
            log.write("Correct!\n")
        elif input_value in [value["definition"] for value in cards.values()]:
            get_key = [key for key, value in cards.items() if value["definition"] == input_value][0]
            print(f"Wrong. The correct answer is \"{cards[random_card]}\", "
                  f"but your definition is correct for \"{get_key}\".\n")
            log.write(f"Wrong. The correct answer is \"{cards[random_card]}\", "
                      f"but your definition is correct for \"{get_key}\".\n")
            cards[random_card]["errors"] += 1
        else:
            print(f"Wrong. The correct answer is \"{cards[random_card]}\".\n")
            log.write(f"Wrong. The correct answer is \"{cards[random_card]}\".\n")
            cards[random_card]["errors"] += 1


def save_log():
    print("File name:")
    input_file = input()
    with open(input_file, "w") as file:
        file.write(log.getvalue())
    print("Log saved succesfully.\n")


def hardest_card():
    hardest_cards = []
    max_errors = 0
    for key, value in cards.items():
        if value["errors"] > max_errors:
            max_errors = value["errors"]
            hardest_cards = [key]
        elif value["errors"] == max_errors:
            hardest_cards.append(key)
    if max_errors > 0:
        if len(hardest_cards) == 1:
            print(f"The hardest card is \"{hardest_cards[0]}\". You have {max_errors} errors answering it.")
            log.write(f"The hardest card is \"{hardest_cards[0]}\". You have {max_errors} errors answering it.\n")
        else:
            hardest_cards_str = '", "'.join(hardest_cards)
            print(f"The hardest cards are \"{hardest_cards_str}\". You have {max_errors} errors answering them.")
            log.write(f"The hardest cards are \"{hardest_cards_str}\". You have {max_errors} errors answering them.\n")
    else:
        print("There are no cards with errors.")
        log.write("There are no cards with errors.\n")


def reset_stats():
    for key, value in cards.items():
        cards[key]["errors"] = 0
    print("Card statistics have been reset.")
    log.write("Card statistics have been reset.\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--import_from", help="import cards from file")
    parser.add_argument("--export_to", help="export cards to file")
    args = parser.parse_args()
    if args.import_from:
        with open(args.import_from, "r") as file:
            for line in file:
                term, definition, errors = line.strip().split(";")
                cards[term] = {"definition": definition, "errors": int(errors)}
        print(f"{len(cards)} cards have been loaded.")
    while True:
        user_input = input("Input the action (add, remove, import, export, ask, exit, "
                           "log, hardest card, reset stats): \n")
        log.write(f"Input the action (add, remove, import, export, ask, exit, "
                  f"log, hardest card, reset stats): \n{user_input}\n")
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
            if args.export_to:
                with open(args.export_to, "w") as file:
                    for term, card in cards.items():
                        file.write(f"{term};{card['definition']};{card['errors']}\n")
                print(f"{len(cards)} cards have been saved.")
            exit()
        elif user_input == "log":
            save_log()
        elif user_input == "hardest card":
            hardest_card()
        elif user_input == "reset stats":
            reset_stats()


if __name__ == "__main__":
    main()