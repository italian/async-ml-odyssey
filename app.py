from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# === СОСТОЯНИЕ ЛАБОРАТОРИИ (Глобальные переменные) ===
# В веб-сервере глобальные переменные работают, пока сервер запущен.
# Для одного пользователя это ок.
lab_state = {
    'current_on': False,  # Включен ли рубильник?
    'progress': 0,        # 0 - новичок, 1 - прошел опыт 1
    'success_count': 0    # Сколько раз прошел импульс?
}

@app.route('/')
def home():
    return render_template('index.html', progress=lab_state['progress'])

@app.route('/experiment/1')
def experiment_one():
    return render_template('experiment_1.html')

# === API: ОБРАБОТКА ДЕЙСТВИЙ (Сюда стучится JavaScript) ===
@app.route('/api/toggle_switch', methods=['POST'])
def api_toggle_switch():
    # 1. Меняем состояние рубильника
    was_on = lab_state['current_on']
    is_on = not was_on # Переключаем (True -> False или False -> True)
    
    lab_state['current_on'] = is_on
    
    # 2. Считаем Физику (Взаимоиндукция)
    voltage = 0.0
    message = ""
    
    is_completed = False
    # Ток возникает только в момент ИЗМЕНЕНИЯ
    if is_on != was_on:
        if is_on:
            # Включение -> Всплеск +
            voltage = 10.0
            message = "ИМПУЛЬС (ВКЛЮЧЕНИЕ)!"
            success_count = lab_state['success_count'] + 1
            lab_state['success_count'] = success_count
        else:
            # Выключение -> Всплеск -
            voltage = -10.0
            message = "ИМПУЛЬС (ВЫКЛЮЧЕНИЕ)!"
            success_count = lab_state['success_count'] + 1
            lab_state['success_count'] = success_count
            
        # Засчитываем прогресс
        if success_count >= 3:
            lab_state['progress'] = 1
            is_completed = True

    # 3. Отправляем ответ обратно в браузер (JSON)
    return jsonify({
        'is_on': is_on,
        'voltage': voltage,
        'message': message,
        'success_count': lab_state['success_count'], # <--- Обязательно
        'is_completed': is_completed,                # <--- Обязательно
        'progress': lab_state['progress']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)