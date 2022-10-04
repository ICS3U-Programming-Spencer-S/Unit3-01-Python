#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Oct. 3, 2022
# A program to calculate total of a sale for Manitoba

# Constants, Manitoba 12%
import constants


def main():

    # Get user subtotal
    subtotal = float(input("What is the cost of the item?: $"))

    # Calculate the tax with the subtotal
    tax = subtotal * constants.Provtax
    total = subtotal + tax

    # Prints the tax cost and the sales tax.
    print(
        "${0:.2f} was added to the total due to the {1:.2f}% Manitoba sales tax.".format(
            tax, constants.Provtax * 100
        )
    )

    # Display end result of tax cost
    print("The total cost of the item was ${0:.2f}".format(total))


if "__main__" == __name__:
    main()
