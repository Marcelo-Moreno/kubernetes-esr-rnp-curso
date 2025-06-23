#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello():
#    return "Olá, ESR da RNP!"

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000)

# Importa a classe Flask do pacote flask
from flask import Flask, request
import os
import socket

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Define uma rota para a URL raiz ("/")
# Quando esta rota é acessada, a função 'hello_world' é executada
@app.route('/')
def hello_world():
    """
    Retorna uma mensagem de saudação e informações básicas sobre o ambiente.
    """
    # Obtém o nome do host da máquina
    hostname = socket.gethostname()
    # Obtém o endereço IP do host (pode retornar 127.0.0.1 em alguns ambientes Docker,
    # mas dentro do pod Kubernetes, será o IP do pod)
    ip_address = socket.gethostbyname(hostname)

    # Tenta obter o valor de uma variável de ambiente 'APP_MESSAGE'.
    # Se a variável não estiver definida, usa uma mensagem padrão.
    app_message = os.environ.get('APP_MESSAGE', 'Olá do aplicativo Python!')

    # Constrói a mensagem de resposta em HTML
    response = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aplicativo Python Simples</title>
        <style>
            body {{
                font-family: 'Inter', sans-serif;
                background-color: #f0f0f0;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }}
            .container {{
                background-color: #ffffff;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 90%;
            }}
            h1 {{
                color: #2c3e50;
                margin-bottom: 20px;
                font-size: 2em;
            }}
            p {{
                font-size: 1.1em;
                line-height: 1.6;
                margin-bottom: 10px;
            }}
            .highlight {{
                font-weight: bold;
                color: #3498db;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{app_message}</h1>
            <p>Este é um aplicativo Python simples rodando em um contêiner.</p>
            <p>Servido de: <span class="highlight">{hostname}</span> (IP: <span class="highlight">{ip_address}</span>)</p>
            <p>Requisição de: <span class="highlight">{request.remote_addr}</span></p>
            <p>Versão do Flask: <span class="highlight">{app.config['FLASK_VERSION']}</span></p>
        </div>
    </body>
    </html>
    """
    return response

# Define uma rota para um endpoint de saúde ("/health")
# Isso é útil para verificações de prontidão (readiness) e vivacidade (liveness) no Kubernetes
@app.route('/health')
def health_check():
    """
    Endpoint de verificação de saúde.
    Retorna um status 200 OK e uma mensagem indicando que o serviço está funcionando.
    """
    return "OK", 200

# Adiciona uma variável de configuração para a versão do Flask (para demonstração)
app.config['FLASK_VERSION'] = '2.2.3' # Use a versão mais recente do Flask que você preferir

# Verifica se o script está sendo executado diretamente (não importado)
if __name__ == '__main__':
    # Obtém a porta do ambiente ou usa a porta 5000 como padrão
    # Kubernetes geralmente expõe portas em contêineres que o serviço pode acessar
    port = int(os.environ.get('PORT', 5000))
    # Inicia o servidor Flask em todas as interfaces de rede (0.0.0.0) e na porta definida
    app.run(debug=True, host='0.0.0.0', port=port)
