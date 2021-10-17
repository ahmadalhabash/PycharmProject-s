# Exceptions / Errors practice

# Assignment 1
x = 5
try:

       print("The number is : " +x)
except:
       print("Casting WAS NOT made for the print of 'x'")
       print("The number is : %s " % x)
       print("\n")

# Assignment 2
try:
     y+1
except:
    y = 1
    print("Y was not defined, Name Error was raised")
    result = y+5
    print(result)

print("\n")

# Assignment 3

list = [1, 2, 3, 4]
try:
     print(list[6])
     print("xxx")
except:
      print("Tried to pull index '6' while only '3' are available")
      print(list[3])