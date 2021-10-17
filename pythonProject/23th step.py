# Methods Practice

# Part - A
def sorting(*languages_list):

    for languages in languages_list:
        if languages == "Java":
            print("Java language found")

            for character in languages:
                print(character)

        else:
            print("Java was not found " +languages)

sorting("Python", "JS", "c++")
sorting("Pthon", "Java")
sorting("Python", "Java", "GO")
print("\n")
print("\n")
# Part - B
def tax_calculacation(gross_salary, tax = 0.22):

    net_salary = gross_salary * (1-tax)
    print("Net Salary is : " + str(net_salary))
    return net_salary

def salary_limit_tester(net_salary__variable):

    if net_salary__variable >= 5800:
        print("Success! The salary is : " + str(net_salary__variable))

    else:
        print("The Salary is under 5800, it is : " + str(net_salary__variable))


net_slary_1 = tax_calculacation(5000, 0.2)
salary_limit_tester(net_slary_1)


net_slary_2 = tax_calculacation(6000, 0.2)
salary_limit_tester(net_slary_2)

net_slary_3 =tax_calculacation(10000)
salary_limit_tester(net_slary_3)