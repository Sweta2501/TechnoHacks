import random
password = "ABCDEFGHIJKMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!~@#$%^&*()_+{}:"
len_password = int(input("Enter the length of the password: "))
p = "".join(random.sample(password, len_password))
print(f"Password is: {p}")
