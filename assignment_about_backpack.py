# Задание №3
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один
# допустимый вариант.
# Верните все возможные варианты комплектации рюкзака.

things = {'зажигалка': 5,
          'компас': 5,
          'фрукты': 200,
          'рубашка': 50,
          'аптечка': 80,
          'куртка': 400,
          'бинокль': 50,
          'удочка': 500,
          'бутерброды': 250,
          'палатка': 800,
          'спальный мешок': 250,
          'жвачка': 5}


def collect_backpack(thing: dict, weight: int) -> dict:
    """
    collects a backpack
    1 - Dict
    2 - weight
    """

    backpack_weight = weight
    res = dict()
    for key, value in thing.items():
        if backpack_weight >= value:
            backpack_weight -= value
            res[key] = value

    return f"Сложили в рюкзак - {res}, Осталось веса {backpack_weight}"

print(f"Первый вариант - {collect_backpack(things, 1000)}")
print(f"Второй вариант - {collect_backpack((dict(sorted(things.items(), key=lambda item: item[1]))), 1000)}")
print(f"Третий вариант - {collect_backpack((dict(sorted(things.items(), key=lambda item: item[1], reverse=True))), 1000)}")