# Tarefa 4 - Curso de Kubernetes (ESR/RNP)

## 🎯 Objetivo

Criar um cluster Kubernetes com o Kind, representando dois nodepools:

- **Nodepool A (hardware=low)**: 3 workers para aplicações básicas (nginx)
- **Nodepool B (hardware=high)**: 2 workers para aplicações críticas (apache)

## 🛠️ Etapas realizadas

1. **Criação do cluster Kind** com 1 control-plane, 3 workers (low) e 2 workers (high), via arquivo `kind-config-tarefa4.yaml`
2. **Deploy do nginx** sem taints nem tolerations (`nginx-deployment.yaml`)
3. **Aplicação de taints** nos nodes do nodepool B (hardware=high)
4. **Deploy do apache** com tolerations (`apache-deploy.yaml`)
5. **Verificação de agendamento dos pods** nos nodes corretos
6. **Captura de evidências e geração de PDF**

## 📂 Arquivos

- `kind-config-tarefa4.yaml`: Configuração do cluster Kind
- `nginx-deployment.yaml`: Deployment do nginx (sem toleration)
- `apache-deploy.yaml`: Deployment do apache (com toleration)

## 🧪 Verificações

- `kubectl get nodes --show-labels`
- `kubectl get pods -o wide`
- `kubectl describe node <nome>`
- `kubectl describe pod <pod apache>`
- `kubectl taint nodes <nome> hardware=high:NoSchedule`
