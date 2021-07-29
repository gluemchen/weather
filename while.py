import random
temperatur = ["kalt", "heiss", "normal", "error"]
random_temp = random.choice(temperatur)
while random_temp:
    random_temp = "kalt"
    if random_temp == "kalt":
        print("Es ist kalt!")
        random_temp = "heiss"
        continue
    elif random_temp == "heiss":
        print("Es ist heiss!")
        random_temp = "normal"
        continue
    elif temperatur == "normal":
        print("Es ist angenehm!")
        random_temp = "error"
        continue 
    else:
        random_temp == "error"
    print("Something went wrong!")
    