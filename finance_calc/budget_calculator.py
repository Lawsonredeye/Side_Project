#!/usr/bin/env python3
"""
Main program for the financial budget calculator to help
you stay in track with your finances
"""

from func import needs_budget, wants_budget, savings, display_account

income = int(input("Enter Budget/Income: "))
if not isinstance(income, int):
    raise TypeError("Invalid income! Income must be a digit")

print()
choice = input("Enter Expenses eg clothes, shoes: ")
expense = eval(input("Enter Price #: "))

print("\nIs it:\n1.) needs\n2.) wants\n3.) savings")
response = input("Enter response: ")

if response == "needs" or response == "1":
    needs = needs_budget(income, expense)
    print(f"you have {needs} left for your needs")
elif response == "wants" or response == "2":
    wants = wants_budget(income, expense)
    print(wants)
elif response == "savings" or response == "3":
    saving = savings(income, expense)
    print(saving)
else:
    print("Wrong input")
