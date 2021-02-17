import menu
import json


def main():
    menu.clearScreen()

    responce = input(
        'Enter 1: Create new password\nEnter 2: Search for username & password\nEnter any other to quit\n\n-> ')

    if responce == '1':
        try:
            passwordLength = int(
                input('Enter password length (recommended: 12-16): '))
        except ValueError:
            print('\n\nError: Must be an Integer Value\n\n')
            passwordLength = int(
                input('Enter password length (recommended: 12-16): '))

        menu.clearScreen()
        siteName = str(input('Enter Site Name: '))
        username = input('Enter Username or E-mail: ')

        password = menu.encryptPassword(passwordLength)

        with open('passwords.json') as json_file:
            data = json.loads(json_file.read())

            temp = data['passwords']

            y = {
                "site": str(siteName.lower()),
                "username": str(username.lower()),
                "password": password.decode('utf-8')
            }

            temp.append(y)

            menu.writeJSON(data)

            menu.clearScreen()
            print('\n\n------------------------------------')
            print('Password has been copid to clipboard')
            print('------------------------------------\n\n')

            main()

    if responce == '2':

        menu.clearScreen()
        site_name = str(input('Enter Site Name: '))
        menu.decryptPassword(site_name)

    else:
        print('Bye Bye!')
        exit()


main()
