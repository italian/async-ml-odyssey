from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# === СОСТОЯНИЕ ЛАБОРАТОРИИ ===
lab_state = {
    'current_on': False,
    'progress': 0,
    'success_count': 0
}

@app.route('/')
def home():
    return render_template('index.html', progress=lab_state['progress'])

@app.route('/experiment/1')
def experiment_one():
    return render_template('experiment_1.html')

@app.route('/api/toggle_switch', methods=['POST'])
def api_toggle_switch():
    was_on = lab_state['current_on']
    is_on = not was_on
    lab_state['current_on'] = is_on
    
    voltage = 0.0
    message = ""
    is_completed = False
    
    if is_on != was_on:
        if is_on:
            voltage = 10.0
            message = "ИМПУЛЬС (ВКЛЮЧЕНИЕ)!"
            lab_state['success_count'] += 1
        else:
            voltage = -10.0
            message = "ИМПУЛЬС (ВЫКЛЮЧЕНИЕ)!"
            lab_state['success_count'] += 1
            
        if lab_state['success_count'] >= 3:
            lab_state['progress'] = 1
            is_completed = True

    return jsonify({
        'is_on': is_on,
        'voltage': voltage,
        'message': message,
        'success_count': lab_state['success_count'],
        'is_completed': is_completed,
        'progress': lab_state['progress']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)