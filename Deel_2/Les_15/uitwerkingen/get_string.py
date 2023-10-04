# get_string
# user_input.py

def get_string(prompt):
  
    user_input = input(prompt)
    return user_input

if __name__ == "__main__":
  
    user_string = get_string("Voer een tekst in: ")
    print(f'Je hebt ingevoerd: {user_string}')
