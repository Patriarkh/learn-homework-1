"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    try:
        # Преобразуем аргументы к нужным типам
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
    except (ValueError, TypeError):
        # Если произошла ошибка приведения типов, сообщаем об этом
        raise ValueError("Некорректные аргументы: цена, скидка должны быть числами, а максимальная скидка — целым числом.")

    # Проверяем, что максимальная скидка не превышает 100
    if max_discount > 100:
        raise ValueError("Максимальная скидка не может быть больше 100")

    # Применяем скидку, если она не превышает max_discount
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

# Тестируем функцию
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))  # Это вызовет исключение
    print(discounted("сто", "десять"))  # Это вызовет исключение
    print(discounted(100.0, 5, "10"))

    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
