import string
import os
import json
from random import choices, shuffle
from pyperclip import copy

from cryptography.fernet import Fernet

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATIONS = string.punctuation

try:
    open('passwords.json')
except FileNotFoundError:
    with open('passwords.json', 'w') as outputFile:
        data = {}
        data['passwords'] = []
        json.dump(data, outputFile)
        outputFile.close()


def writeJSON(data):
    with open('passwords.json', 'w') as f:
        json.dump(data, f)
        f.close()


def generatePassword(length):
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATIONS}'
    shuffle(list(printable))

    password = choices(printable, k=length)
    password = ''.join(password)
    copy(password)

    return password


def encryptPassword(password_length):
    password = generatePassword(password_length)

    try:
        f = open('secret.key', 'r')
        key = f.read()

    except:
        key = Fernet.generate_key()
        with open('secret.key', 'wb') as key_file:
            key_file.write(key)

    f = Fernet(key)
    encryptedPassword = f.encrypt(password.encode('utf-8'))

    return encryptedPassword


def decryptPassword(siteName):
    d = json.load(open('passwords.json', 'r'))
    passwords = d['passwords']
    f = open('secret.key', 'r')

    key = f.read()
    fn = Fernet(key)

    for i in passwords:
        if i['site'] == str(siteName):
            password = fn.decrypt(bytes(i['password'], 'utf-8'))

            print(
                '\nUsername\E-mail: {}\nPassword: {}\n'.format(i['username'], password.decode('utf-8')))


def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
