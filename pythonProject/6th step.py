# Collection - Dictionart (basics)

# Creat a new dictionary
new_employee = {'first_name' : 'David' , 'salary' : 100000 , 'company' : 'Google'}

# Print the dictionary
print('Print the dictionary : ' +str(new_employee))

# Get cell 'value' - first way
print("Get 'value' of 'first_name' key :  "  + str(new_employee['first_name']))

# Get cell 'value' - second way
print("Get cell 'value' of 'salary' key : " + str(new_employee.get('salary')))

# Remove dictionary cell by using '.pop()
new_employee.pop('salary')
print("Remove dictionary cell by using '.pop()' : " +str(new_employee))

#Print out all 'key' out of the dictionary
print("Get all 'key' out of the dictionary : " +str(new_employee.keys()))

#Print out all 'valuse' out of the dictionary
print("Get all 'values' out of the dictionary : " +str(new_employee.values()))

# Use a variable and place it inside a dictionary cell
job_title_value= "developer"
new_dictionary = {"job_title" : job_title_value}

print("Print the 'new dictionary' : " + str(new_dictionary))