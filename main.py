def tax_credit(income):
    if(income >= 5701 and income < 8549):
        return round((income*0.0668 - 380.5) / 0.17,2)
    elif(income >= 8549 and income < 11141):
        return round((income*(-0.0735)+819.08) / 0.17,2)
    else:
        return 0
def main():
    print(tax_credit(4000))
    print(tax_credit(11140))
    print(tax_credit(11142))
    
main()