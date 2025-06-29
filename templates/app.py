from flask import Flask, render_template
import os

# Configuração com caminhos absolutos
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__,
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

# Dados do cardápio
cardapio = {
    "lanches": [
        {
            "nome": "Mega X-Tudo",
            "descricao": "Pão, hambúrguer, queijo, presunto, ovo, bacon, alface, tomate e maionese",
            "preco": "R$ 25,90",
            "imagem": "xtudo.jpg"
        },
        {
            "nome": "Mega Bacon",
            "descricao": "Pão, hambúrguer, queijo, bacon crocante e molho especial",
            "preco": "R$ 22,90",
            "imagem": "bacon.jpg"
        },
    ],
    "bebidas": [
        {
            "nome": "Refrigerante Lata",
            "descricao": "Coca-Cola, Guaraná, Fanta Laranja",
            "preco": "R$ 6,00",
            "imagem": "refri.jpg"
        },
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', cardapio=cardapio)

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
