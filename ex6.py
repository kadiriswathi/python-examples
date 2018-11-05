name=input('enter the customer name')
type=input("enter slab typer|R|c|C|i|I:")
units=float(input("enter the untis"))


def amount(type, units):
    if type=='i'or type=='I':
        return units*5.25
    elif type=='c' or type=='C':
        return  units*4.00
    else:
        return  units*3.08


if type =='i' or type=='I'or type=='c' or type=='C' or type=='i'or type=='I':
    print("total bill amount is",amount(type,units))
else:
    print("please select  the correct type")