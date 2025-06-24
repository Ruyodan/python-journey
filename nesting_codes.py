# nesting = putting code inside another code
# weight_of_package = int(input("Enter weight of your package : "))
# number_of_packages = int(input("Enter number of packages: "))
# discount_of_package = 0.2

# total_of_cost_package = (weight_of_package * number_of_packages) * (1 - discount_of_package)
# print("Total cost of packages:", total_of_cost_package)


# rental_car = int(input("Enter number of cars: "))
# rental_days = int(input("Enter number of days: "))
# price_one_day = 100

# total_to_pay = rental_car * rental_days * price_one_day
# print("Total to pay:", total_to_pay)


income  = int(input("Enter the income: "))
food = int(input("Enter the food expenses: "))
rent = int(input("Enter the rent expenses: "))
extra = int(input("Enter the extra expenses: "))
expensive_tracker = food + rent + extra

total = income - expensive_tracker
print("remaining:", total)

