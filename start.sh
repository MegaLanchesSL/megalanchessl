#!/bin/bash
echo "Iniciando servidor..."
echo "Conteúdo da pasta templates:"
ls -la /opt/render/project/src/templates/
gunicorn --bind 0.0.0.0:$PORT --log-level debug app:app
