# # # # creating a mini bot message loop
# # # word = input("Enter your word: ").lower()
# # # while word != "done":
# # #     print("we got your message")
# # #     word = input("Enter your word: ").lower()
  
  
# # #   creating account login
# # password = input("Enter your password: ").lower()
# # while password != "wac" and password != "wydad":
# #     print("Incorrect password, please try again.")
# #     password = input("Enter your password: ")
# # print("Welcome to your account!")


# # creating a discount for the first 3 people
# count = 0
# while count < 3:
# 	name = input("Enter your name: ")
# 	print("congrats!" ,name, "You saved 20%")
# 	count += 1
# name = input("Enter your name: ")
# print("All done!")


# creating a tries counter
tries = 0
program = ""
while tries < 5 and program != "python":
    program = input("Enter your programming language: ")
    tries += 1
    
if program == "python":
    print("You got it right!" , tries, "tries")