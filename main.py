print("Добро пожаловать в этот мир! Выживите ли вы здесь или умрёте - зависит от вас!")
print("Создайте своего персонажа!:")
a = input("Введите имя персонажа?:")
b = input("Гендер персонажа?:")
if b != "ламинат":
    print("а чё не ламинат")
c = input("Рост персонажа?:")
d = input("где работает ваш персонаж?:")
print("Ваши характеристики:""Имя:", a, "Пол:", b, "Рост:", c, "Работа:", d, "Нажмите Enter чтобы продолжить")
input("")
print("Ваш персонаж", a, "появился в России ваш шанс выживания тут 0.00001% Нажмите Enter чтобы продолжить")
input("")
f = input("Ваш персонаж коммунист?:")
if f != "да":
    print("Ваш персонаж умер")
print("Перед вами 3 пути: Бардель, Арена, Замок. Куда ты пойдёшь?")
s = input("")
if s.lower() == "бардель":
    print("вы зашли в Бардель 'вам понравилось)))' к вам подходит охранник но у вас нет денег что вы выберите: отсос, драка ")
    g = input("")
    if g.lower() == "отсос":
        print("Вас отпускают")
    elif g.lower() == "драка":
        print("вы проиграли и вас выеб")

elif s.lower() == "арена":
    print("вы зашли в Арену 'вы были тяжело ранены и умерли' даже не зашёв в арену  ")

elif s.lower() == "замок":
    print("вы зашли в Замок 'вас выгнали лол' ")

else:
    print("Такой локации нет")