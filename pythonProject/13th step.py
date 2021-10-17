# If statments basics part 2

age = 35
name = "James"

# Example number 1 - Logical operator 'and'
if age>20 and name== "James":
    print("Example 1 - My name is James, and I'm over 20")

else:
    print("Exampel - Defauult exist point")



# Example number 2 - Logical operator 'and'
if age > 20 or name == "James":
    print("Example 2 - My name is James, and I'm over 20")

else:
    print("Exampel 2 - Defauult exist point")


# Example - Nested 'if' statements
married = False

if age>20 and name == "James" :
    if married == True:
        print("Exampel 3 - Good luck, its gonns be a long (happy) ride (-:")
    else:
        print("Exampel 3 - Nested 'else' ")

else:
    print("Example 3 - Parent 'else' ")