def phone_brands(brand3, brand1, brand2):
    print("The 3rd brand is " + brand3)


phone_brands(brand1="Apple", brand2="Xiaome", brand3="LG")

print("\n")


def clothing_companies(*clothing_companes):
    print("The last company is : " + clothing_companes[-1])


clothing_companies("Nike", "Adidas", "H&M")
clothing_companies("Nike", "Adidas")

print("\n")


def my_function(**cmopany_info):
    print("His last name is " + cmopany_info["model"])


my_function(brand="Apple ", model="iPhone_x")
my_function(brand="Apple ", model="iPhone_x", year = 2020)
