import requests  # Скачали пакет "Запроса"

url = "https://httpbin.org/post"  # Ссылка, куда шлём запроса
first_name = "Max"
last_name = "Hryshchenko"
email = "1@gmail.com"
password = "1qwerty1"
r = requests.post(url, {"first_name": first_name, "last_name": last_name,
                        "email": email, "password": password})  # Запрос post с ключами и их значениями
data = r.json()  # Реквест в виде Словаря
print(data["form"])  # ???
