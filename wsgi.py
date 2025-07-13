# wsgi.py
import sys
import os

# Adicione o diretório raiz do seu projeto ao PYTHONPATH
# Isso permite que o PythonAnywhere encontre o 'app.py'
project_folder = '/home/MegaLanchesSaoLeo/megalanchessl' # Substitua SEU_USUARIO_PA pelo seu username no PythonAnywhere
                                                    # E 'megalanchessl' pelo nome da pasta do seu projeto após o clone

if project_folder not in sys.path:
    sys.path.insert(0, project_folder)

# Importa a sua aplicação Flask do app.py
from app import app as application # 'application' é o nome que o PythonAnywhere espera
