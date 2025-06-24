# # # # != is to check if the valueare not equal
# # # # genre = input("Enter your favorite genre of music: ")
# # # # if genre == "rock":
# # # #     print("You might like bands like Queen or The Rolling Stones.")
# # # # else:
# # # #     print("You might like artists like Taylor Swift or Drake.")    

# # # password = input("Enter your password: ")
# # # if password != "1234":
# # #     print("incorrect, Password!")
# # # else:
# # #     print("Welcome to your account!")
# # #     print("You can now access your account details.")

# # # creating a discount program trip
# # # trip_type = input("Enter the trip Buisness or Personnal?: ").lower() 
# # # price = int(input("Enter the price of your trip: "))

# # # discount = trip_type == "buisness" and price >= 1200
# # # print("Discount applied" if discount else "No discount available")


# # creating a discount code for a product
# # discount_code = input("Enter your code: ")
# # if discount_code == "wac":
# #     print("Discount applied: 20%!") 
# # else:
# #     print("No discount available") 
    
    
# # creating a program for a type of trip
# trip_cost = int(input("Enter the cost of your trip: "))
# if trip_cost <350:
#     print("You can go to the stay-cation")
# elif trip_cost >= 350 and trip_cost < 1000:
#     print("You can go on a road trip")
# elif trip_cost >= 1000:
#     print("You can go with flight to the beach")
    
# print("Have Fun!")


# craeting a program gather the bag weight in KG and also either domestic or international from the user
bag_weight = int(input("Enter the weight of your bag in KG: "))
destination = input("Enter your destination (domestic or international): ").lower()
if bag_weight <= 18:
    price = 25
else:
    price = 75

if destination == "domestic":
    price += 300
elif destination == "international":
    price += 750
    
else:
    print("❌ Error: Invalid destination. Please enter 'domestic' or 'international'.")
    exit()  # Stops the program if destination is invalid
    
print("The total price for your bag is:", price, "$")