import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbols=["!","@","#","$","%","^","&","*","(",")",";","/","?","|"]
numbers=["1","2","3","4","5","6","7","8","9"]
print("Welcome to Aarya's Password Genrator :))))))\n")
no_letters=int(input("No of letters in Password : "))
no_symbols=int(input("No of symbols in Password : "))
no_numbers=int(input("No of numbers in Password : "))
# Easy level 
# password=""
# for char in range(0,no_letters):
#     password += random.choice(letters)
#     print(password)
# for char in range(0,no_symbols):
#     password += random.choice(symbols)
#     print(password)
# for char in range(0,no_numbers):
#     password += random.choice(numbers)
#     print(password)
# hard level 
password=[]
for char in range(0,no_letters):
    password += random.choice(letters)
for char in range(0,no_symbols):
    password += random.choice(symbols)
for char in range(0,no_numbers):
    password += random.choice(numbers)
random.shuffle(password)
final_password=""
for char in password:
    final_password+=char
print("Ypur password is : ",final_password)
