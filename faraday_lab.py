import os   # <--- 1. Добавляем модуль для работы с системой

# Лаборатория Фарадея: : Эпоха 1 (1831)
# Переменные состояния симуляции

is_magnet_moving = False        # Движется ли магнит?
direction_in = True             # Направление: True - внутрь катушки, False - наружу
speed = 5                       # Скорость движения (условные единицы)
delta_speed = 1                 # Величина изменения скорости (условные единицы)
B_field = 2.0                   # Величина магнитной индукции/Сила магнита (условные единицы)
current_on = False              # Течет ли ток в первичной катушке?
prev_current_on = current_on    # Тек ли он в прошлом кадре?
voltage = 0.0
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
    print(f"Сила магнита (магнитная индукция): {B_field} Тл")
    print(f"Скорость: {speed}")
    print(f"Течет ли ток в первичной катушке?: {current_on}")
    print(f"Тек ли он в прошлом кадре?: {prev_current_on}")

    # Вся логика теперь внутри цикла (обрати внимание на отступы!)
    voltage = 0
    if is_magnet_moving:
        if direction_in:
            voltage = speed * B_field
        else:
            voltage = -speed * B_field
    if current_on != prev_current_on:
        if prev_current_on:
            voltage = voltage - B_field
        else:
            voltage = voltage + B_field

    # Выводим результат
    print(f"Напряжение: {voltage} В")

    prev_current_on = current_on

    # === СТРОКА ИНСТРУКЦИИ ===
    print("\n[ПУЛЬТ] w:Внутрь | s:Наружу | Space:Стоп | +/-:Скорость | o:переключить | q:Выход")

    cmd = input("Ваше действие: ")
    if cmd == 'w':
        is_magnet_moving = True
        direction_in = True
    elif cmd == 's':
        is_magnet_moving = True
        direction_in = False
    elif cmd == ' ':
        is_magnet_moving = False
    elif cmd == '+':
        speed += delta_speed
    elif cmd == '-':
        speed -= delta_speed
    elif cmd == 'o':
        current_on = not current_on
    elif cmd == 'q':
        break
    else:
        message = "- Неизвестная команда -"
