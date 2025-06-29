from flask import Flask, render_template, request, redirect

app = Flask(__name__)

cardapio = [
    {"nome": "X-Salada", "preco": "R$ 12,00", "imagem": "xsalada.jpg"},
    {"nome": "X-Bacon", "preco": "R$ 14,00", "imagem": "xbacon.jpg"},
    {"nome": "Refrigerante Lata", "preco": "R$ 5,00", "imagem": "refrigerante.jpg"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html", cardapio=cardapio)

@app.route('/pedido', methods=['POST'])
def pedido():
    item = request.form.get('item')
    return redirect(f"https://wa.me/554991853581?text=Quero+fazer+um+pedido:+{item}")

if __name__ == '__main__':
    app.run(debug=True)
