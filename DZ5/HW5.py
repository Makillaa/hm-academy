import requests  # Скачали пакет "Запроса"

url = "https://httpbin.org/post"  # Ссылка, куда шлём запроса
data = {
    "first_name": "Max",
    "last_name": "Hryshchenko",
    "email": "1@gmail.com",
    "password": "1qwerty1"
}
my_request = requests.post(url, data)  # Запрос post на сыылку и с ключами и их значениями
data = my_request.json()  # Реквест в виде Словаря
print(data["form"])  # Выводим данные записанные в форму
