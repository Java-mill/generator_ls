from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

def generate_password(length=12):
    # Создаем набор символов для пароля
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Генерируем пароль заданной длины
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = int(request.form.get('length'))
        password = generate_password(length)
        return render_template('index.html', password=password)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
