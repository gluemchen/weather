lowest_value =int(input("Input lowest number: "))
highest_value =int(input("Input lowest number: "))

low_to_high = range(lowest_value-1,highest_value+1)

summe = 0

for i in low_to_high:
    summe += i
    print(summe)
    continue