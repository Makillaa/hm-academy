new_dict = {  # Создание словаря
    "first_name": "Max",
    "last_name": "Hryshchenko",
    "email": "1@gmail.com",
    "age": 20
}

my_list = []  # Создание пустого листа
for value in new_dict.values():  # Добавление определённых элементов в список
    if isinstance(value, str):
        if len(value) > 2 and "a" in value:
            my_list.append(value)
    elif isinstance(value, int):
        if value in range(25, 40):
            my_list.append(value)
print(my_list)

# for key, value in new_dict.items():  # Упрощённая версия алгоритма
#     if type(value) == str and len(value) > 5 and "a" in value:
#         my_list.append(value)
#     elif type(value) == int and range(25, 40):
#         my_list.append(value)
#         print(my_list)

for element in my_list:  # Убираем элементы с буквой m или n
    if type(element) == str and ("m" in element or "n" in element):
        my_list.remove(element)
    elif type(element) == int:
        element = str(element)
print(my_list)

list1 = ("Awe", "True", "Hrak")  # Создание нового листа со значаниями
my_list.extend(list1)  # Сопряжение нового листа к тому, что уже был
my_list.sort(reverse=True)  # Сортируем в обратном порядке
print(my_list)

new_string = " , ".join(my_list)  # Упрощённый метод создания строки с элементами листа через запятую
print(new_string)

# new_string = ""  # Создаём пустую строку
# for element in my_list:  # Переводим элементы с листа в строку и разделяем их запятой
#     new_string += str(element) + " , "
# new_string = new_string.strip(" , ")  # Убираем лишние запятые(в начале и конце)
# print(new_string)

new_string = new_string.split(' , ')  # Переводим обратно в список
print(new_string)
print(type(new_string))
