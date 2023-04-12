"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json


def write_order_to_json():
    
    order = {"item": "клавиатура", "quantity": 1,
             "price": 400, "buyer":"Петров И.И.", "date": "20.11.2000" }

    with open('orders.json', encoding='utf8') as file:
        data = json.load(file)
        data["orders"].append(order)
        with open('orders.json', 'w', encoding='utf8') as ot_file:
            json.dump(data, ot_file, ensure_ascii=False, indent=4)
        

write_order_to_json()