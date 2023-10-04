# les 16

def get_integer(prompt):

    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Ongeldige invoer. Voer een geldig geheel getal in.")

def get_float(prompt):
  
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Ongeldige invoer. Voer een geldig getal in.")

if __name__ == "__main__":

    user_integer = get_integer("Voer een geheel getal in: ")
    print(f'Je hebt ingevoerd: {user_integer}')

    user_float = get_float("Voer een getal in: ")
    print(f'Je hebt ingevoerd: {user_float}')
