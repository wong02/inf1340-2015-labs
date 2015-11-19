#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

PROVINCIAL_TAX = .05
FEDERAL_TAX = .025


def calculate_provincial_tax(purchase):
    return purchase * PROVINCIAL_TAX

def calculate_federal_tax(purchase):
    return purchase * FEDERAL_TAX

def bill_of_sale(purchase):
    prov_tax = calculate_provincial_tax(purchase)
    fed_tax = calculate_federal_tax(purchase)

    file_name = "taxes.txt"

    with open(file_name, 'w') as output_file:
        output_file.write ("Amount of purchase: {0:.2f} \n".format(purchase))
        output_file.write ("Provincial tax: {0:.2f} \n".format(prov_tax))
        output_file.write ("Federal tax: {0:.2f} \n".format(fed_tax))
        output_file.write ("Total tax: {0:.2f} \n".format(prov_tax + fed_tax))
        output_file.write ("Total sale: {0:.2f} \n".format(1 + prov_tax + fed_tax))


bill_of_sale(5)