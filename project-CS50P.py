# Description Pete's Random Password Generator
# DISCLAIMER: This program is not meant to be used for real passwords. For educational purposes only!
# https://cs50.harvard.edu/python/2022/project/


import cowsay
import random
import string


# Constants
MIN_CHARACTERS = 1
MAX_CHARACTERS = 20


def main():
    # Introduction to the user
    print_intro()

    # Get the requirements for the password
    character_count = get_int(
        f"How many characters (A to Z) do you want in your password? Enter a number between: {MIN_CHARACTERS}...{MAX_CHARACTERS}\n")
    number_count = get_int(
        f"How many numbers do you want in your password? Enter a number between: {MIN_CHARACTERS}...{MAX_CHARACTERS}\n")
    special_count = get_int(
        f"How many special characters (!@#$% and more) do you want in your password? Enter a number between: {MIN_CHARACTERS}...{MAX_CHARACTERS})\n")

    # Ask if the is satisfied with the password
    satisfied = False
    while not satisfied:
        # Generate and present the password to the user
        present_password(generate_password(
            character_count, number_count, special_count))
        satisfied = ask_if_satisfied()

    # Ask if the user wants a tip for generating stronger passwords
    tip = give_tip(character_count, number_count, special_count)
    if tip:
        cowsay.tux(tip)

    # Exit program
    print("Thank you for using Pete's Password Generator!\n")


def print_intro():
    """ Print an introduction to the program. """
    print("+----==========o[Pete's Password Generator]o=========----+\n DISCLAIMER: This program is not meant to be used for\n real passwords. For educational purposes only!\n")
    cowsay.tux("Hello, I am a Pete the Penguin!\nI will guide you through the process of\ngenerating a password for you.\nBefore I can start, I need to ask you a few\nquestions. Let's get started!")
    print()


# Pytest
def get_int(prompt):
    """ Get an integer from the user. Keep asking until the user enters a valid number."""
    while True:
        try:
            n = int(input(prompt))
            # Check if the number is not in the given range
            if n < MIN_CHARACTERS or n > MAX_CHARACTERS:
                continue
            # All requirements are met
            else:
                return n
        # If the user enters a string
        except ValueError:
            continue


def generate_password(character_count, number_count, special_count):
    """ Generate a password with the given requirements."""
    # Generating a concept for the password
    concept_password = list()
    for _ in range(character_count):
        concept_password += "c"
    for _ in range(number_count):
        concept_password += "n"
    for _ in range(special_count):
        concept_password += "s"
    random.shuffle(concept_password)

    # Filling the concept with random characters
    password = ""
    for character in concept_password:
        if character == "c":
            password += random.choice(string.ascii_letters)
        elif character == "n":
            password += random.choice(string.digits)
        elif character == "s":
            password += random.choice(string.punctuation)
    return password


# Pytest
def present_password(password):
    """ Present the password to the user."""
    cowsay.tux(
        f"The password I've come up with is '{password}'.\nI hope you like it!")


def ask_if_satisfied():
    """ Ask the user if they are satisfied with the password."""
    while True:
        answer = input("Are you satisfied with the password? (y/n)\n").lower()
        if answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        else:
            continue


# Pytest
def give_tip(character_count, number_count, special_count):
    """ Give a tip to the user to improve the strength of the password."""
    while True:
        answer = input(
            "Do you want a tip to improve the strength of your password? (y/n)\n").lower()
        if answer == "y" or answer == "yes":
            # Check if the password is too short
            if character_count + number_count + special_count < 10:
                return "Try to make your password longer. A password with 10 or more characters is considered strong."
            # Check if the password is too simple
            elif number_count < 3 or special_count < 3:
                return "Try to add more numbers and/or special characters to your password. A password with more than 3 characters of each categorie is considered strong."
            # The password is strong
            else:
                return "Keep up the good work! Your password is quite strong, but you can always make it stronger by making it longer."
        elif answer == "n" or answer == "no":
            return None
        else:
            continue


if __name__ == "__main__":
    main()
