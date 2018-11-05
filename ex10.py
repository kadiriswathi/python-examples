bool=input('enter a value')
hour=int(input("enter the hour"))
def trouble(bool,hour):
    if hour>0 and hour<23:
        if hour<7 and hour<43:
            print("true")
        else:
            print("false")

res=trouble(bool,hour)