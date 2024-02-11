import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

temp_password = []
final_password = ""

letters_size = int(input("\nHow many letters do you want? "))
numbers_size = int(input("\nHow many numbers do you want? "))
symbols_size = int(input("\nHow many symbols do you want? ")) 

for i in range(letters_size):
    temp_password.append(random.choice(letters))
for i in range(numbers_size):
    temp_password.append(random.choice(numbers))
for i in range(symbols_size):
    temp_password.append(random.choice(symbols))

final_password = "".join(random.sample(temp_password, len(temp_password)))

if final_password == "":
    print("\nYou can't have and empty password!\n")
else:
    print(f"\nYour password is: {final_password}\n")