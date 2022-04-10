#first attempt of menu creation 

option=100
  option=int(input("choose an option from the above list"))
  while option!=0
    if option==1:
      print("option 1 has been called")
    elif option==2:
      print("option 2 has been called")
    elif option==3:
      print("option 3 has been called")
    elif option==4:
      print("option 4 has been called")
    elif option==5:
      print("option 5 has been called")
    else:
      break



def menu():
  print("[1]Load Colour Files")
  print("[2]Print All Colours")
  print("[3]Select Colour")
  print("[4]Find Closest Colour")
  print("[5]Display Colour")
  print("[0]Exit")
