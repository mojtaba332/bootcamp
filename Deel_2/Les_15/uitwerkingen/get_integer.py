# user_input.py
# - get_integer()


def get_integer(prompt):
    
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Ongeldige invoer. Probeer opnieuw met een geheel getal.")

if __name__ == "__main__":

    user_integer = get_integer("Voer een geheel getal in: ")
    print(f'Je hebt ingevoerd: {user_integer}')
