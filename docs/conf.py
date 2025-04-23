# docs/conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Informações do projeto
project = 'Seu Projeto'
author = 'Seu Nome ou Time'
release = '0.1'

# Extensões que você já tem
extensions = [
    "sphinxcontrib.openapi",
    "sphinxcontrib.redoc",
]

# Caminhos de templates e arquivos a serem excluídos
templates_path = ['_templates']
exclude_patterns = []

# Tema Read The Docs
html_theme = 'sphinx_rtd_theme'

# Caminho correto para os arquivos estáticos gerados
html_static_path = ['_static']
html_css_files = [
    'pygments.css',  # CSS gerado pelo Sphinx
]

# Se tiver algum arquivo customizado de CSS:
# html_css_files = [
#     '_static/custom.css',  # caso tenha feito um CSS custom
# ]

# Ajuste se estiver acessando via subcaminho
# html_baseurl = '/docs/'  # Se estiver acessando via /docs/ ou outro subpath

# Desabilitar favicon por padrão, se necessário
html_favicon = None
