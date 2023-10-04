#get_letter


# user_input.py

def get_letter(prompt):

    while True:
        user_input = input(prompt)
        
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.upper()
        else:
            print("Ongeldige invoer. Voer precies één letter in.")

if __name__ == "__main__":
    user_letter = get_letter("Voer één letter in: ")
    print(f'Je hebt ingevoerd: {user_letter}')
