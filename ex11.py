tm=int(input("enter the marks:"))
def total(tm):
 if tm>360 :
  print("Frist Class")
 elif tm>=300 and tm<360:
  print("second class")
 elif tm<300:
    print("third class")
marks=total(tm)