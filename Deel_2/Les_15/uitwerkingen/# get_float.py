 # user_input.py
# get_float()


def get_float(prompt):
  
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Ongeldige invoer. Probeer opnieuw met een getal.")

if __name__ == "__main__":
    user_float = get_float("Voer een getal in: ")
    print(f'Je hebt ingevoerd: {user_float}')
