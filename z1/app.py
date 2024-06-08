from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def get_time_greeting():
    current_time = datetime.now().time()
    if current_time >= datetime.strptime('06:00:00', '%H:%M:%S').time() and current_time < datetime.strptime('12:00:00', '%H:%M:%S').time():
        return 'Доброе утро'
    elif current_time >= datetime.strptime('12:00:00', '%H:%M:%S').time() and current_time < datetime.strptime('18:00:00', '%H:%M:%S').time():
        return 'Добрый день'
    elif current_time >= datetime.strptime('18:00:00', '%H:%M:%S').time() and current_time < datetime.strptime('24:00:00', '%H:%M:%S').time():
        return 'Добрый вечер'
    else:
        return 'Доброй ночи'

@app.route('/datetime')
def index():
    greeting = get_time_greeting()
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)