import random
Prepod = input("Введите имя преподователя")
Students = ["Вадим", "Лера", "Андрей", "Света"]
for str in Students:
    Students.sort()
    print("Преподователь:", Prepod)
    print("Список студентов:", *Students, sep="\n")
    break
print("К доске идет:" + random.choice(Students))