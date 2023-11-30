import os
import sys
from cpf_validator import CPF, CPFFormatter, CPFValidator


def clear_console():
    """
    Clears the console screen.
    """
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    while True:
        cpf_input = input("Enter the CPF you want to validate: ")
        cpf = CPF(cpf_input, CPFFormatter(), CPFValidator())
        if cpf.is_valid():
            print("Valid CPF.")
        else:
            print("Invalid CPF.")
        if input("Do you want to validate another CPF? (y/n): ").lower() != "y":
            break
        clear_console()
