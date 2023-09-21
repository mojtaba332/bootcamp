TE_RADEN_WOORD = "Python"
print("Welkon bij mijn Game...")

geraden_woord = input("wat is het woord?")
while geraden_woord != TE_RADEN_WOORD:
    print("Het woord is helaas fout!")
    geraden_woord = input("wat is het woord?")

print(f"je hebt het woord geraden, het wa: {TE_RADEN_WOORD}")
