print('Добро пожаловать в игру "Камень, ножницы, бумага"!')

options = ["камень", "ножницы", "бумага"]

while True:
    user_choice = input(
        "Выберите один из вариантов: камень, ножницы, бумага (или введите 'выход' для завершения игры): ")
    if user_choice == "выход":
        break
    elif user_choice in options:
        import random
        comp_choice = random.choice(options)
        print("Компьютер выбрал: " + comp_choice)
        if user_choice == comp_choice:
            print("Ничья!")
        elif (user_choice, comp_choice) in [("камень", "ножницы"), ("ножницы", "бумага"), ("бумага", "камень")]:
            print("Вы победили!")
        else:
            print("Вы проиграли!")
    else:
        print("Пожалуйста, введите правильный вариант.")

print("Спасибо за игру!")
