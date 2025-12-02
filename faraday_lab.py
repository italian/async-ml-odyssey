import os   # <--- 1. Добавляем модуль для работы с системой

# Лаборатория Фарадея: : Эпоха 1 (1831)
# Переменные состояния симуляции

is_magnet_moving = False    # Движется ли магнит?
direction_in = True         # Направление: True - внутрь катушки, False - наружу
speed = 5                   # Скорость движения (условные единицы)
voltage = 0
message = ""

# 2. Запускаем бесконечный цикл
while True:
    os.system('clear')  # <--- 2. Очищаем экран перед каждым кадром

    print("--- СИМУЛЯЦИЯ ФАРАДЕЯ ---")
    print(message)
    message = ""

    # Выводим состояние в консоль, чтобы проверить
    print(f"Магнит движется: {is_magnet_moving}")
    print(f"Направление внутрь: {direction_in}")
    print(f"Скорость: {speed}")

    # Вся логика теперь внутри цикла (обрати внимание на отступы!)
    if not is_magnet_moving:
        voltage = 0
    if is_magnet_moving:
        if direction_in:
            voltage = speed
        else:
            voltage = -speed
    
    # Выводим результат
    print(f"Напряжение: {voltage} В")

    cmd = input("Ваше действие (w=внутрь, s=наружу, space=стоп):")
    if cmd == 'w':
        is_magnet_moving = True
        direction_in = True
    elif cmd == 's':
        is_magnet_moving = True
        direction_in = False
    elif cmd == ' ':
        is_magnet_moving = False
    else:
        message = "- Неизвестная команда -"
