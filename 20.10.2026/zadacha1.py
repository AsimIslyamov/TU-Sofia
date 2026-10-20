n = int(input("Колко числа ще въведете? "))

sum_even = 0
count_even = 0
sum_odd = 0
count_odd = 0

for i in range(n):
    x = int(input(f"Въведете число {i + 1}: "))
    if x % 2 == 0:
        sum_even += x
        count_even += 1
    else:
        sum_odd += x
        count_odd += 1

if count_even > 0:
    print(f"Четни числа - сума: {sum_even}, средноаритметично: {sum_even / count_even:.2f}")
else:
    print("Няма въведени четни числа.")

if count_odd > 0:
    print(f"Нечетни числа - сума: {sum_odd}, средноаритметично: {sum_odd / count_odd:.2f}")
else:
    print("Няма въведени нечетни числа.")
