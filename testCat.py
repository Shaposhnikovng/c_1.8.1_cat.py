from cat import Cat

cat1 = Cat("Барон", "мальчик", 1)
cat2 = Cat("Матильда", "девочка", 2)
name1 = "Кличка: "
gender1 = "Пол: "
age1 = "Возраст: "

print("-------------------")
print("---Кошки---")
print("-------------------")
print(name1, cat1.name)
print(gender1, cat1.gender)
print(age1, cat1.age)
print("-------------------")
print(name1, cat2.name)
print(gender1, cat2.gender)
print(age1, cat2.age)
