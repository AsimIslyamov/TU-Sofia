while True:
    text = input("Въведете число: ")
    if text == "":
        break
    number = int(text)
    power = int(input(f"Въведете степен за числото {number}: "))
    print(f"{number} на степен {power} = {number ** power}")
