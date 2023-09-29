#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Sep. 29, 2023
# This program gets a diameter for a pizza and will calculate the total, including tax.

import constants


def main():
    # Get diameter from user
    print("This program calculates the total cost of a pizza with user-given diameter.")
    diameter = float(input("Please enter a diameter for the pizza (inch): "))

    # Calculate total cost of pizza
    subtotal = constants.MATERIALS * diameter + constants.RENT + constants.LABOUR
    total = subtotal * (1 + constants.HST)

    # Display total cost of pizza
    print("The total cost of the pizza is: ${:.2f}".format(total))


if __name__ == "__main__":
    main()
