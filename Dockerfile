FROM python:3.10-slim

# Instala dependências básicas
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório de trabalho
WORKDIR /docs

# Copia os requirements e instala
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

# Instala o Sphinx diretamente (se necessário)
RUN pip install sphinx

# Copia o conteúdo da pasta docs (pode mudar isso conforme seu projeto)
COPY ./docs /docs

# Comando padrão: gerar a doc
CMD ["sphinx-build", "-b", "html", ".", "_build/html"]
