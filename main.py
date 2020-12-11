# Simple encryption/decryption system

import string
import random
import os
from sys import path


class Encryption:

    def __init__(self, obj):
        self.phrase = obj

    def encrypt(self):
        y = list(self.phrase)
        encrypted_message = ""
        for i in y:
            with open("codex.txt", 'r') as file:
                lines = file.readlines()
                for line in lines:
                    x = line.split(" ")
                    x = [s.replace('\n', '') for s in x]
                    if i == x[0]:
                        encoded_letter = x[2]
                        encrypted_message += encoded_letter
        return encrypted_message


class Decryption:

    def __init__(self, obj, length):
        self.phrase = obj
        self.length = length

    def decrypt(self):
        x = [' '.join(self.phrase[i:i + self.length] for i in range(0, len(self.phrase), self.length))]
        x = x[0].split(" ")
        decrypted_message = ""

        for element in x:
            with open('codex.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    x = line.split(" ")
                    x = [s.replace('\n', '') for s in x]
                    if element == x[2]:
                        decrypted_letter = x[0]
                        decrypted_message += decrypted_letter
        if len(decrypted_message) == 0:
            raise Exception("invalid encryption message.")
        else:
            return decrypted_message


def rnd(x):
    return ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=x))


def writefile():
    alphabets = string.ascii_letters
    numbers = string.digits
    punct = string.punctuation
    with open('codex.txt', 'w') as file:
        for i in alphabets:
            entry = i + " = " + str(rnd(10)) + "\n"
            file.write(entry)
        for i in numbers:
            entry = i + " = " + str(rnd(10)) + "\n"
            file.write(entry)
        for i in punct:
            entry = i + " = " + str(rnd(10)) + "\n"
            file.write(entry)


try:
    with open('codex.txt') as f:
        if os.stat("codex.txt").st_size == 0:
            writefile()
        else:
            pass
except IOError:
    f = open("codex.txt", "x")
    writefile()
key = input("Would you like to encrypt or decrypt a phrase (no spaces)? ")

while True:

    if key.lower() == "encrypt":
        phrase: str = input("What would you like to encrypt: ")
        encrypted = Encryption(phrase)
        print(f"Your encrypted phrase: {encrypted.encrypt()}")
        break

    elif key.lower() == "decrypt":
        phrase: str = input("What would you like to decrypt: ")
        decrypted = Decryption(phrase, 10)
        print(f"Your decrypted phrase: {decrypted.decrypt()}")
        break

    else:
        print("Invalid response")
        break
