import csv
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for


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
# nova aba pedidos

@app.route("/pedidos", methods=["GET"])
def pedidos():
    return render_template("pedidos.html", cardapio=cardapio)

from flask import request, jsonify

@app.route("/enviar-pedido", methods=["POST"])
def enviar_pedido():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados não recebidos"}), 400

    nome = dados.get("nome")
    telefone = dados.get("telefone")
    endereco = dados.get("endereco")
    descricao = dados.get("descricao")

    caminho_csv = os.path.join(base_dir, "pedidos.csv")
    try:
        with open(caminho_csv, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([nome, telefone, endereco, descricao])
        print(f"Pedido salvo: {nome} - {telefone} - {descricao}")
        return jsonify({"mensagem": "Pedido salvo com sucesso"})
    except Exception as e:
        print("Erro ao salvar pedido:", e)
        return jsonify({"erro": "Erro ao salvar o pedido"}), 500

if __name__ == '__main__':
    app.run(debug=True)
