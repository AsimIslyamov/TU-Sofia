n = int(input("Въведете лявата граница n: "))
m = int(input("Въведете дясната граница m: "))

count_in_range = 0
sum_in_range = 0

while True:
    text = input("Въведете число (Enter за край): ")
    if text == "":
        break
    x = int(text)
    if n <= x <= m:
        count_in_range += 1
        sum_in_range += x

print(f"Брой числа в интервала [{n}; {m}]: {count_in_range}")
print(f"Сума на числата в интервала [{n}; {m}]: {sum_in_range}")
