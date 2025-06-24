# # movie_request = input("do you want watch a movie? (yes or no): ").lower()
# # if movie_request == "yes":
# #     movie_genre = input("Enter the genre of the movie you want to watch: ").lower()
# #     if movie_genre == "comedy":
# #         print("You might like movies like 'The Hangover Trilogy'.")
# #     else:
# #         print("You might like movies like 'Top Gun'.")   
# # else:
# #     print("Okay, watch a TV series!")        



# request = input("Do you want to book a hotel or resort: ").lower()
# if request == "resort":
#     max_price = int(input("Enter the max price per night: "))
#     if max_price >= 350:
#         print("You can book for the six senses resort.")
#     else:
#         print("You can book for the four seasons.")    
# else:
#     print("You can book for the nearest Hilton hotel.")


# This code calculates the total cost of three products and applies a discount based on the most expensive product.
product1 = int(input("Enter the cost for first product: "))
product2 = int(input("Enter the cost for second product: "))
product3 = int(input("Enter the cost for third product: "))

total = product1 + product2 + product3

if product3 > product1 and product3 > product2:
    discounted_total = total * 0.5
    print("You get a 50% discount. Total =", discounted_total)
elif product1 > product2 and product1 > product3:
    discounted_total = total * 0.34
    print("You get a 66% discount. Total =", discounted_total)
else:
    print("No discount. Total =", total)

