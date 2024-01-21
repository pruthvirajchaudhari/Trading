import random

def generate_password(length=8):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    numbers = '0123456789'
    password = ''

    for i in range(length):
        if i % 2 == 0:
            password += random.choice(characters)
        else:
            password += random.choice(numbers)

    return password

# Test the function
password = generate_password(10)
print("Generated Password: ", password)