max_even = None
min_odd = None
count_even = 0
count_odd = 0

while True:
    text = input("Въведете число (Enter за край): ")
    if text == "":
        break
    x = int(text)
    if x % 2 == 0:
        count_even += 1
        if max_even is None or x > max_even:
            max_even = x
    else:
        count_odd += 1
        if min_odd is None or x < min_odd:
            min_odd = x

print(f"Брой четни числа: {count_even}")
print(f"Брой нечетни числа: {count_odd}")

if max_even is not None:
    print(f"Максимално четно число: {max_even}")
else:
    print("Няма въведени четни числа.")

if min_odd is not None:
    print(f"Минимално нечетно число: {min_odd}")
else:
    print("Няма въведени нечетни числа.")