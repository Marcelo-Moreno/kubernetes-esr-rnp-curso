#FROM python:3.10-slim
#WORKDIR /app
#COPY app.py .
#RUN pip install flask
#CMD [ "python", "app.py" ]


# Usa uma imagem base Python oficial
FROM python:3.10-slim-buster

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia o código do aplicativo para o contêiner
COPY app.py .

# Expõe a porta 5000 (a porta padrão do Flask)
EXPOSE 5000

# Define a variável de ambiente para a mensagem (opcional)
ENV APP_MESSAGE="Boas-vindas ao meu App Kubernetes!"

# Comando para executar o aplicativo quando o contêiner for iniciado
CMD ["python", "app.py"]
