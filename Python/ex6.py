#Переменная
types_of_people = 10
x = f"Существует{types_of_people} типов людей."

binary = "python"
do_not = "Нет"
#Строка с помещением в нее других строк
y = f"Те, кто понимает {binary}, и те кто {do_not}."

print(x)
print(y)

print(f"Я сказал:{x}")
#Строка с помещением в нее других строк 
print(f"А еще я сказал: '{y}''")

hilarious = False
joke_evaluation = "Разве это не смешно?! {}"
#Строка с помещением в нее других строк
print(joke_evaluation.format(hilarious))

w = "Это часть строки слева..."
e = "А это справа"
#Строка с помещением в нее других строк
print( w + e)
