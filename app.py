from flask import Flask, render_template

app = Flask(__name__)

# Dados do cardápio (simplificado para exemplo)
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
        # Adicione mais itens conforme necessário
    ],
    "bebidas": [
        {
            "nome": "Refrigerante Lata",
            "descricao": "Coca-Cola, Guaraná, Fanta Laranja",
            "preco": "R$ 6,00",
            "imagem": "refri.jpg"
        },
        # Adicione mais itens conforme necessário
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
    app.run(debug=True)