# Лаборатория Фарадея: : Эпоха 1 (1831)
# Переменные состояния симуляции

is_magnet_moving = True # Движется ли магнит?
direction_in = True     # Направление: True - внутрь катушки, False - наружу
speed = 5               # Скорость движения (условные единицы)
voltage = 0

# Выводим состояние в консоль, чтобы проверить
print(f"Магнит движется: {is_magnet_moving}")
print(f"Направление внутрь: {direction_in}")
print(f"Скорость: {speed}")

if not is_magnet_moving:
    voltage = 0
if is_magnet_moving:
    if direction_in:
        voltage = speed
    else:
        voltage = -speed
print(f"Напряжение: {voltage}")
