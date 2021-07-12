import random

def passgen():
    print("How long do you want your password to be?")
    password_length = int(input())
    passwrd = ""
    ###
    possible_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@!$#"
    ###
    password_raw = random.sample(possible_chars, password_length)
    password = passwrd.join(password_raw)
    print(password)
passgen()
