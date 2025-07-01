'''from flask import Flask, render_template
import os

# Configuração com verificação explícita
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')

# Verifica se a pasta templates existe
if not os.path.exists(template_dir):
    raise Exception(f"Pasta de templates não encontrada em: {template_dir}")

app = Flask(__name__,
            template_folder=template_dir,
            static_folder=os.path.join(base_dir, 'static'))

# ... (restante do seu código atual)
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
            "imagem": "xbacon.jpg"
        },
    ],
    "bebidas": [
        {
            "nome": "Refrigerante 200 ml",
            "descricao": "Pepsi, Guaraná",
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

@app.route('/debug')
def debug():
    """Rota para verificar os caminhos"""
    return {
        "base_dir": base_dir,
        "template_dir": template_dir,
        "templates_exist": os.path.exists(template_dir),
        "templates_list": os.listdir(template_dir) if os.path.exists(template_dir) else "Não encontrado"
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
'''
'''from flask import Flask, render_template
import os

# Configuração com verificação explícita
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')

# Verifica se a pasta templates existe
if not os.path.exists(template_dir):
    raise Exception(f"Pasta de templates não encontrada em: {template_dir}")

app = Flask(__name__,
            template_folder=template_dir,
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
            "imagem": "xbacon.jpg"
        },
        # --- NOVO LANCHE AQUI ---
        {
            "nome": "Mega Frango Catupiry",
            "descricao": "Pão, frango desfiado, catupiry cremoso, alface e tomate",
            "preco": "R$ 21,50",
            "imagem": "xtudo.jpg" # Certifique-se de ter esta imagem na pasta static/images
        },
        {
            "nome": "Mega Porção de Violinha",
            "descricao": "violinha frita",
            "preco": "R$ 55,00",
            "imagem": "violinha.jpg" # Certifique-se de ter esta imagem na pasta static/images
        },
        # -----------------------
    ],
    "bebidas": [
        {
            "nome": "Refrigerante Lata",
            "descricao": "Coca-Cola, Guaraná, Fanta Laranja",
            "preco": "R$ 6,00",
            "imagem": "refri.jpg"
        },
        # --- NOVA BEBIDA AQUI ---
        {
            "nome": "Suco Natural Laranja",
            "descricao": "Suco feito na hora com laranjas frescas",
            "preco": "R$ 8,50",
            "imagem": "refri.jpg" # Certifique-se de ter esta imagem na pasta static/images
        },
        {
            "nome": "Água Mineral",
            "descricao": "Água mineral sem gás 500ml",
            "preco": "R$ 4,00",
            "imagem": "refri.jpg" # Certifique-se de ter esta imagem na pasta static/images
        },
        # -----------------------
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

@app.route('/debug')
def debug():
    """Rota para verificar os caminhos"""
    return {
        "base_dir": base_dir,
        "template_dir": template_dir,
        "templates_exist": os.path.exists(template_dir),
        "static_folder": app.static_folder,
        "css_file_exists": os.path.exists(os.path.join(app.static_folder, 'css', 'style.css')),
        "images_folder_exists": os.path.exists(os.path.join(app.static_folder, 'images')),
        "logo_image_exists": os.path.exists(os.path.join(app.static_folder, 'images', 'logo.jpg'))
    }

if __name__ == '__main__':
    app.run(debug=True)
'''
import csv
from flask import Flask, render_template
import os

# Configuração com verificação explícita
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')

# Verifica se a pasta templates existe
if not os.path.exists(template_dir):
    raise Exception(f"Pasta de templates não encontrada em: {template_dir}")

app = Flask(__name__,
            template_folder=template_dir,
            static_folder=os.path.join(base_dir, 'static'))

# --- Início da nova lógica para carregar o cardápio do CSV ---

def carregar_cardapio_do_csv(caminho_csv):
    cardapio_carregado = {
        "lanches": [],
        "bebidas": []
    }
    try:
        with open(caminho_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = {
                    "nome": row['produto'],
                    "descricao": row['descricao'],
                    "preco": row['preco'],
                    "imagem": row['foto']
                }
                if row['tipo'].lower() == 'lanche':
                    cardapio_carregado["lanches"].append(item)
                elif row['tipo'].lower() == 'bebida':
                    cardapio_carregado["bebidas"].append(item)
        print(f"Cardápio carregado com sucesso do CSV: {len(cardapio_carregado['lanches'])} lanches, {len(cardapio_carregado['bebidas'])} bebidas.")
        return cardapio_carregado
    except FileNotFoundError:
        print(f"Erro: Arquivo CSV não encontrado em {caminho_csv}. Usando cardápio padrão ou vazio.")
        # Retorna um cardápio vazio ou um cardápio padrão se o CSV não for encontrado
        return {
            "lanches": [
                # Adicione aqui alguns itens padrão se o CSV não for encontrado,
                # para que o site não fique totalmente vazio.
                # Exemplo:
                # {"nome": "Lanche Padrão", "descricao": "Disponível em breve", "preco": "R$ 0,00", "imagem": "placeholder.jpg"}
            ],
            "bebidas": []
        }
    except Exception as e:
        print(f"Erro ao ler CSV: {e}")
        return {
            "lanches": [],
            "bebidas": []
        }

# Caminho completo para o arquivo CSV
CAMINHO_CARDAPIO_CSV = os.path.join(base_dir, 'cardapio.csv')
cardapio = carregar_cardapio_do_csv(CAMINHO_CARDAPIO_CSV)

# --- Fim da nova lógica ---


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    # O cardápio já está carregado, então apenas passe-o
    return render_template('menu.html', cardapio=cardapio)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/debug')
def debug():
    """Rota para verificar os caminhos e status do cardápio"""
    return {
        "base_dir": base_dir,
        "template_dir": template_dir,
        "templates_exist": os.path.exists(template_dir),
        "static_folder": app.static_folder,
        "css_file_exists": os.path.exists(os.path.join(app.static_folder, 'css', 'style.css')),
        "images_folder_exists": os.path.exists(os.path.join(app.static_folder, 'images')),
        "logo_image_exists": os.path.exists(os.path.join(app.static_folder, 'images', 'logo.jpg')),
        "cardapio_csv_path": CAMINHO_CARDAPIO_CSV,
        "cardapio_csv_exists": os.path.exists(CAMINHO_CARDAPIO_CSV),
        "cardapio_lanches_count": len(cardapio["lanches"]),
        "cardapio_bebidas_count": len(cardapio["bebidas"])
    }

if __name__ == '__main__':
    app.run(debug=True)
