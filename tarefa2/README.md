# Tarefa 2 – Curso Orquestração de Contêineres com Kubernetes (ESR/RNP)

[](https://github.com/Marcelo-Moreno/tarefa2-esr-k8s/blob/main/README.md#tarefa-2--curso-orquestra%C3%A7%C3%A3o-de-cont%C3%AAineres-com-kubernetes-esrrnp)

Este repositório contém os arquivos e configurações utilizados na Tarefa 2 do curso **"Orquestração de Contêineres com Kubernetes"** da **Escola Superior de Redes - RNP**.

---

## ✅ Escopo da Tarefa

[](https://github.com/Marcelo-Moreno/tarefa2-esr-k8s/blob/main/README.md#-escopo-da-tarefa)

- [x]  Provisione um cluster Kubernetes com pelo menos 3 nós utilizando **Kind**
- [x]  Crie uma imagem de uma aplicação simples e publiquei no **Docker Hub**
- [x]  Configure um **Deployment** com 4 réplicas da aplicação no cluster
- [x]  Registre todos os passos com printscreens e organizei o relatório final

---

## 📦 Aplicação

[](https://github.com/Marcelo-Moreno/tarefa2-esr-k8s/blob/main/README.md#-aplica%C3%A7%C3%A3o)

A aplicação é um pequeno servidor em Python com Flask que responde "Olá, ESR da RNP!" na raiz (`/`).

### Código-fonte: `app.py`

[](https://github.com/Marcelo-Moreno/tarefa2-esr-k8s/blob/main/README.md#c%C3%B3digo-fonte-apppy)

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, ESR da RNP!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```