from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список товаров
products = [
    {'name': 'Кокосик', 'desc': 'Песочное печенье с кокосом', 'weight': 0.3, 'quantity': 545, 'price': 35.0},
    {'name': 'Медведи', 'desc': 'Фигурный жевательный мармелад', 'weight': 0.05, 'quantity': 1500, 'price': 33.0},
    {'name': 'Чебурашка', 'desc': 'Прохладительный напиток со вкусом апельсина', 'weight': 1.5, 'quantity': 650, 'price': 45.0},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['desc']
        weight = float(request.form['weight'])
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        products.append({'name': name, 'desc': desc, 'weight': weight, 'quantity': quantity, 'price': price})
        return redirect('/')
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)
