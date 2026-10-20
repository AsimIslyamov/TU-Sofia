sum_positive = 0
product_positive = 1
count_positive = 0

while True:
    x = int(input("Въведете число (-99 за край): "))
    if x == -99:
        break
    if x > 0:
        sum_positive += x
        product_positive *= x
        count_positive += 1

if count_positive > 0:
    print(f"Сума на положителните числа: {sum_positive}")
    print(f"Произведение на положителните числа: {product_positive}")
else:
    print("Няма въведени положителни числа.")