from gui import *


def runFewTests():
    print(tax_credit(4000))
    print(tax_credit(10000))
    print(tax_credit(11140))
    print(tax_credit(11142))


def main():
    runFewTests()
    drawGUI()


main()
