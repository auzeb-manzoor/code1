#CMPT project Part1
#By aaqib wani


#Dictionary(empty)
open_dict={}


#creation of menu, The Main Porgram Loop
#the print functions that denote "option X has been called" are placeholders
w=1
while w==1:
    print("[1]Load Colour Files")
    print("[2]Print All Colours")
    print("[3]Select Colour")
    print("[4]Find Closest Colour")
    print("[5]Display Colour")
    print("[0]Exit")
    option=int(input("choose an option from the above list"))
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
    elif option==0:
      print("program terminated.")
      break   
    else:
      print("try a valid input")
#Opening the csv file
import csv
with open('colours.csv','r') as Colour_file:
  file= csv.reader(Colour_file)
  for line in file:
   colour_keys=tuple((line[1],line[2],line[3]))
#taking RGB values and presenting them as Tuples.
   name_keys=str((line[0],"hexdecimal"))
 #File Formatting, creation of dictionary
   open_dict[colour_keys]=name_keys
print(open_dict)
# example: print(rgbtohex((255, 255, 255)))
#assign hex code and then assign a corresponding hexdecimal to the integer.

def rgb2hex(rgb):
  return '#%02x%02x%02x' % rgb
  
