# 📦 Tarefa 3 – Curso de Kubernetes (ESR/RNP)

## 🎯 Objetivo

Executar os seguintes passos para testar a resiliência do Kubernetes em um cluster com 3 nós:

1. Fazer o deploy de uma aplicação web dentro do cluster
2. Identificar em qual node a aplicação foi alocada
3. Simular a queda desse node
4. Observar o comportamento da aplicação e para qual node ela foi realocada
5. Restabelecer o node caído

---

## 🛠️ Aplicação

A aplicação foi desenvolvida em **Python com Flask** e exibe informações úteis como:

- Mensagem personalizada via variável de ambiente
- Nome do host e IP do pod
- IP do cliente (usuário)
- Versão do Flask

### Arquivos principais:

- `app.py`: aplicação web
- `Dockerfile`: imagem container da aplicação
- `requirements.txt`: dependências Python
- `deployment.yaml`: manifesto do Kubernetes para o deploy
- `service.yaml`: expõe a aplicação via NodePort

---

## 🐳 Imagem Docker

A imagem foi publicada no Docker Hub:

📦 [`marcelomoreno/app-esr2:v1`](https://hub.docker.com/r/marcelomoreno/app-esr2)

---

## 🚀 Deploy da aplicação no cluster Kind

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
