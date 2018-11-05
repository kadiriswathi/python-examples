empname=input("enter the name:")
sal=float(input("entet the salary:"))
type=input("enter the degination:m|M|a|A|c|C:")
if type=="m":
    bonus=sal*20/100
    ts=sal+bonus
    print(ts)
if type=="a":
    bonus = sal * 10 / 100
    ts = sal + bonus
    print(ts)
if type=="c":
    bonus = sal * 5 / 100
    ts = sal + bonus
    print(ts)