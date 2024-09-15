"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


#iphone
iphone = [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]
iphone_score = 0
for score in iphone:
    iphone_score = iphone_score + score
avg_iphone = iphone_score / len(iphone)
print("Количество продаж айфона: ", iphone_score)
print("Среднее количество продаж айфона: ", avg_iphone)

#xiaomi
xiaomi = [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]
xiaomi_score = 0
for score in xiaomi:
    xiaomi_score = xiaomi_score + score
avg_xiaomi = xiaomi_score / len(xiaomi)
print("Количество продаж xiaomi: ", xiaomi_score)
print("Среднее количество продаж xiaomi: ", avg_xiaomi)

#samsung
samsung = [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]
samsung_score = 0
for score in samsung:
    samsung_score = samsung_score + score
avg_samsung = samsung_score / len(samsung)
print("Количество продаж самсунга: ", samsung_score)
print("Среднее количество продаж самсунга: ", avg_samsung)

all_score = iphone_score + xiaomi_score + samsung_score
avg_score = all_score / (len(iphone) + len(xiaomi) + len(samsung))
print("Общее количество продаж: ", all_score)
print("Среднее количество продаж всех товаров: ", avg_score)