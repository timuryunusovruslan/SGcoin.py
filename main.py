import random

print("Hello, my friends!")

print("Here is a website to get SG crypto")

print("But you need to follow these steps")



balance = 0 
coins = 0

name = input("But first, what is you name? ")

print(f"Nice to meet you {name}!")







print("1 - check your bank account, 2 - spin daily wheel, 3 - get coins, 4 - send them to someone, 5 - type Promo code")
choosen = int(input("Now you need to select option..."))

if choosen == 1:
    print(balance)
        

if choosen == 2:
    print("How i see you want to spin wheel!")
    got_coin = random.randint(1,100)
    print(got_coin)
    balance = balance + got_coin
    print(f"Now your balance is: {balance}")
        

if choosen == 3:
    adding = int(input("How much coins do you want to add? But only less than 100 "))
    if adding > 100:
        print("Too much amount at a time!")
    if adding < 100:
        balance = balance + adding
        print(balance)
        


if choosen == 4:
    subtraction = int(input("How much coins you want to send to anyone? "))
    balance = balance - subtraction
    print(balance) 


if choosen == 5:
    promo_number = random.randint(100, 1000)
    promo_choice = input("Promo code: ")
    if promo_choice == "Gold Ticket" or "GTA4":
        balance = balance + promo_number
        print(f"You are lucky, you are getting {promo_number} sg coins")
        print(f"Your new balance: {balance}")


print("Now you have a special ticket number!")
print("Use it for transactions!")
selection_number = random.randint(1000, 10000)
print(f"Your special code: {selection_number}")
print(f"Your balance: {balance}")
print("Your next visit must be in an hour!")
print("Now you can trade your sg's coins with other users")




        
    




