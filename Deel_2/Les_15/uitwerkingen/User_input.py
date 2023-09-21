def get_integer(zin):
    getal = -1
    while getal == -1:
        try:
            getal = int(input(zin))
        except ValueError:
            print("voer toch eens eeen getal in, dat doe je nu niet.")

    return getal

# def get_letter(vraag):
#     letter == ""
#     while letter == "":
#         letter = input(vraag)
#         if len(letter) > 1:
#             letter = ""
#         print("Max, 1 karakter")
        
#     return letter