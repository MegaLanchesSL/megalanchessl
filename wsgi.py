# wsgi.py
'''
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
'''
import sys
import os

# Caminho do projeto
project_folder = '/home/MegaLanchesSaoLeo/megalanchessl'
if project_folder not in sys.path:
    sys.path.insert(0, project_folder)

# Importa a aplicação Flask
from app import app as application

# 🔒 Wrapper para adicionar headers de segurança
def application_with_security_headers(environ, start_response):
    def custom_start_response(status, headers, exc_info=None):
        headers.append(('X-Frame-Options', 'DENY'))
        headers.append(('Content-Security-Policy', "frame-ancestors 'none'"))
        headers.append(('X-Content-Type-Options', 'nosniff'))
        headers.append(('X-XSS-Protection', '1; mode=block'))
        headers.append(('Strict-Transport-Security', 'max-age=31536000; includeSubDomains'))
        return start_response(status, headers, exc_info)
    return application(environ, custom_start_response)

# Substitui a aplicação original pelo wrapper
application = application_with_security_headers
