# A simple string example
short_string_variable = "Have a greaat week, Ninjas !"
print(short_string_variable)

# Print the first letter of a string variable, index 0
firs_letter_variable = "New York City"[0]
print(firs_letter_variable)

# Mix upper and lower case letter variable
mixed_letter_variable = "This Is A MIxeD VarRiAbLe"
print(mixed_letter_variable.lower())

# Length of the variable
print(len(mixed_letter_variable))

# Use '+' sign a print command
first_name = "David"
print("First name is : " + first_name)

# Replace a part of a string
first_serial_number = " ABC123"
print("changed serial number  : " + first_serial_number.replace('AB', '1234'))
# Replace a part of a string -> Twice !
second_serial_number = "ABC123ABC"
print("changed serial number #2 : " + second_serial_number.replace('ABC', 'zzz' , 1))

# Take a part of a variable , according to specific index range
range_of_indexes = second_serial_number[0:3]
print(range_of_indexes)

# one last thing - adding spaces between multiple variable in print
first_word = "thank"
second_word = " you"
third_word = " God"

print(first_word + second_word + third_word)
